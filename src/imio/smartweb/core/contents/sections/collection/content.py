# -*- coding: utf-8 -*-

from imio.smartweb.core.contents.sections.base import ISection
from imio.smartweb.core.contents.sections.base import Section
from imio.smartweb.locales import SmartwebMessageFactory as _
from plone.app.vocabularies.catalog import CatalogSource
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from zope.interface import implementer
from zope import schema


class ISectionCollection(ISection):
    """Marker interface and Dexterity Python Schema for SectionCollection"""

    directives.widget(
        "collection",
        RelatedItemsFieldWidget,
        vocabulary="plone.app.vocabularies.Catalog",
        pattern_options={
            "selectableTypes": ["Collection"],
            "favorites": [],
        },
    )
    collection = RelationChoice(
        title=_(u"Select a collection"),
        source=CatalogSource(),
    )

    max_nb_results = schema.Int(
        title=_(u"Maximum number of items to display"),
        required=True,
        default=6,
        min=1,
        max=12,
    )

    nb_results_by_batch = schema.Choice(
        title=_(u"Number of items per batch"),
        required=True,
        default=3,
        values=[1, 3, 4],
    )

    link_text = schema.TextLine(
        title=_(u"Text for the link to the collection"), required=False
    )

    model.fieldset(
        "layout",
        fields=[
            "show_items_lead_image",
            "show_items_description",
            "show_items_publication_date",
            "image_scale",
        ],
    )
    show_items_lead_image = schema.Bool(
        title=_(u"Show items lead image"), required=False
    )

    show_items_description = schema.Bool(
        title=_(u"Show items description"), required=False
    )

    show_items_publication_date = schema.Bool(
        title=_(u"Show items publication date"), required=False
    )

    image_scale = schema.Choice(
        title=_(u"Image scale for items"),
        default=u"preview",
        vocabulary="plone.app.vocabularies.ImagesScales",
        required=True,
    )


@implementer(ISectionCollection)
class SectionCollection(Section):
    """SectionCollection class"""

    manage_display = True
