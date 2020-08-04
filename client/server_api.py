import traceback

import requests

from . import shows
from .config import open_config


def request(method, args={}):
    try:
        config = open_config()
        r = requests.get("http://"+config["host"]+":"+config["port"]+"/api/"+method+"?code="+config["code"], params=args).json()
        if r.get("error"):
            shows.error("Что-то не так в запросе: " + r["error"]["msg"])
    except:
        to_print = traceback.format_exc()
        shows.error(to_print)
        r = {}
    return r

def bot_isActive() -> bool:

    r = request("isActive")
    return r["response"]["status"]

def bot_stat() -> list:

    r = request("stat")["response"]
    return [r["uptime"], r["event_time"], r["message_counter"]]

def bot_getAdmins():

    r = request("getAdmins")["response"]["admins"]
    return r