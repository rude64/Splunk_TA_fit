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

# Get user activity API calls
calories = fit.ApiCall(token, '/1/user/-/activities/log/calories/date/today/1d.json')
steps = fit.ApiCall(token, '/1/user/-/activities/log/steps/date/today/1d.json')
minutesSedentary = fit.ApiCall(token, '/1/user/-/activities/log/minutesSedentary/date/today/1d.json')

calories = json.dumps(calories['activities-log-calories'])
steps = json.dumps(steps['activities-log-steps'])
minutesSedentary = json.dumps(minutesSedentary['activities-log-minutesSedentary'])

# Send to stdout for Splunk to consume in inputs.conf
print '{"activities-log-calories": %s}' % calories

print '{"activities-log-steps": %s}' % steps
print '{"activities-log-minutesSedentary": %s}' % minutesSedentary
