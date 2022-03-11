import time
import json
import random


def random_data_BETBELPDENB():
    rand_data = {
        "BETBELPDENB001_1_ConnEstabFailSum": 0,
        "BETBELPDENB001_1_ConnEstabSuccSum": random.randint(10, 100),
        "BETBELPDENB001_2_ConnEstabFailSum": 0,
        "BETBELPDENB001_2_ConnEstabSuccSum": random.randint(10, 100),
        # BETBELPDENB_1 and BETBELPDENB_2
        # BETBELLBENB_
        # OnGoRadio
        # BSName_CellNUMBER pair
        # Seperate into 5 or 3
        # 3 files  dump into same json
        # 1 file or 3 files has no difference

        "BETBELPDENB001_1_TotalCellUnavailableTimeFault": 0,
        "BETBELPDENB001_1_TotalCellUnavailableTimeManualIntervention": 0,
        "BETBELPDENB001_1_TotalCellUnavailableTime": 0,
        "BETBELPDENB001_2_TotalCellUnavailableTimeFault": 0,
        "BETBELPDENB001_2_TotalCellUnavailableTimeManualIntervention": 0,
        "BETBELPDENB001_2_TotalCellUnavailableTime": 0,
        "BETBELPDENB001_1_DrbULThCapacitySum": random.randint(1000000, 10000000),
        "BETBELPDENB001_1_DrbPdcpSduAirLossRateDlSum": 0,
        "BETBELPDENB001_1_DrbMaxULThCapacity": random.randint(30000, 42000),
        "BETBELPDENB001_1_DrbPdcpSduLossRateUlSum": 0,
        "BETBELPDENB001_1_DrbDLThCapacitySum": random.randint(1000000, 10000000),
        "BETBELPDENB001_1_DrbULThCapacityAvg": random.randint(20000, 25000),
        "BETBELPDENB001_1_DrbDLThCapacityAvg": random.randint(20000, 22000),
        "BETBELPDENB001_2_DrbULThCapacitySum": random.randint(1000000, 10000000),
        "BETBELPDENB001_2_DrbPdcpSduAirLossRateDlSum": 0,
        "BETBELPDENB001_2_DrbMaxULThCapacity": random.randint(35000, 40000),
        "BETBELPDENB001_2_DrbPdcpSduLossRateUlSum": 0,
        "BETBELPDENB001_2_DrbDLThCapacitySum": random.randint(1000000, 10000000),
        "BETBELPDENB001_2_DrbULThCapacityAvg": random.randint(20000, 22000),
        "BETBELPDENB001_2_DrbDLThCapacityAvg": random.randint(20000, 22000),
        "BETBELPDENB001_1_RbDlIpLatency": 0,
        "BETBELPDENB001_1_PdcpSduAirLossDl": 0,
        "BETBELPDENB001_1_PdcpSduDropRateDl": 0,
        "BETBELPDENB001_1_PdcpTrafficUlKbps": 0,
        "BETBELPDENB001_1_IpLateSamplesDl": 0,
        "BETBELPDENB001_1_PdcpSduAirTotalDl": 0,
        "BETBELPDENB001_1_PdcpSduAirLossRateDl": 0,
        "BETBELPDENB001_1_PdcpTrafficDlKbps": 0,
        "BETBELPDENB001_2_RbDlIpLatency": 0,
        "BETBELPDENB001_2_PdcpSduAirLossDl": 0,
        "BETBELPDENB001_2_PdcpSduDropRateDl": 0,
        "BETBELPDENB001_2_PdcpTrafficUlKbps": 0,
        "BETBELPDENB001_2_IpLateSamplesDl": 0,
        "BETBELPDENB001_2_PdcpSduAirTotalDl": 0,
        "BETBELPDENB001_2_PdcpSduAirLossRateDl": 0,
        "BETBELPDENB001_2_PdcpTrafficDlKbps": 0}

    return rand_data


# Reading the json as a dict
with open('C:\\Users\\Jijun Du\\Desktop\\Jupyter Notebook\\Gyan\\gyan-report.json') as json_data:
    data = json.load(json_data)



while True:
    
    rand_data = random_data_BETBELPDENB()
    # Reading the json as a dict
    
    data.update(rand_data)
    
    # Directly from dictionary
    with open('gyan-report.json', 'w') as outfile:
        json.dump(data, outfile)
    time.sleep(1)
    #print("Complete")

  