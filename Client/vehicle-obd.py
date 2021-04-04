import obd
import time
from datetime import datetime
import json
import pandas as pd 
import csv
import requests
import json

# simple datetime converter to convert datetime object to string . This was used to overcome "datetime.datetime not JSON serializable" error
def dateConverter(item):
    if isinstance(item, datetime):
        return item.__str__()

def writeToCSV(data_dic):
    keys = data_dic.keys()
    dict_writer = csv.DictWriter(filename, keys)
    dict_writer.writerow(data_dic)
    
def finalpreProcessingAndRestAPICall(r):
    dic_entry.update({'{}'.format(r.command):'{}'.format(r.value)})
    dic_entry.update({'Timestamp' : datetime.now()})
    dataJson = json.dumps(dic_entry, default=dateConverter)
    writeToCSV(dic_entry)
    dic_entry.clear()
    try:
        res = requests.post('http://136.186.108.101:80/api/save_obd', json=dataJson, timeout=1)
    except:
        pass

def preProcessDataOBDParameter(r):
    dic_entry.update({'{}'.format(r.command):'{}'.format(r.value)})


# initialize dictionary 
dic_entry={}
dt = datetime.now()

connection = obd.Async(portstr='COM8') # auto-connects to com port

filename = open('{}-{}-{}-{}-{}{}.csv'.format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second), 'wb')

writer = csv.writer(filename)


connection.watch(obd.commands.SPEED, callback=finalpreProcessingAndRestAPICall)
connection.watch(obd.commands.RPM, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.TIMING_ADVANCE, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.INTAKE_TEMP, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.MAF, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.THROTTLE_POS, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.AIR_STATUS, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_SENSORS, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_B1S1, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_B1S2, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_B1S3, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_B1S4, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_B2S1, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_B2S2, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_B2S3, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_B2S4, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.OBD_COMPLIANCE, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_SENSORS_ALT, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.AUX_INPUT_STATUS, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.RUN_TIME, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.PIDS_B, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.DISTANCE_W_MIL, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.FUEL_RAIL_PRESSURE_VAC, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.FUEL_RAIL_PRESSURE_DIRECT, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_S1_WR_VOLTAGE, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_S2_WR_VOLTAGE, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_S3_WR_VOLTAGE, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_S4_WR_VOLTAGE, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_S5_WR_VOLTAGE, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_S6_WR_VOLTAGE, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_S7_WR_VOLTAGE, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_S8_WR_VOLTAGE, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.COMMANDED_EGR, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.EGR_ERROR, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.EVAPORATIVE_PURGE, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.FUEL_LEVEL, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.WARMUPS_SINCE_DTC_CLEAR, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.DISTANCE_SINCE_DTC_CLEAR, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.EVAP_VAPOR_PRESSURE, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.BAROMETRIC_PRESSURE, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_S1_WR_CURRENT, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_S2_WR_CURRENT, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_S3_WR_CURRENT, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_S4_WR_CURRENT, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_S5_WR_CURRENT, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_S6_WR_CURRENT, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_S7_WR_CURRENT, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.O2_S8_WR_CURRENT, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.CATALYST_TEMP_B1S1, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.CATALYST_TEMP_B2S1, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.CATALYST_TEMP_B1S2, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.CATALYST_TEMP_B2S2, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.PIDS_C, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.STATUS_DRIVE_CYCLE, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.CONTROL_MODULE_VOLTAGE, callback=npreProcessDataOBDParameterewV)
connection.watch(obd.commands.ABSOLUTE_LOAD, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.COMMANDED_EQUIV_RATIO, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.RELATIVE_THROTTLE_POS, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.AMBIANT_AIR_TEMP, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.THROTTLE_POS_B, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.THROTTLE_POS_C, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.ACCELERATOR_POS_D, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.ACCELERATOR_POS_E, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.ACCELERATOR_POS_F, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.THROTTLE_ACTUATOR, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.RUN_TIME_MIL, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.TIME_SINCE_DTC_CLEARED, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.MAX_MAF, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.FUEL_TYPE, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.ETHANOL_PERCENT, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.EVAP_VAPOR_PRESSURE_ABS, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.EVAP_VAPOR_PRESSURE_ALT, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.SHORT_O2_TRIM_B1, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.LONG_O2_TRIM_B1, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.SHORT_O2_TRIM_B2, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.LONG_O2_TRIM_B2, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.FUEL_RAIL_PRESSURE_ABS, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.RELATIVE_ACCEL_POS, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.HYBRID_BATTERY_REMAINING, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.OIL_TEMP, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.FUEL_INJECT_TIMING, callback=preProcessDataOBDParameter)
connection.watch(obd.commands.FUEL_RATE, callback=preProcessDataOBDParameter)
    

connection.start() # start the async update loop

while True:
    pass
connection.stop()
filename.close()