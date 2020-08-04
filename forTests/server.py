import time

from flask import *

app = Flask("Bot")

admins = [45634563, 453455, 312321]


# TODO: Сделаить норльный сервер
@app.route("/api/<path:method>")
def api(method):
    r = {"response": {}}
    if method == "isActive":
        r["response"].update({"status": True})
    elif method == "stat":
        r["response"].update({"uptime": "40 сек", "event_time": "0.1234123", "message_counter": "157"})
    elif method == "getAdmins":
        r["response"].update({"admins": admins})
    else:
        r = {"error": {"code": 1, "msg": "Api method not found"}}
    return jsonify(r)


def start(port):
    app.run("127.0.0.1", port)


# TODO: Сделать генерацию порта...
if __name__ == '__main__':
    start(3)
