import os
import configparser


current_dir = os.getcwd()
print("current dir", current_dir);

config = configparser.ConfigParser()
config_path = './config.ini'
mypath = os.path.abspath(config_path)
config.read(config_path)

print('App config setup has been completed.')