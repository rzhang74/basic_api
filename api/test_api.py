import requests, json

base = 'http://localhost:8000/'
header = {'Content-Type': 'application/json'}
# 'Authorization': 'Token xxxxxx'

def test_register(uname, password, fname, lname, email):
    payload = {'username': uname, 'password': password, 'first_name': fname, \
               'last_name': lname, 'email': email}
    r = requests.post(base + 'register', data=json.dumps(payload), headers=header)
    return r

def test_login(uname, passwd):
    payload = {'username': uname, 'password': passwd}
    r = requests.post(base + 'login', data=json.dumps(payload), headers=header)
    return r #r.json, remember the token. it is auth

def test_logout(auth):
    header['Authorization'] = 'Token ' + auth
    r = requests.post(base + 'logout', headers = header)
    return r