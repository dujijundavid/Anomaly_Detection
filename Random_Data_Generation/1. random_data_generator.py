from jproperties import Properties
import random
import json
import time


configs = Properties()
debug= True
if debug == True:
    with open('gyan-core-agent-rand.properties', 'rb') as read_prop:
        configs.load(read_prop)
else:
    with open('/opt/gyan/core/gyan-core-agent-rand/gyan-core-agent-rand.properties', 'rb') as read_prop:
        configs.load(read_prop)

db_configs_dict = {}
items_view = configs.items()

for item in items_view:
    db_configs_dict[item[0]] = item[1].data



column_name = db_configs_dict["column_name"].split(",")[0] 
min_val = int(db_configs_dict[column_name +".min"])
max_val = int(db_configs_dict[column_name +".max"])


while True:
    
    agent = db_configs_dict["agent"]
    if agent == "agent1":   # Regular Value
        rand_value = random.randint(min_val,max_val)

    elif agent=="agent2" or agent=="agent3":    # Upper Anomaly
        rand_value = random.randint(max_val,max_val*float(db_configs_dict[agent+".deviation"]))

    elif agent=="agent4" or agent=="agent5":    # Lower Anomaly
        rand_value = random.randint(min_val*float(db_configs_dict[agent+".deviation"]),min_val)


    data= {"RAND001_1_"+column_name: rand_value}

    print(agent)
    print(data)


    jsonFilePath= "gyan_core_agent_rand.json" 
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
    
    time.sleep(120)
    