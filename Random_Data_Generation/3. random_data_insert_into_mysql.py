import os
import time
from prometheus_client import start_http_server, Gauge, Enum
import requests
import json
import mysql.connector
import pandas as pd
from jproperties import Properties
import datetime

debug= False

configs = Properties()

with open('gyan-core-agent-rand.properties', 'rb') as read_prop:
    configs.load(read_prop)

db_configs_dict = {}
items_view = configs.items()
for item in items_view:
    db_configs_dict[item[0]] = item[1].data


polling_interval_seconds = int(db_configs_dict["POLLING_INTERVAL_SECONDS"])

exporter_port = int(db_configs_dict["APP_PORT"])

host= str(db_configs_dict["db_host"])
db_name = str(db_configs_dict["db_name"])
password = str(db_configs_dict["db_password"])
database = str(db_configs_dict["db_database_name"])
user = str(db_configs_dict["db_user"])

client_name = str(db_configs_dict["client_name"])
column_name = str(db_configs_dict["column_name"])



db_connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)


#load json
if debug == True:
    json_location = str(db_configs_dict["json_location"])
else:
    json_location = str(db_configs_dict["folder_location"]) + str(db_configs_dict["json_location"])


while True:
    cursor = db_connection.cursor()

    # Get timestamp value
    current_timestamp = datetime.datetime.now()
    
    # Get Json Peak upload speed value
    f = open(json_location)
    data = json.load(f)
    peak_upload_speed = data[client_name+column_name]

    # SQL query and values
    MySQL_insert_query = "INSERT INTO core_stats (client_id, stats_timestamp, total_attached_user, total_rejected_user, peak_upload_speed, peak_download_speed, enodeb_shutdown_count,handover_failure_count,bearer_active_user_count,bearer_rejected_user_count,total_users,total_dropped_packets,enodeb_connected_count,enodeb_connection_status) VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s)"

    the_value = (client_name, str(current_timestamp), 0, 0, peak_upload_speed,0,
                0,   0, 0, 0, 0,  0, 0,0)
    
    # Insert Command
    cursor.execute(MySQL_insert_query, the_value)
    # try:
    db_connection.commit()
    time.sleep(120)
    


