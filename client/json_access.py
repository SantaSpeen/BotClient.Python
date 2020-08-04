import json

CONFIG = "./jsons/config.json"
VARS = "./jsons/global_vars.json"


def read(file):
    with open(file, "r") as f:
        data = json.load(f)
    return data


def save(file, data):
    with open(file, "w") as f:
        json.dump(data, f)


def open_config(indent=False):
    data = read(CONFIG)
    if indent:  data = json.dumps(data, indent=1)
    return data


def save_config(config, admins):
    to_json = {"host": config['host'], "port": config['port'], "code": config['code']}
    save(CONFIG, to_json)

    to_json.update({"admins": admins()})
    save(CONFIG, to_json)


def open_global_vars():
    return read(VARS)


def save_global_vars(setting_open=False):
    to_json = {
        "setting_open": setting_open
    }
    save(VARS, to_json)
