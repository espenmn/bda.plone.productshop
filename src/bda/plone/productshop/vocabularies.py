from zope.interface import directlyProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import (
    SimpleVocabulary,
    SimpleTerm,
)
from zope.i18nmessageid import MessageFactory
from .utils import (
    dotted_name,
    available_variant_aspects,
)

#added by espen
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from bda.plone.productshop.interfaces import IShopTabsSettings



_ = MessageFactory('bda.plone.productshop')


def AvailableVariantAspectsVocabulary(context):
    terms = list()
    for definition in available_variant_aspects():
        terms.append(SimpleTerm(value=dotted_name(definition.interface),
                                title=definition.title))
    return SimpleVocabulary(terms)


directlyProvides(AvailableVariantAspectsVocabulary, IVocabularyFactory)



def RtfFieldsVocabulary(context):
    registry = getUtility(IRegistry)
    settings = registry.forInterface(IShopTabsSettings)
    terms = [ SimpleTerm(value=pair, token=pair, title=pair) for pair in settings]
    return SimpleVocabulary(terms)


directlyProvides(RtfFieldsVocabulary, IVocabularyFactory)

