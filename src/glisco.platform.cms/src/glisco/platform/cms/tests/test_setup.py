# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from glisco.platform.cms.testing import (  # noqa: E501
    GLISCO_PLATFORM_CMS_INTEGRATION_TESTING,
)
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that glisco.platform.cms is properly installed."""

    layer = GLISCO_PLATFORM_CMS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if glisco.platform.cms is installed."""
        self.assertTrue(self.installer.is_product_installed("glisco.platform.cms"))

    def test_browserlayer(self):
        """Test that IGliscoPlatformCmsLayer is registered."""
        from glisco.platform.cms.interfaces import IGliscoPlatformCmsLayer
        from plone.browserlayer import utils

        self.assertIn(IGliscoPlatformCmsLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = GLISCO_PLATFORM_CMS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("glisco.platform.cms")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if glisco.platform.cms is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("glisco.platform.cms"))

    def test_browserlayer_removed(self):
        """Test that IGliscoPlatformCmsLayer is removed."""
        from glisco.platform.cms.interfaces import IGliscoPlatformCmsLayer
        from plone.browserlayer import utils

        self.assertNotIn(IGliscoPlatformCmsLayer, utils.registered_layers())
