# -*- coding: utf-8 -*-

from imio.smartweb.core.contents.sections.base import ISection
from imio.smartweb.core.contents.sections.base import Section
from imio.smartweb.locales import SmartwebMessageFactory as _
from plone.supermodel import model
from zope.interface import implementer
from zope import schema


class ISectionGallery(ISection):
    """Marker interface and Dexterity Python Schema for SectionGallery"""

    model.fieldset("layout", fields=["image_scale"])
    image_scale = schema.Choice(
        title=_(u"Image scale for images"),
        default=u"preview",
        vocabulary="plone.app.vocabularies.ImagesScales",
        required=True,
    )


@implementer(ISectionGallery)
class SectionGallery(Section):
    """SectionGallery class"""

    manage_content = True
