import json
import requests

_gb = input("Enter GB (.i.g: 5): ")

def get_id():
    return input("Enter your ID (.i.g: ...f669f7844994): ")

_id = get_id()

while (len(_id) != 36):
    print("Err: Invalid ID!!")
    _id = get_id()

def handle():
    return requests.post("https://api.cloudflareclient.com/v0a745/reg", data=json.dumps({"referrer": _id}))

for i in range(int(_gb)):
    _res = handle()
    _json_res = _res.json()
    if _res.status_code == 200 and _json_res.get('account'):
        print("You got {}GB data!!".format(i+1))
    else:
        print("Error! Something wrong!!")
        for r in range(2):
            _res = handle()
            _json_res = _res.json()
            if _res.status_code == 200 and _json_res.get('account'):
                print("You got 1GB more data!")
                break
            else:
                print("Retry error!! \nexit!")
                exit()