import json


def congifsettings():
    configfile = open('config.json')
    return json.load(configfile)