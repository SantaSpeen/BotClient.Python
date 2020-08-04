import traceback

import requests

from . import shows
from .json_access import open_config


def request(method, args: dict = {}) -> dict:
    try:
        config = open_config()
        r = requests.get(
            "http://" + config["host"] + ":" + config["port"] + "/api/" + method + "?code=" + config["code"],
            params=args).json()
    except Exception as e:
        to_print = traceback.format_exc()
        print(to_print)
        shows.error("Соболезную, но у тебя ошибка:\n"+str(e))
        r = {"error": {"msg": "Ошибка скрипта.."}}
    if r.get("error"):
        shows.error("Что-то не так в запросе: " + r["error"]["msg"])
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
