# Green House Gas Project

This repository contains the codebase for Green House Gas Python Flask Web Application and python code files used to collect data from IoT sensors.

## The main objective of the Green House Gas Project 

Emissions reporting and sustainability are increasingly important to Australian business. Managing the collection and analysis of Green House Gas emission data from domestic goods and services delivery is a complex and diverse challenge. 

The main objective of this green house gas project is to develop a complete end-to-end IoT solution for collecting, pre-processing, storing and visualising green house gas emission data from delivery trucks and related other sensor data (i.e., GPS data, OBD vehicle data etc.). Then analyse the collected data to determine possible correlations between green house gas data and other related sensor data (e.g., RPM of vehicle and CO emission etc.). 

## Overview of the Green House Gas IoT solution

In this solution, we are collecting sensor data from four IoT sensors. They are 
-Gas Analyser sensor: Gas emission data 
-OBD sensor : Vehicle On Board Diagnostic data
-GPS sensor : GPS data
-Dashcam : Video data

We have connected the above sensors to a Raspbery Pi 4 via serial and bluetooth(OBD sensor) communication links. Python Client application deployed in the Raspbery Pi is responsible for collecting, pre-processing and locally storing sensor data. Furthermore, it transmits sensor data to a database hosted in a cloud server via REST API calls.

We have developed a Python Flask Web Application and hosted it in a cloud server. The APIs in the flask appliction are used to :
-Store sensor data into the database
-Retreive data from database and load into widgets of the dashboard that visualise real time sensor data. 

Below diagram illustrates the architecture of the solution



## Python Flask Web Application 

### Required packages. 

-Python 3.X (Tested with 3.7)
-Flask


