# -*- coding: utf-8 -*-

from imio.smartweb.core.testing import IMIO_SMARTWEB_CORE_INTEGRATION_TESTING
from imio.smartweb.core.viewlets.category import CategoryViewlet
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
import unittest


class SubsiteIntegrationTest(unittest.TestCase):

    layer = IMIO_SMARTWEB_CORE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests"""
        self.request = self.layer["request"]
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_viewlet_on_content_with_no_category(self):
        viewlet = CategoryViewlet(self.portal, self.request, None, None)
        viewlet.update()
        self.assertFalse(viewlet.available())
        self.portal.category = "foo"
        self.assertTrue(viewlet.available())
        self.assertEqual(viewlet.get_category(), "foo")

    def test_viewlet_on_page(self):
        page = api.content.create(
            container=self.portal,
            type="imio.smartweb.Page",
            title="Page",
        )
        viewlet = CategoryViewlet(page, self.request, None, None)
        viewlet.update()
        self.assertFalse(viewlet.available())
        page.category = "publications"
        self.assertEqual(viewlet.get_category(), "Publications")

    def test_viewlet_on_procedure(self):
        procedure = api.content.create(
            container=self.portal,
            type="imio.smartweb.Procedure",
            title="Procedure",
        )
        viewlet = CategoryViewlet(procedure, self.request, None, None)
        viewlet.update()
        self.assertFalse(viewlet.available())
        procedure.category = "taxes_et_redevances"
        self.assertEqual(viewlet.get_category(), "Taxes and fees")
