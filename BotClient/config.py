import json


def open_config(indent=False):
    with open("./BotClient/config.json", "r") as f:
        data = json.load(f)
        if indent:
            data = json.dumps(data, indent=1)
    return data

def save_config(config):
    host = config['host']
    port = config['port']
    token = config['token']

    to_json = {"host":host, "port": port, "token": token}
    with open("./BotClient/config.json", "w") as f:
        json.dump(to_json, f)
