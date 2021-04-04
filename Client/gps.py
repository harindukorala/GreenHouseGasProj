import time
import serial
from datetime import datetime
import json
import requests
import csv

gps_data_dic = {}
header = ['Timestamp', 'Latitude Degree', 'Longitude Degree', 'Speed']
dt = datetime.now()
savefilename = open('{}-{}-{}-{}-{}-{}.csv'.format(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second), 'w', newline='')
writer = csv.writer(savefilename)
writer.writerow(header)

def decodeReadData(line, gps_data_dic):
    stringResponse = str(line)
    GPRMC_Data_List = []
    if("GPRMC" in stringResponse):
        GPRMC_Data_List = stringResponse.split(",")
        gps_data_dic = extractCordinates(GPRMC_Data_List, gps_data_dic)
        if not '' in gps_data_dic.values():
            writeToCSV(gps_data_dic)
            constructJson(gps_data_dic)
        else:
            print("Data is not coming")
        
def extractCordinates(GPRMC_List, gps_data_dic):  
    if (GPRMC_List):
        #3749.1111,S,14502.3289,E,
        latdeg, latmin, latsec = 0,0,0
        londeg, lonmin, lonsec = 0,0,0
        if GPRMC_List[3]:
            latdeg = int(float(GPRMC_List[3])/100.0)
            latmin = float(GPRMC_List[3]) - (float)(latdeg*100.0)
        #convert latmin to int
            latsec = latmin-int(latmin)
            latmin = int(latmin)
            degmin = float(latmin)/ 60 
            degsec = latsec / 3600
            finalLatitude = latdeg + degmin + degsec
            #print(finalLatitude)
            strLatDeg = str(finalLatitude)
        else:
            strLatDeg = ''
        if GPRMC_List[5]:
            londeg = int(float(GPRMC_List[5])/100.0)
            lonmin = float(GPRMC_List[5]) - (float)(londeg*100.0)
            lonsec = lonmin-int(lonmin)
            lonmin = int(lonmin)
            londegmin = float(lonmin)/ 60 
            londegsec = lonsec / 3600
            finalLongtitude = londeg + londegmin + londegsec
            #print(finalLongtitude)
            strLondeg = str(finalLongtitude)
        else:
            strLondeg = ''
        if GPRMC_List[4]:
            lat_direction =  GPRMC_List[4]
        else:
            lat_direction = ''
        if GPRMC_List[6]:
            long_direction = GPRMC_List[6]
        else:
            long_direction = ''
        if GPRMC_List[7]:
            speed = float(GPRMC_List[7]) * 1.852000
        else:
            speed = ''
        if ("S" in lat_direction):
            strLatDeg = '-' + strLatDeg
        if ("W" in long_direction):
            strLondeg = '-' + strLondeg
        gps_data_dic.update({'Latitude Degree' : strLatDeg })
        gps_data_dic.update({'Longitude Degree' : strLondeg })
        gps_data_dic.update({'Speed' : speed})
    return gps_data_dic

def constructJsonAndRestAPICall(gps_data_dic):
    dataJson = json.dumps(gps_data_dic, default = dateConverter)
    try:
        res = requests.post('http://136.186.108.101:80/api/save_gps_data', json=dataJson, timeout=1)
    except:
        pass

def writeToCSV(gps_data_dic):
    keys = gps_data_dic.keys()
    dict_writer = csv.DictWriter(filename, keys)
    dict_writer.writerow(gps_data_dic)
        
def dateConverter(item):
    if isinstance(item, datetime):
        return item.__str__()

try:
  gps = serial.Serial('COM5', 4800)
except:
  print("Failed to connect")
  exit()
# Read data and print it to terminal... until you stop the program

while 1:
    gps_data_dic.clear()
    timestamp = datetime.now()
    gps_data_dic.update({'Timestamp' : timestamp })
    line = gps.readline()
    decodeReadData(line, gps_data_dic)
gps.close()
savefilename.close()