# -*- coding: utf-8 -*-

from imio.smartweb.core.contents import IFolder
from imio.smartweb.core.interfaces import IImioSmartwebSubsite
from imio.smartweb.locales import SmartwebMessageFactory as _
from plone import api
from plone.app.layout.navigation.interfaces import INavigationRoot
from plone.dexterity.interfaces import IDexterityContent
from Products.CMFPlone.interfaces.constrains import DISABLED
from Products.CMFPlone.interfaces.constrains import ISelectableConstrainTypes
from Products.Five.browser import BrowserView
from zope.interface import alsoProvides


class FooterSettings(BrowserView):
    """Footer settings"""

    def add_footer(self):
        if not self.available:
            return
        if IFolder.providedBy(self.context):
            container = ISelectableConstrainTypes(self.context)
            constrain_types_mode = container.getConstrainTypesMode()
            container.setConstrainTypesMode(DISABLED)
        pt = api.portal.get_tool("portal_types")
        portal_type = self.context.portal_type
        allowed_content_types = pt.getTypeInfo(portal_type).allowed_content_types
        allowed_content_types = list(allowed_content_types)
        allowed_content_types.append("imio.smartweb.Footer")
        pt.getTypeInfo(portal_type).allowed_content_types = tuple(allowed_content_types)
        footer = api.content.create(
            title="Footer",
            id="footer",
            container=self.context,
            type="imio.smartweb.Footer",
        )
        allowed_content_types.remove("imio.smartweb.Footer")
        pt.getTypeInfo(portal_type).allowed_content_types = tuple(allowed_content_types)
        if IFolder.providedBy(self.context):
            container.setConstrainTypesMode(constrain_types_mode)
        api.portal.show_message(_(u"Footer has been successfully added"), self.request)
        self.request.response.redirect(footer.absolute_url())

    @property
    def available(self):
        if not INavigationRoot.providedBy(
            self.context
        ) and not IImioSmartwebSubsite.providedBy(self.context):
            return False
        footers = self.context.listFolderContents(
            contentFilter={"portal_type": "imio.smartweb.Footer"}
        )
        return len(footers) == 0
