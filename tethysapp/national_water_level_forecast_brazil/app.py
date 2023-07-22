from tethys_sdk.base import TethysAppBase


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