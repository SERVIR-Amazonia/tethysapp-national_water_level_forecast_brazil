from tethys_sdk.base import TethysAppBase
from tethys_sdk.app_settings import CustomSetting


class NationalWaterLevelForecastBrazil(TethysAppBase):
    """
    Tethys app class for National Water Level Forecast Brazil.
    """

    name = 'National Water Level Forecast Brazil'
    description = ''
    package = 'national_water_level_forecast_brazil'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'national-water-level-forecast-brazil'
    color = '#009c3b'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def custom_settings(self):
        return (
            CustomSetting(
                name='SERVER',
                type=CustomSetting.TYPE_STRING,
                description='Server DNS or IP:PORT',
                required=True,
                default='localhost:8080',
            ),
            CustomSetting(
                name='DB_USER',
                type=CustomSetting.TYPE_STRING,
                description='Database user',
                required=True,
                default='postgres',
            ),
            CustomSetting(
                name='DB_PASS',
                type=CustomSetting.TYPE_STRING,
                description='Database password',
                required=True,
                default='pass',
            ),
            CustomSetting(
                name='DB_NAME',
                type=CustomSetting.TYPE_STRING,
                description='Database name',
                required=True,
                default='postgres',
            ),
        )