## Scripted Inputs for Fitbit Technology Addon

Configuration and installation manual for Splunk_TA_fit using the aforementioned fitbit devices. The scripted inputs provided should provide all the necessary data to ingest your trackers health data into Splunk.

## Files
- fitbit.py - Python class for handling data and token requests
- access_generator.py - Command line utility for gaining initial access to your Fitbit account data
- config.ini.spec - Spec file for showing example config.ini with comments
- requests-2.0.0-py2.7.egg - Egg file for requests. Prevents install of requests in your Splunk Environment
- *&lt;endpoint type&gt;*.py - Worker files for ingesting different data sources from Fitbit

## Requirements
- Python Requests - Egg file provided
- CherryPy - Egg file to be provided at later date

## Installation Instructions

### Preparation
Prior to installation of this TA to your Splunk Indexer(s). You should create and configure the config.ini file. This file will be replaced with a GUI based settings screen in Splunk, but will remain as a config.ini for now.


#### __Config.ini:__
1. Untar, or unzip, the downloaded file to a local location on your system.
2. Create a __config.ini__ file in the _bin_ folder. This file will hold the necessary Fitbit application information to log your OAuth2 data. A sample has been provided in the config.ini.spec file. You will need to create an application at [https://dev.fitbit.com](https://dev.fitbit.com) with a __Private__ application type to obtain the necessary information if you have not already done so. Please ensure that you use the OAuth2 client key, and not the OAuth1 version key, as OAuth1 access will be removed from the Fitbit API in 2016. Here is more information about the config.ini settings:
  - Login Parameters/C_KEY - Your OAuth2 Client Key information, such as ABC123
  - Login Parameters/C_SECRET - Your OAuth2 Client Secret Key information, such as abc1234abc1234abc1234abc1234
  - Login Parameters/REDIRECT_URI - Your OAuth2 Redirect URI, ex. http://127.0.0.1:8080. Please note that the URI must match your Fitbit app, to include trailing slashes if any.
  - *&lt;endpoint type&gt;*/DATE_INTERVAL - Number of days to include in results from specified endpoint. Default is 1d.
  - *&lt;endpoint type&gt;*/TIME_INTERVAL - Number of seconds or minutes to include in results from specified endpoint. Default is based on endpoint type. See config.ini.spec for more information.
  - *&lt;endpoint type&gt;*/TIME_DELAY - Number of minutes to subtract in results from specified endpoint. This will decrease the amount of Splunk license usage and prevent duplicate results from being processed in the Splunk Fit app. If you are unsure of the number of minutes to use, you should add the number of minutes from your inputs.conf interval. Default is based on endpoint type. See config.ini.spec for more information.
3. Tar or zip all the files back into their original format, keeping your __config.ini__ file in the _bin_ directory

### Install the TA in Splunk
Install the TA on your Splunk indexers via any Splunk provided means. Install from file is preferred, however any installation procedure can be followed. If you are unfamiliar with Splunk app installation see the following [Splunk Answers Post](https://answers.splunk.com/answers/51894/how-to-install-a-splunk-app.html). Then restart Splunk in order to continue installation.

#### Create Access Token:
Run the __access_generator.py__ from your terminal or command line located in the _$SPLUNK_HOME/etc/apps/Splunk_TA_fit/bin_ folder. This file creates the necessary access tokens and permissions in order for the Technology Addon to consume user data. This utility requires that you have already configured the __config.ini__ file within your environment. Run the following commands in your terminal:

    cd bin/
    chmod +x access_generator.py
    python access_generator.py

1. The __access_generator__ will provide a browser window with a code. Copy this code to your clipboard. See screenshot:
![Access Generator Code](/../master/static/CodeRef.png?raw=true "Access Generator Code")

2. At the prompt in the __access_generator__ utility, paste the code that you copied from the previous step:
![Access Generator Prompt](/../master/static/RunAccessGen.png?raw=true "Access Generator Prompt")

3. Once the code has been submitted then you should see the screenshot below:
![Access Generator Complete](/../master/static/Complete.png?raw=true "Access Generator Complete")

When the process above has been completed, you should see a file called __user_settings.txt__ has been created in the _$SPLUNK_HOME/etc/apps/Splunk_TA_fit/bin_ directory. This file contains all the required access and refresh tokens needed to access your Fitbit account information.

### Configure local/inputs.conf
The final installation step is to configure your __inputs.conf__ file that tells Splunk which data to request from your Fitbit account. To configure this, you must first create a __local__ folder in the _$SPLUNK_HOME/etc/apps/Splunk_TA_fit/_ directory. This __local__ directory is where you will make specific changes to your Splunk_TA_fit environment.

A sample __inputs.conf__ file has been provided in the _$SPLUNK_HOME/etc/apps/Splunk_TA_fit/default/_ directory. Please note that the scripts in the default file have been disabled and you will need to turn the _disabled=true_ setting to _false_ in each stanza. Please follow the guidance in the __default/inputs.conf__ file for more information.

Now restart Splunk and you should start receiving data within a few minutes!