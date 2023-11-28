import configparser
import os
import sys

if getattr(sys, "frozen", False):
    bundle_dir = sys._MEIPASS
else:
    bundle_dir = os.getcwd()

config = configparser.ConfigParser()

config.read(os.path.join(bundle_dir, "config.ini"))
train_config = config["train"]
