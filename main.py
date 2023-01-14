import logging
import logging.handlers
import os

import requests
def log_msg(msg_type, msg):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger_file_handler = logging.handlers.RotatingFileHandler(
        "status.log",
        maxBytes=1024 * 1024,
        backupCount=1,
        encoding="utf8",
    )
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logger_file_handler.setFormatter(formatter)
    logger.addHandler(logger_file_handler)
    if msg_type == 'i': logger.info(msg)

def get_temp () :
    weather_talkpython = 'https://weather.talkpython.fm/api/weather/'
    q_city_weather = weather_talkpython + '?city=Gainesville&state=VA&country=US&units=imperial'
    r = requests.get(q_city_weather)
    if r.status_code == 200:
        data = r.json()
        temperature = data["forecast"]["temp"]
    else:
        temperature = "err"
    return temperature


if __name__ == "__main__":
    try:
        SOME_SECRET = os.environ["SOME_SECRET"]
    except KeyError:
        SOME_SECRET = "Token not available!"
    log_msg('i', f"Token value: {SOME_SECRET}")
    temp = get_temp()
    log_msg('i', f'Temperature in Gainesville, VA, USA: {temp}')