import configparser
import logging

logging.basicConfig(level=logging.DEBUG, 
                    filename='log.log', 
                    filemode="w" ,
                    format="%(asctime)s - %(levelname)s - %(message)s" )

logger = logging.getLogger(__name__)
handler = logging.FileHandler('log/app.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

# Config file 
config = configparser.ConfigParser()
config.read('config.ini')

userName = config.get('User', 'user_name')
password = config.get('User', 'password')

print(userName)
print(password)

logger.info(f"username: {userName}" )
logger.info(f"Password: {password}" )