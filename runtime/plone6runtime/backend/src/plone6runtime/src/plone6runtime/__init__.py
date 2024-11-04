"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "plone6runtime"

_ = MessageFactory("plone6runtime")

logger = logging.getLogger("plone6runtime")
