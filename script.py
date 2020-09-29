import json
import requests
import time
import platform
import sys

# payload = {'key1': 'value1', 'key2': 'value2'}  
# r = requests.get('https://httpbin.org/get', params=payload)  
# http://httpbin.org/get?key2=value2&key1=value1

def request_site(ip:str):
    ok = False
    r  = requests.get(ip)
    if(r.status_code == requests.codes.ok): ok = True
    else: ok = False
    return ok
    

def main_loop():
    sites = load_data()
    while True:
        try:
            for i in sites:
                try:
                    ok = request_site(i['ip'])
                    i['status'] = ok
                except ConnectionRefusedError:
                    i['status'] = False
            with open("sites.json", "w") as c_data:
                json.dump(sites, c_data)
            time.sleep(60)
        except KeyboardInterrupt:
            # print("You stopped me! Fool!")
            sys.exit(0)
    
def load_data():
    with open("sites.json") as c_data:
        data = c_data.read()
        sites = json.loads(data)
        return sites

def main(argv):
    # platforma = platform.system()
    # if platforma == "Linux":
    # main_loop()
    # elif platforma == "Windows":
    try:
        main_loop()
    except requests.ConnectionError as err:
        print(err)
    

if __name__ == '__main__':
    main(sys.argv)