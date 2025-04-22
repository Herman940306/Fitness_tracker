''' Pre-condition: Ensure that the Django framework is properly installed and
configured.

# Post-condition: The MembersConfig class is registered as the configuration
for the 'members' app. '''
from django.apps import AppConfig


# This class is used to configure the members app in Django.
class MembersConfig(AppConfig):
    """Configuration for the members app."""
    # The default auto field type for primary keys in models.
    default_auto_field = "django.db.models.BigAutoField"
    name = "members"
