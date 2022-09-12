
"""Application exporter"""
import pandas as pd
import time
from prometheus_client import start_http_server, Gauge, Enum
import json
from jproperties import Properties
class AppMetrics:

    
    """
    Representation of Prometheus metrics and loop to fetch and transform
    application metrics into Prometheus metrics.
    """

    def __init__(self, app_port=80, polling_interval_seconds=5):
        self.app_port = app_port
        self.polling_interval_seconds = polling_interval_seconds
        self.gauge_dic={}
        # Prometheus metrics to collect


    def run_metrics_loop(self,json_str):
        """Metrics fetching loop"""

        while True:
            self.fetch(json_str)
            time.sleep(self.polling_interval_seconds)

    def fetch(self,json_str):
        """
        Get metrics from application and refresh Prometheus metrics with
        new values.
        """
        with open(json_str,"r") as json_file:
            status_data = json.load(json_file)
        
        # Update Prometheus metrics with application metrics
        for key,value in status_data.items():
            if key not in self.gauge_dic:
                self.gauge_dic[key] = Gauge(key,key)
                self.gauge_dic[key].set(value)
        
        print("Fetch Complete")


def main():
    """Main entry point"""


    
    configs = Properties()
    debug= False
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

    
    # get variable name from property files.
    client_id = db_configs_dict["client_name"].split(",")[0] 
    polling_interval_seconds = int(db_configs_dict["POLLING_INTERVAL_SECONDS"])
    app_port = int(db_configs_dict["APP_PORT"])
    exporter_port = int(db_configs_dict[client_id+"_EXPORTER_PORT"])
    folder_location = str(db_configs_dict["folder_location"])
    json_location = str(db_configs_dict["json_location"])


    app_metrics = AppMetrics(
        app_port=app_port,
        polling_interval_seconds=polling_interval_seconds
    )
    start_http_server(exporter_port)

    
    if debug:
        json_str = json_location
        app_metrics.run_metrics_loop(json_str)
    else:
        json_str = folder_location+json_location
        app_metrics.run_metrics_loop(json_str)
    
while True:
    main()
    time.sleep(120)
