import serial
from datetime import datetime
import json
import csv
import requests
import time

def dateConverter(item):
    if isinstance(item, datetime):
        return item.__str__()

def writeToCSV(gas_data_dic):
    keys = gas_data_dic.keys()
    dict_writer = csv.DictWriter(filename, keys)
    dict_writer.writerow(gas_data_dic)

start_time = time.time()
flagreset_time = time.time()
gas_data_dic = {}
header = ['Timestamp', 'Flag','CO', 'HC', 'CO2', 'O2', 'NCX', 'AFR', 'Lambda', 'CE', 'Temp']
dt = datetime.now()
savefilename = open('{}-{}-{}-{}-{}-{}.csv'.format(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second), 'w', newline='')
writer = csv.writer(savefilename)
writer.writerow(header)
flag = True

try:
  ser = serial.Serial('COM10')
except:
  print("Failed to connect")
  exit()

ser.write("!DA1\r".encode()) # enable stream reading
while True:
    if time.time() - start_time > 1800:
        ser.write("!ZRO\r".encode())
        flag = False
        start_time = time.time()
        flagreset_time = time.time()
    if flag is not True and time.time() - flagreset_time > 120:
        flag = True
    line = ser.readline()
    timestamp = datetime.now()
    gas_data_dic.update({'Timestamp' : timestamp })
    if flag:
        gas_data_dic.update({'flag': 1})
    else:
        gas_data_dic.update({'flag': 0})
    
    stringResponse = str(line)
    gas_data_list = stringResponse.split(",")
    if len(gas_data_list) >= 8:
        CO = gas_data_list[1]
        HC = gas_data_list[2]
        CO2 = gas_data_list[3]
        O2 = gas_data_list[4]
        NCX = gas_data_list[5]
        AFR = gas_data_list[6]
        Lambda = gas_data_list[7]
        CE = gas_data_list[8]
        Temp = gas_data_list[9].replace("\\r\\n'","")
        gas_data_dic.update({'CO' : CO })
        gas_data_dic.update({'HC' : HC })
        gas_data_dic.update({'CO2' : CO2 })
        gas_data_dic.update({'O2' : O2 })
        gas_data_dic.update({'NCX' : NCX })
        gas_data_dic.update({'AFR' : AFR })
        gas_data_dic.update({'Lambda' : Lambda })
        gas_data_dic.update({'CE' : CE })
        gas_data_dic.update({'Temp' : Temp })
        dataJson = json.dumps(gas_data_dic, default = dateConverter)
        writeToCSV(gas_data_dic)
        try:
            res = requests.post('http://136.186.108.101:80/api/save_gas_data', json=dataJson, timeout=1)
        except:
            pass
            


