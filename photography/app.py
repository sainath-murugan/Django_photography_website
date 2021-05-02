from django.apps import AppConfig

class PhotographyConfig(AppConfig):
    name = "photography"

    def ready(self):
        import photography.signals