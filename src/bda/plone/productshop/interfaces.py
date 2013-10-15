from zope.interface import Interface
from plone.namedfile.interfaces import IImageScaleTraversable
from collective.instancebehavior import IInstanceBehaviorAssignableContent

#added by espen
#not sure if all is needed
#from plone.registry.interfaces import IRegistry
from zope.i18nmessageid import MessageFactory
from z3c.form import interfaces
from zope import schema
from zope.interface import alsoProvides
from plone.directives import form
from bda.plone.shop.interfaces import IShopSettingsProvider

_ = MessageFactory('bda.plone.productshop')


class IProductShopExtensionLayer(Interface):
    """Product shop specific browser layer.
    """


##############################################################################
# content markers
##############################################################################

class IProduct(Interface, IImageScaleTraversable):
    """Marker interface for product content.
    """


class IProductGroup(IProduct):
    """Marker interface for product group content.
    """


class IVariant(IProduct, IInstanceBehaviorAssignableContent):
    """Marker interface for variant content.
    """


class IVariantAspect(Interface):
    """Aspect of a variant.
    """


                                                         
      
##############################################################################
# control panel (tab)
##############################################################################
                            
class IShopTabsSettings(form.Schema):
    """Adds settings to bda.plone.shop's controlpanel
    """

    form.fieldset(
        'tabs',
        label=_(u'TabsSettings'),
        fields=[
            'rtf_fields',
            ],
        )

    rtf_fields = schema.Choice(
                        title=_(u"Render which (rtf) fields as Tabs"),
                        vocabulary='bda.plone.productshop.RtfFieldsVocabulary'
                        )




alsoProvides(IShopTabsSettings, IShopSettingsProvider)