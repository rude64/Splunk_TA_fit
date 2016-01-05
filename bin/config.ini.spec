############## Config.ini.spec ##############
# Sample config.ini for testing purposes
# Will be deprecated and replaced by Splunk
# GUI interface in official release
#############################################
# Replace with your OAuth2 information from
# https://dev.fitbit.com
#############################################

[Login Parameters] 
C_KEY=ABC123                            # Fitbit App OAuth2 Client Key
C_SECRET=abc1234abc1234abc1234abc1234   # Fitbit App Client Secret
REDIRECT_URI=http://127.0.0.1:8080      # Fitbit App redirect URL

[Activity]
DATE_INTERVAL = 1d      # 1d is currently the only accepted response
TIME_INTERVAL = 15min   # 1min or 15min
TIME_DELAY = -15        # Always -(minus). Expressed in x number of minutes

[Heart]
DATE_INTERVAL = 1d      # 1d is currently the only accepted response
TIME_INTERVAL = 1min    # 1sec or 1min
TIME_DELAY = -5         # Always -(minus). Expressed in x number of minutes
