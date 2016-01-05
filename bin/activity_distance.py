import os, fitbit, json
import datetime as dt
import ConfigParser
# import requests.packages.urllib3
# requests.packages.urllib3.disable_warnings()

# Setup Splunk Environment
# Setup Splunk Environment
APPNAME = 'Splunk_TA_fit'
CONFIG = '/bin/config.ini'
SPLUNK_HOME = os.environ['SPLUNK_HOME']
TOKEN_CONFIG = '/bin/user_settings.txt'

tokenfile = SPLUNK_HOME + '/etc/apps/' + APPNAME + TOKEN_CONFIG

parser = ConfigParser.SafeConfigParser()
parser.read(SPLUNK_HOME + '/etc/apps/' + APPNAME + CONFIG)
DATE_INTERVAL = parser.get('Activity', 'DATE_INTERVAL')
TIME_INTERVAL = parser.get('Activity', 'TIME_INTERVAL')
TIME_DELAY = parser.get('Activity', 'TIME_DELAY')

fit = fitbit.Fitbit()

# Try to read existing token pair
try:
    token = json.load(open(tokenfile))

except IOError:
    print "Error retrieving access token. Please rerun provided access_generator.py!"
    auth_url = fit.GetAuthorizationUri()
    print "Please visit the link below and approve the app:\n %s" % auth_url
    # Set the access code that is part of the arguments of the callback URL FitBit redirects to.
    access_code = raw_input("Please enter code (from the URL you were redirected to): ")
    # Use the temporary access code to obtain a more permanent pair of tokens
    token = fit.GetAccessToken(access_code)
    # Save the token to a file
    json.dump(token, open(tokenfile,'w'))

# Create start time and end time for api call
delay = int(TIME_DELAY)
now = dt.datetime.now()
delta = dt.timedelta(minutes=delay)
t = now.time()
end_time = (t.strftime('%H:%M'))

# Subtract 1 minute to start time to provide end time
start_time = ((dt.datetime.combine(dt.date(1, 1, 1), t) + delta).time().strftime('%H:%M'))

# Concatenate API str to include start and end time
api_str = '/1/user/-/activities/distance/date/today/' + DATE_INTERVAL + '/' + TIME_INTERVAL + '/time/' + start_time + '/' + end_time + '.json'

# Get user activity intraday API calls
distance = fit.ApiCall(token, api_str)

distance = json.dumps(distance)

print distance
