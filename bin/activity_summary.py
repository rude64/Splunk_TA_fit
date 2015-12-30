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

# Get user activity API calls
# calories = fit.ApiCall(token, '/1/user/-/activities/log/calories/date/today/1d.json')
# steps = fit.ApiCall(token, '/1/user/-/activities/log/steps/date/today/1d.json')
# minutesSedentary = fit.ApiCall(token, '/1/user/-/activities/log/minutesSedentary/date/today/1d.json')
# elevation = fit.ApiCall(token, '/1/user/-/activities/log/elevation/date/today/1d.json')
# distance = fit.ApiCall(token, '/1/user/-/activities/log/distance/date/today/1d.json')
# floors = fit.ApiCall(token, '/1/user/-/activities/log/floors/date/today/1d.json')

summary = fit.ApiCall(token, '/1/user/-/activities/date/today.json')

# Generate JSON data dump
# calories = json.dumps(calories['activities-log-calories'])
# steps = json.dumps(steps['activities-log-steps'])
# minutesSedentary = json.dumps(minutesSedentary['activities-log-minutesSedentary'])
# elevation = json.dumps(elevation['activities-log-elevation'])
# distance = json.dumps(distance['activities-log-distance'])
# floors = json.dumps(floors['activities-log-floors'])

summary = json.dumps(summary)

# Send to stdout for Splunk to consume in inputs.conf
# print '{"activities-log-calories": %s}' % calories
# print '{"activities-log-elevation": %s}' % elevation
# print '{"activities-log-steps": %s}' % steps
# print '{"activities-log-distance": %s}' % distance
# print '{"activities-log-floors": %s}' % floors
# print '{"activities-log-minutesSedentary": %s}' % minutesSedentary

print summary
