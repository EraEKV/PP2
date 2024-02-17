import json

print("Interface Status")
print("=======================================================================================")
print("DN                                                 Description         Speed    MTU  ")
print("-------------------------------------------------- ------------------  ------  -----")

with open("4/sample-data.json", "r") as file:
    data = json.load(file)
    for item in data['imdata']:
        # print(f"{item['l1PhysIf']['attributes']['dn']}                        {item['l1PhysIf']['attributes']['speed']}    {item['l1PhysIf']['attributes']['mtu']}")
        dn = item['l1PhysIf']['attributes']['dn']
        speed = item['l1PhysIf']['attributes']['speed']
        mtu = item['l1PhysIf']['attributes']['mtu']
        print(f"{dn.ljust(70)} {speed.ljust(8)} {mtu}")