# -*- coding: utf-8 -*-

from collective.geolocationbehavior.geolocation import IGeolocatable
from imio.smartweb.core.interfaces import IImioSmartwebCoreLayer
from imio.smartweb.core.testing import IMIO_SMARTWEB_CORE_INTEGRATION_TESTING
from imio.smartweb.core.testing import ImioSmartwebTestCase
from imio.smartweb.core.tests.utils import get_sections_types
from plone import api
from plone.app.testing import login
from plone.app.testing import logout
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.formwidget.geolocation.geolocation import Geolocation
from plone.namedfile.file import NamedBlobFile
from plone.protect.authenticator import createToken
from time import sleep
from z3c.relationfield import RelationValue
from zope.annotation.interfaces import IAnnotations
from zope.component import getMultiAdapter
from zope.component import getUtility
from zope.component import queryMultiAdapter
from zope.interface import alsoProvides
from zope.intid.interfaces import IIntIds
from zope.lifecycleevent import modified


class TestSections(ImioSmartwebTestCase):

    layer = IMIO_SMARTWEB_CORE_INTEGRATION_TESTING

    def setUp(self):
        # Number of sections where there is a title if section is empty.
        # sectionHTML,...
        self.NUMBER_OF_EMPTY_SECTIONS = 9
        self.request = self.layer["request"]
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.page = api.content.create(
            container=self.portal,
            type="imio.smartweb.Page",
            id="page",
        )

    def test_redirection(self):
        section = api.content.create(
            container=self.page,
            type="imio.smartweb.SectionText",
            title="Section text",
            id="text",
        )
        getMultiAdapter((section, self.request), name="view")()
        self.assertEqual(
            self.request.response.headers["location"],
            "http://nohost/plone/page#section-text",
        )

    def test_get_last_mofication_date(self):
        section = api.content.create(
            container=self.page,
            type="imio.smartweb.SectionText",
            title="Section text",
        )
        self.assertEqual(section.get_last_mofication_date, section.ModificationDate())
        section = api.content.create(
            container=self.page,
            type="imio.smartweb.SectionGallery",
            title="Section Gallery",
        )
        self.assertEqual(section.get_last_mofication_date, section.ModificationDate())
        first_modification = section.get_last_mofication_date
        sleep(1)
        # adding an image to a section causes a reindex of the section, thus
        # changes its last modification date
        api.content.create(
            container=section,
            type="Image",
            title="Image",
        )
        next_modification = section.get_last_mofication_date
        self.assertNotEqual(first_modification, next_modification)

    def test_files_informations(self):
        section = api.content.create(
            container=self.page,
            type="imio.smartweb.SectionFiles",
            title="Section files",
        )
        file_obj = api.content.create(
            container=section,
            type="File",
            title="My file",
        )
        file_obj.file = NamedBlobFile(data="file data", filename="file.txt")
        view = queryMultiAdapter((section, self.request), name="view")
        self.assertEqual(view.get_thumb_scale_list(), "thumb")

        api.portal.set_registry_record("plone.thumb_scale_listing", "preview")
        annotations = IAnnotations(self.request)
        del annotations["plone.memoize"]
        view = queryMultiAdapter((section, self.request), name="view")
        self.assertEqual(view.get_thumb_scale_list(), "preview")

        api.portal.set_registry_record("plone.no_thumbs_lists", True)
        annotations = IAnnotations(self.request)
        del annotations["plone.memoize"]
        view = queryMultiAdapter((section, self.request), name="view")
        self.assertIsNone(view.get_thumb_scale_list())

        view = queryMultiAdapter((self.page, self.request), name="full_view")
        self.assertIn("1 KB", view())

    def test_video_section(self):
        section = api.content.create(
            container=self.page,
            type="imio.smartweb.SectionVideo",
            title="Section video",
        )
        section.video_url = "https://www.youtube.com/watch?v=_dOAthafoGQ"
        view = queryMultiAdapter((section, self.request), name="view")
        embedded_video = view.get_embed_video()
        self.assertIn("iframe", embedded_video)
        self.assertIn(
            "https://www.youtube.com/embed/_dOAthafoGQ?feature=oembed", embedded_video
        )

    def test_map_section(self):
        section = api.content.create(
            container=self.page,
            type="imio.smartweb.SectionMap",
            title="Section map",
        )
        IGeolocatable(section).geolocation = Geolocation(latitude="4.5", longitude="45")
        view = queryMultiAdapter((self.page, self.request), name="full_view")
        self.assertIn("Section map", view())
        self.assertIn('class="pat-leaflet map"', view())

    def test_selections_section(self):
        section = api.content.create(
            container=self.page,
            type="imio.smartweb.SectionSelections",
            title="Section selections",
        )
        page2 = api.content.create(
            container=self.portal, type="imio.smartweb.Page", title="Page 2"
        )
        intids = getUtility(IIntIds)
        section.selected_items = [
            RelationValue(intids.getId(page2)),
        ]
        view = queryMultiAdapter((section, self.request), name="table_view")
        self.assertIn("Page 2", [item[0]["title"] for item in view.items()])
        view = queryMultiAdapter((self.page, self.request), name="full_view")
        self.assertIn("Page 2", view())

    def test_collection_section(self):
        portal_page = api.content.create(
            container=self.portal,
            type="imio.smartweb.PortalPage",
            title="Portal page",
        )
        section_gallery = api.content.create(
            container=self.page,
            type="imio.smartweb.SectionGallery",
            title="Section gallery",
        )
        for i in range(0, 10):
            api.content.create(
                container=section_gallery,
                type="Image",
                title=f"Image{i}",
            )
        query = [
            {
                "i": "portal_type",
                "o": "plone.app.querystring.operation.selection.any",
                "v": ["Image"],
            }
        ]
        collection = api.content.create(
            container=self.portal,
            type="Collection",
            title="My collection",
        )
        collection.setQuery(query)
        self.assertEqual(len(collection.results()), 10)
        section_collection = api.content.create(
            container=portal_page,
            type="imio.smartweb.SectionCollection",
            title="Section collection",
        )
        intids = getUtility(IIntIds)
        section_collection.collection = RelationValue(intids.getId(collection))
        section_collection.nb_results_by_batch = 1
        view = queryMultiAdapter((section_collection, self.request), name="table_view")
        self.assertEqual(len(view.items()), 6)
        section_collection.max_nb_results = 10
        view = queryMultiAdapter((section_collection, self.request), name="table_view")
        self.assertEqual(len(view.items()), 10)

    def test_sections_ordering(self):
        page = api.content.create(
            container=self.portal,
            type="imio.smartweb.Page",
            title="Page",
        )
        alsoProvides(self.request, IImioSmartwebCoreLayer)
        api.content.create(
            container=page,
            type="imio.smartweb.SectionGallery",
            title="Section 1",
            id="section1",
        )
        api.content.create(
            container=page,
            type="imio.smartweb.SectionText",
            title="Section 2",
            id="section2",
        )
        self.assertListEqual(page.objectIds(), ["section1", "section2"])
        self.request.form["_authenticator"] = createToken()
        self.request.form["id"] = "section2"
        self.request.form["delta"] = "-1"
        self.request.form["orderedSectionsIds"] = '["section1", "section2"]'
        self.request.environ["REQUEST_METHOD"] = "POST"
        getMultiAdapter((page, self.request), name="reorder-section")()
        self.assertListEqual(page.objectIds(), ["section2", "section1"])

        self.request.form["id"] = "section1"
        self.request.form["delta"] = "-1"
        # wrong ordered sections ids
        self.request.form["orderedSectionsIds"] = '["section1", "section2"]'
        getMultiAdapter((page, self.request), name="reorder-section")()
        # nothing changes
        self.assertListEqual(page.objectIds(), ["section2", "section1"])

    def test_empty_sections(self):
        page = api.content.create(
            container=self.portal,
            type="imio.smartweb.Page",
            title="Page",
        )
        api.content.transition(page, "publish")
        section_types = get_sections_types()
        for section_type in section_types:
            api.content.create(
                container=page,
                type=section_type,
                title="Title of my {}".format(section_type),
            )
        video_section = getattr(page, "title-of-my-imio-smartweb-sectionvideo")
        video_section.video_url = "https://www.youtube.com/watch?v=_dOAthafoGQ"
        selections_section = getattr(
            page, "title-of-my-imio-smartweb-sectionselections"
        )
        intids = getUtility(IIntIds)
        selections_section.selected_items = [
            RelationValue(intids.getId(self.page)),
        ]
        view = queryMultiAdapter((page, self.request), name="full_view")()
        self.assertEqual(
            view.count('<h2 class="section-title">Title of my '), len(section_types)
        )
        logout()
        view = queryMultiAdapter((page, self.request), name="full_view")()
        self.assertEqual(view.count('<h2 class="section-title">Title of my '), 6)
        login(self.portal, "test")
        gallery_section = getattr(page, "title-of-my-imio-smartweb-sectiongallery")
        api.content.create(
            container=gallery_section,
            type="Image",
            title="Image",
        )
        files_section = getattr(page, "title-of-my-imio-smartweb-sectionfiles")
        file_obj = api.content.create(
            container=files_section,
            type="File",
            title="My file",
        )
        file_obj.file = NamedBlobFile(data="file data", filename="file.txt")
        links_section = getattr(page, "title-of-my-imio-smartweb-sectionlinks")
        api.content.create(
            container=links_section,
            type="imio.smartweb.BlockLink",
            title="My link",
        )
        view = queryMultiAdapter((page, self.request), name="full_view")()
        self.assertEqual(
            view.count('<h2 class="section-title">Title of my '), len(section_types)
        )

    def test_sections_titles(self):
        page = api.content.create(
            container=self.portal,
            type="imio.smartweb.Page",
            title="Page",
        )
        api.content.transition(page, "publish")
        section_types = get_sections_types()
        for section_type in section_types:
            api.content.create(
                container=page,
                type=section_type,
                title="Title of my {}".format(section_type),
            )
        video_section = getattr(page, "title-of-my-imio-smartweb-sectionvideo")
        video_section.video_url = "https://www.youtube.com/watch?v=_dOAthafoGQ"
        gallery_section = getattr(page, "title-of-my-imio-smartweb-sectiongallery")
        api.content.create(
            container=gallery_section,
            type="Image",
            title="Image",
        )
        files_section = getattr(page, "title-of-my-imio-smartweb-sectionfiles")
        file_obj = api.content.create(
            container=files_section,
            type="File",
            title="My file",
        )
        file_obj.file = NamedBlobFile(data="file data", filename="file.txt")
        links_section = getattr(page, "title-of-my-imio-smartweb-sectionlinks")
        api.content.create(
            container=links_section,
            type="imio.smartweb.BlockLink",
            title="My link",
        )
        selections_section = getattr(
            page, "title-of-my-imio-smartweb-sectionselections"
        )
        intids = getUtility(IIntIds)
        selections_section.selected_items = [
            RelationValue(intids.getId(self.page)),
        ]

        view = queryMultiAdapter((page, self.request), name="full_view")()
        self.assertEqual(
            view.count('<h2 class="section-title">Title of my '), len(section_types)
        )
        # test hide_title
        for section_id in page.objectIds():
            section = getattr(page, section_id)
            section.hide_title = True
        # hide_title in login mode (add some specific css class)
        view = queryMultiAdapter((page, self.request), name="full_view")()
        self.assertEqual(
            view.count('<h2 class="hidden-section-title hide-in-preview">Title of my '),
            self.NUMBER_OF_EMPTY_SECTIONS,
        )
        # hide_title in logout mode (no more <h2> / title)
        logout()
        view = queryMultiAdapter((page, self.request), name="full_view")()
        self.assertEqual(view.count("</h2>"), 0)

    def test_sections_titles_display_switch(self):
        page = api.content.create(
            container=self.portal,
            type="imio.smartweb.Page",
            title="Page",
        )
        api.content.transition(page, "publish")
        # We can't edit title visibility of Contact & Text sections.
        # And visibility of these sections titles is False.
        for section_type in [
            "imio.smartweb.SectionContact",
            "imio.smartweb.SectionText",
        ]:
            section = api.content.create(
                container=page,
                type=section_type,
                title="Title of my {}".format(section_type),
            )
            section.hide_title = True
            view = queryMultiAdapter((section, self.request), name="hide_section_title")
            view.hide_section_title()
            self.assertTrue(section.hide_title)
            view = queryMultiAdapter((section, self.request), name="show_section_title")
            view.show_section_title()
            self.assertTrue(section.hide_title)
            view = queryMultiAdapter((page, self.request), name="full_view")
            self.assertNotIn("Show title", view())

        section = api.content.create(
            container=page,
            type="imio.smartweb.SectionGallery",
            title="Title of my galery",
        )
        view = queryMultiAdapter((section, self.request), name="hide_section_title")
        view.hide_section_title()
        self.assertTrue(section.hide_title)
        view = queryMultiAdapter((section, self.request), name="show_section_title")
        view.show_section_title()
        self.assertFalse(section.hide_title)

    def test_background_style(self):
        section = api.content.create(
            container=self.page,
            type="imio.smartweb.SectionText",
            title="Section text",
        )
        view = queryMultiAdapter((section, self.request), name="view")
        self.assertEqual(view.background_style(), "")
        section.background_image = NamedBlobFile(data="file data", filename="file.png")
        self.assertIn(
            "background-image:url('http://nohost/plone/page/section-text/@@images/background_image/large')",
            view.background_style(),
        )

    def test_sections_worflows(self):
        wf_tool = api.portal.get_tool("portal_workflow")
        section_types = get_sections_types()
        for section_type in section_types:
            obj = api.content.create(
                container=self.page,
                type=section_type,
                title="Title of my {}".format(section_type),
            )
            chain = wf_tool.getChainFor(obj)
            self.assertEqual(chain, ())

    def test_section_html(self):
        section_html = api.content.create(
            container=self.page,
            type="imio.smartweb.SectionHTML",
            title="Section html",
            id="section-html",
            html="",
        )
        section_html.html = (
            '<div><h1>Perdu.com</h1><embed src="http://www.perdu.com"></embed></div>'
        )
        modified(section_html)
        page_html = getMultiAdapter((self.page, self.request), name="full_view")()
        self.assertIn("Perdu.com", page_html)
        self.assertNotIn("iframe", page_html)
