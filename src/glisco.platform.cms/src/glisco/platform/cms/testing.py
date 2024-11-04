# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import glisco.platform.cms


class GliscoPlatformCmsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=glisco.platform.cms)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "glisco.platform.cms:default")


GLISCO_PLATFORM_CMS_FIXTURE = GliscoPlatformCmsLayer()


GLISCO_PLATFORM_CMS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(GLISCO_PLATFORM_CMS_FIXTURE,),
    name="GliscoPlatformCmsLayer:IntegrationTesting",
)


GLISCO_PLATFORM_CMS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(GLISCO_PLATFORM_CMS_FIXTURE,),
    name="GliscoPlatformCmsLayer:FunctionalTesting",
)


GLISCO_PLATFORM_CMS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        GLISCO_PLATFORM_CMS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="GliscoPlatformCmsLayer:AcceptanceTesting",
)
