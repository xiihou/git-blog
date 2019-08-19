from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'App'

    # 信号
    def ready(self):
        from . import signals
        super().ready()
