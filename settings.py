import json


def configsettings():
    configfile = open('config.json')
    return json.load(configfile)