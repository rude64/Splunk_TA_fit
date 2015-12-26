import fitbit, json
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

tokenfile = "user_settings.txt"

fit = fitbit.Fitbit()

# Try to read existing token pair
try:
    token = json.load(open(tokenfile))
except IOError:
    # If not generate a new file
    # Get the authorization URL for user to complete in browser.
    auth_url = fit.GetAuthorizationUri()
    print "Please visit the link below and approve the app:\n %s" % auth_url
    # Set the access code that is part of the arguments of the callback URL FitBit redirects to.
    access_code = raw_input("Please enter code (from the URL you were redirected to): ")
    # Use the temporary access code to obtain a more permanent pair of tokens
    token = fit.GetAccessToken(access_code)
    # Save the token to a file
    json.dump(token, open(tokenfile,'w'))

# Sample API call
response = fit.ApiCall(token, '/1/user/-/profile.json')

# Token is part of the response. Note that the token pair can change when a refresh is necessary.
# So we replace the current token with the response one and save it.
token = response['token']
json.dump(token, open(tokenfile,'w'))

# Do something with the response
print "Welcome %s, your Fitbit account is now connected!" % response['user']['displayName']
