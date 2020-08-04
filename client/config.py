import json


def open_config(indent=False):
    with open("./config.json", "r") as f:
        data = json.load(f)
        if indent:
            data = json.dumps(data, indent=1)
    return data

def save_config(config, admins):
    host = config['host']
    port = config['port']
    code = config['code']

    to_json = {"host": host, "port": port, "code": code}
    with open("./config.json", "w") as f:
        json.dump(to_json, f)
    to_json.update({"admins": admins()})
    with open("./config.json", "w") as f:
        json.dump(to_json, f)
