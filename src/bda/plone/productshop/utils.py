from zope.component import getUtilitiesFor
from plone.behavior.interfaces import IBehavior
from z3c.form.field import Fields
from .interfaces import IVariantAspect


def dotted_name(obj):
    return '%s.%s' % (obj.__module__, obj.__name__)


def request_property(func):
    """Decorator like ``property``, but underlying function is only called once
    per request.

    Cache attribute on request under key
    ``instanceid.classname.funcname``.

    Works only on instances providing a ``request`` attribute.
    """
    def wrapper(self):
        cache_key = '%s.%s.%s' \
            % (str(id(self)), self.__class__.__name__, func.__name__)
        try:
            return getattr(self.request, cache_key)
        except AttributeError:
            val = func(self)
            setattr(self.request, cache_key, val)
            return val
    wrapper.__doc__ = func.__doc__
    return property(wrapper)


class VariantAspectDefinition(object):

    def __init__(self, interface):
        fields = Fields(interface)
        if len(fields) != 1:
            raise ValueError(u'Variant aspect schema must provide exactly 1 '
                             u'field')
        for key in fields:
            break
        self.attribute = key
        self.title = fields[self.attribute].field.title
        self.interface = interface


def available_variant_aspects():
    aspects = list()
    for behavior in getUtilitiesFor(IBehavior):
        interface = behavior[1].interface
        if interface.isOrExtends(IVariantAspect):
            aspects.append(VariantAspectDefinition(interface))
    return aspects
