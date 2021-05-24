# Chatbot Viber
This chatbot allows teacher and students to control AIX Workload Partitions. 
Also, this chatbot will help students to learn AIX OS.

##### Installation of necessary requirements:

---
`pip3 install -r requirements.txt`

##### Example of secrets.py file:

---
**DB2 integration:** <br/>
database = 'DATABASE=_example_database_name_;' <br/>
hostname = 'HOSTNAME=_example_hostname_;'  # 127.0.0.1 or localhost works if it's local <br/>
port = 'PORT=50001;' <br/>
protocol = 'PROTOCOL=TCPIP;' <br/>
uid = 'UID=_example_user_id_;' <br/>
**IBM Watson Assistant:** <br/>
ibm_password = 'PWD=_example_password_;' <br/>
api_key = "example_api_key_" <br/>
url = "https://api.eu-gb.language-translator.watson.cloud.ibm.com" <br/>
**Email notification settings:** <br/>
email = '_example@email_' <br/>
email_password = '_password_' <br/>
**Moodle credentials:** <br/>
moodle_token = '_moodle_token_' <br/>
moodle_url = 'http://_example_moodle_url_/' <br/>
**LogDNA token:** <br/>
logdna_api_key = '_example_logdna_api_key_' <br/>
**Viber authentication token:** <br/>
viber_auth_token = '_example_viber_key_' <br/>

##### Run application:

---
Please, create _secrets.py file_ before run application.
To run application, please execute or register it as a service: <br/>
`python3 ./script.py`