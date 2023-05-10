from django.apps import AppConfig


class ListConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'List'

    def ready(self):
        import List.signals
