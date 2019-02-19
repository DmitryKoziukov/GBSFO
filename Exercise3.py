
#Extremely plain example without the OOP practice.
#Just to show you how could it be like


import requests
from requests.auth import HTTPDigestAuth

#url = "https://some_site_with_a_post_request_for_login"
url = "https://google.com"
headers = {'user-agent': 'my-app/0.0.1'}
user = "any"
passw = "any"


def API_login():
    res=''
    response = requests.post(url, headers = headers, auth=HTTPDigestAuth(user, passw))
    print response.status_code
    if (response.status_code!=200):
        print "TEST FAILED"
    else: print "TEST PASSED"
    try:
        res = response.json()
    except:
        res = response.text
    finally:
        print res

API_login()
