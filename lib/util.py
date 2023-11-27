import configparser
import os
import sys

config = configparser.ConfigParser()

if getattr(sys, "frozen", False):
    bundle_dir = sys._MEIPASS
else:
    bundle_dir = os.getcwd()

config.read(os.path.join(bundle_dir, "config.ini"))
train_config = config["train"]
