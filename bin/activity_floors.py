import os, fitbit, json
# import requests.packages.urllib3
# requests.packages.urllib3.disable_warnings()

# Setup Splunk Environment
APPNAME = 'Splunk_TA_fit'
CONFIG = '/bin/user_settings.txt'
SPLUNK_HOME = os.environ['SPLUNK_HOME']

tokenfile = SPLUNK_HOME + '/etc/apps/' + APPNAME + CONFIG

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

# Get user activity intraday API calls
floors = fit.ApiCall(token, '/1/user/-/activities/floors/date/today/1d/15min.json')

floors = json.dumps(floors)

print floors
