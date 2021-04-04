# Green House Gas Project

This repository contains the codebase for Green House Gas Python Flask Web Application and python code files used to collect data from IoT sensors.

## Overview of the Green House Gas Project 

Emissions reporting and sustainability are increasingly important to Australian business. Managing the collection and analysis of Green House Gas emission data from domestic goods and services delivery is a complex and diverse challenge. 

The main objective of this green house gas project is to develop a complete end-to-end IoT solution for collecting, pre-processing, storing and visualising green house gas emission data from delivery trucks and related other sensor data (i.e., GPS data, OBD vehicle data etc.). Then analyse the collected data to determine possible correlations between green house gas data and other related sensor data (e.g., RPM of vehicle and CO emission etc.). 

## Overview of the Green House Gas IoT solution

In this solution, we are collecting sensor data from four IoT sensors. They are 
- Gas Analyser sensor: Gas emission data 
- OBD sensor : Vehicle On Board Diagnostic data
- GPS sensor : GPS data
- Dashcam : Video data

We have connected the above sensors to a Raspbery Pi 4 via serial and bluetooth(OBD sensor) communication links. Python Client application deployed in the Raspbery Pi is responsible for collecting, pre-processing and locally storing sensor data. Furthermore, it transmits sensor data to a database hosted in a cloud server via REST API calls.

We have developed a Python Flask Web Application and hosted it in a cloud server. The APIs in the flask appliction are used to :
- Store sensor data into the database
- Retreive data from database and load into widgets of the dashboard that visualise real time sensor data. 

Below diagram illustrates the architecture of the solution

![green hous gas data collection and visulaization system](https://user-images.githubusercontent.com/4996419/113511100-81823700-95a1-11eb-92b8-7ca495b9e76f.png)

## Python Flask Web Application 

### Required packages. 

- Python 3.X (Tested with 3.7)
- Flask
- Pandas
- Numpy
- mysql.connector

## Python Client Sensor Data Collection codes

### Required packages. 

- Python 3.X
- pyserial
- opencv-python
- numpy
- vidgear (https://github.com/abhiTronix/vidgear)
- requests
- pandas
- obd (https://pypi.org/project/obd/)

## Explanation for codebase

1. Client : Data Collection , Data Pre processing and Local data storage and REST API communication 
  - Script to collect, pre-process, local storage and REST API communication of gas sensor data :  Client/gas-analyser.py
  - Script to collect, pre-process, local storage and REST API communication of gps sensor data :  Client/gps.py
  - Script to collect, pre-process, local storage and REST API communication of OBD sensor data :  Client/vehicel-obd.py
  - Script to collect, pre-process and local storage of dashcam video data : Client/simple-video-client.py
2. GHGAPP : Flask App
  - API code : GHGAPP/dashboardapi.py 
  - HTML view : GHGAPP/templates/dashboard.html
  - Other static files such as style, javascript : GHGAPP/static



