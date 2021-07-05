import sys
import os
import os.path
from configparser import ConfigParser

config_file = "settings.ini"
config = ConfigParser()

if os.environ.get('DEV'):
    print("Starting in development mode.")
    config_path = os.path.join(os.getcwd(), config_file)
else:
    config_folder = os.path.join(os.path.expanduser("~"), '.config', 'deezer-dl')
    os.makedirs(config_folder, exist_ok=True)
    config_path = os.path.join(config_folder, config_file)

if not os.path.exists(config_path):
    print(f"Could not find config file ({config_path}).")
    sys.exit(1)

print(f"Loading {config_path}")
config.read(config_path)

if "DEEZER_FLAC_QUALITY" in os.environ.keys():
    config["deezer"]["flac_quality"] = os.environ["DEEZER_FLAC_QUALITY"]

if "flac_quality" not in config['deezer'] or config['deezer'].getboolean('flac_quality') not in (True, False):
    print("flac_quality muste be set (True or False)")
    sys.exit(1)

if "DEEZER_COOKIE_ARL" in os.environ.keys():
    config["deezer"]["cookie_arl"] = os.environ["DEEZER_COOKIE_ARL"]
