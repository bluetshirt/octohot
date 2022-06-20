import requests 

url = "https://192.168.68.246/api/printer/command"
key = "114973FEFB8947EC82240ED6CEC09162"

'''use octoprint api to preheat bed and nozzle'''
def preheat_printer():
    headers = {"X-Api_Key": key}
    params = {"commands" : ["M140 S60", "M104 S210"]}
    x = requests.post(url, json=params, headers=headers, verify=False)
    print(x) 

preheat_printer()