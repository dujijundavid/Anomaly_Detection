import json
import sys
# generate random integer values
import random

data = {
    "BETAZRPDCOR001_1_totalAttachedUser": random.randint(1,10),
    "BETAZRPDCOR001_1_totalRejectedUser": 0,
    "BETAZRPDCOR001_1_totalBearerActiveUser": random.randint(3000,10000),
    "BETAZRPDCOR001_1_totalBearerRejectedUser": 0,
    "BETAZRPDCOR001_1_handoverFailureCount": 0,
    "BETAZRPDCOR001_1_peak_ul": random.randint(10,80),
    "BETAZRPDCOR001_1_peak_dl": random.randint(100,190),
    "BETAZRPDCOR001_1_total_dropped_packets": 0,
    "BETAZRPDCOR001_1_total_users": random.randint(1,25),
    "BETAZRPDCOR001_1_enodeb_connected_count": random.randint(1,4),
    "BETAZRPDCOR001_1_enodeb_shutdown_count": random.randint(1,4),
    "BETAZRPDCOR001_1_enodeb_connection_status": 100}


json_string = json.dumps(data)

f = open(r'/opt/tools/gyan-core-agent-belprod/report/gyan-core-agent-report-belprod.json','w')
sys.stdout = f
print(json_string)
sys.stdout.close()
