import requests
import json

def insert(username,note):
    data = {"username":username, "note":note}
    json_data = json.dumps(data)
    res = requests.post("http://127.0.0.1:8000/create/", data=json_data)
    print(res.status_code)
    print(res.json())

insert("jitu","hey there i am jitu...")