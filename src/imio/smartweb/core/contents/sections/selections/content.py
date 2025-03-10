# -*- coding: utf-8 -*-

from imio.smartweb.core.contents.sections.base import ISection
from imio.smartweb.core.contents.sections.base import Section
from imio.smartweb.locales import SmartwebMessageFactory as _
from plone.app.vocabularies.catalog import CatalogSource
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope import schema
from zope.interface import implementer


class ISectionSelections(ISection):
    """Marker interface and Dexterity Python Schema for SectionSelections"""

    selected_items = RelationList(
        title=_(u"Selected items"),
        value_type=RelationChoice(
            title=u"",
            source=CatalogSource(),
        ),
        required=True,
    )

    model.fieldset("layout", fields=["show_items_lead_image", "image_scale"])
    show_items_lead_image = schema.Bool(
        title=_(u"Show items lead image"), default=False, required=False
    )

    image_scale = schema.Choice(
        title=_(u"Image scale for items"),
        default=u"tile",
        vocabulary="plone.app.vocabularies.ImagesScales",
        required=True,
    )


@implementer(ISectionSelections)
class SectionSelections(Section):
    """SectionSelections class"""

    manage_content = False
    manage_display = True
