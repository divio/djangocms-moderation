from django.core.exceptions import ImproperlyConfigured

from cms.app_base import CMSAppExtension


class ModerationExtension(CMSAppExtension):

    def __init__(self):
        self.moderated_models = []

    def configure_app(self, cms_config):
        versioning_enabled = getattr(cms_config, 'djangocms_versioning_enabled', False)
        moderated_models = getattr(cms_config, 'moderated_models', [])
        versioning_models = getattr(cms_config, 'versioning_models', [])

        if not versioning_enabled:
            raise ImproperlyConfigured('Versioning needs to be enabled for Moderation')

        for moderated_model in moderated_models:
            if moderated_model not in versioning_models:
                raise ImproperlyConfigured(
                    'Moderated models need to be Versionable, please include every '
                    'model that needs to be moderated in versioning_models entry'
                )

        self.moderated_models.extend(moderated_models)