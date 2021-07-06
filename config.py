import configparser

config = configparser.ConfigParser()
try:
    config.read('config')
except:
    raise FileNotFoundError('Config not found')
