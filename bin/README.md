### Initial Configuration Instructions ###

Currently there are two separate items to configure prior to accessing the Fitbit API data. The first configuration item will be deprecated upon the final release and replaced with a Splunk GUI based setup screen. The second installation step is not currently being replaced by a GUI at this time.

---

1. ##### Config.ini: #####
- Create a __config.ini__ file in the _$SPLUNK_HOME/etc/apps/Splunk_TA_fit/bin_ folder. This file will hold the necessary Fitbit application information to log your OAuth2 data. A sample has been provided in the config.ini.spec file. You will need to create an application at [https://dev.fitbit.com](https://dev.fitbit.com) to obtain the necessary information if you have not already done so. Please ensure that you use the OAuth2 client key, and not the OAuth1 version key, as OAuth1 access will be removed from the Fitbit API in 2016.

2. ##### Create Access Token: #####
- Run the __access_generator.py__ from your terminal or command line located in the _$SPLUNK_HOME/etc/apps/Splunk_TA_fit/bin_ folder. This file creates the necessary access tokens and permissions in order for the Technology Addon to consume user data.