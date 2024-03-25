import app_config as cfg

print('trying to import app-config...')
user_name = cfg.config.get('user', 'user_name')
print("UserName: ",user_name)


