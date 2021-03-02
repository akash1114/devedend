from django.apps import AppConfig


class StockDataConfig(AppConfig):
    name = 'devedend_data'
    def ready(self):
        from devedend_data.sheculer import updater
        updater.start()
