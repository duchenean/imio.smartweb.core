# -*- coding: utf-8 -*-

from imio.smartweb.core.contents.sections.base import ISection
from imio.smartweb.core.contents.sections.base import Section
from imio.smartweb.locales import SmartwebMessageFactory as _
from plone.app.vocabularies.catalog import CatalogSource
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.app.z3cform.widget import SelectFieldWidget
from plone.autoform import directives
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from zope import schema
from zope.interface import implementer


class ISectionNews(ISection):
    """Marker interface and Dexterity Python Schema for SectionNews"""

    directives.widget(related_news=SelectFieldWidget)
    related_news = schema.Choice(
        title=_(u"Related news folder"),
        source="imio.smartweb.vocabulary.RemoteNewsFolders",
        required=True,
    )

    directives.widget(
        "linking_rest_view",
        RelatedItemsFieldWidget,
        vocabulary="plone.app.vocabularies.Catalog",
        pattern_options={
            "selectableTypes": ["imio.smartweb.NewsView"],
            "favorites": [],
        },
    )
    linking_rest_view = RelationChoice(
        title=_(u"News view used to display news items details"),
        source=CatalogSource(),
        required=True,
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

    model.fieldset("layout", fields=["image_scale"])
    image_scale = schema.Choice(
        title=_(u"Image scale for news"),
        default=u"tile",
        vocabulary="plone.app.vocabularies.ImagesScales",
        required=True,
    )


@implementer(ISectionNews)
class SectionNews(Section):
    """SectionNews class"""
