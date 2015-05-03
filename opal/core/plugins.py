"""
OPAL PLugin - base class and helpers
"""
from opal.utils import _itersubclasses

class OpalPlugin(object):
    """
    Base class from which all of our plugins inherit.
    """
    urls        = []
    javascripts = []
    apis        = []
    stylesheets = []
    menuitems   = []
    actions     = []
    head_extra  = []
    angular_module_deps = []

    def list_schemas(self):
        """
        Return a extra schemas for teams our plugin may have created.
        """
        return {}

    def flows(self):
        """
        Return any extra flows our plugin may hav.e
        """
        return {}

    def roles(self, user):
        """
        Given a USER, return a list of extra roles that this user has.
        """
        return {}
    
    def restricted_teams(self, user):
        """
        Given a USER, return a list of extra teams that user can access.
        """
        return []


def plugins():
    """
    Generator function for plugin instances
    """
    for m in _itersubclasses(OpalPlugin):
        yield m
