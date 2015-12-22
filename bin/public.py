import fitbit
import ConfigParser
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()

# Load Settings
parser = ConfigParser.SafeConfigParser()
parser.read('config.ini')
consumer_key = parser.get('Login Parameters', 'C_KEY')
consumer_secret = parser.get('Login Parameters', 'C_SECRET')
user_key = parser.get('Login Parameters', 'U_KEY')
user_secret = parser.get('Login Parameters', 'U_SECRET')

unauth_client = fitbit.Fitbit(consumer_key, consumer_secret)
# certain methods do not require user keys
unauth_client.food_units()


# You'll have to gather the user keys on your own, or try
# ./gather_keys_cli.py <consumer_key> <consumer_secret> for development
authd_client = fitbit.Fitbit(consumer_key, consumer_secret, resource_owner_key=user_key, resource_owner_secret=user_secret)
activity_stats = authd_client._COLLECTION_RESOURCE('activities')

print activity_stats

authd_client.sleep()