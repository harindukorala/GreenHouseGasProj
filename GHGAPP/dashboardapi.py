from flask import (Blueprint, render_template, g, Response, json, request, jsonify, send_file, send_from_directory, url_for) 
import threading
import argparse
import datetime
import imutils
import time
import requests
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize
from GHGAPP.db import get_db


bp = Blueprint('dashboardapi', __name__)

@bp.route('/')
def index():
    return render_template('dashboard.html')

# APIs used for retrieving data from the database via AJAX calls to populate dashboard widgets 

@bp.route('/get_gps_data', methods=['GET', 'POST'])
def get_gps_data():
	db = get_db()	
	cursor = db.cursor()
	sqlcode = """SELECT payload from gps_real_data ORDER BY idgps_real_data DESC LIMIT 1;"""
	try:
		cursor.execute(sqlcode)
	except Exception as err:
		print("Error Message", err.msg)
	result = cursor.fetchone()
	gps_data_dict = json.loads(result[0])
	cursor.close()	
	return gps_data_dict

@bp.route('/get_real_live_gas_data', methods=['GET', 'POST'])
def get_real_live_gas_data():
	db = get_db()
	cursor = db.cursor()
	sqlcode = """SELECT payload from gas_real_data ORDER BY gas_id DESC LIMIT 1;"""
	try:
		cursor.execute(sqlcode)
	except Exception as err:
		print("Error Message", err.msg)
	result = cursor.fetchone()
	print(result[0])
	gas_data_dict = json.loads(result[0])
	cursor.close()
	return jsonify({
		"0" : gas_data_dict["CO"],
		"1" : gas_data_dict["CO2"],
		"2" : gas_data_dict["O2"],
		"3" : gas_data_dict["NCX"],
		"4" : gas_data_dict["CE"],
		"5" : gas_data_dict["HC"],
		"6" : gas_data_dict["Temp"],
		"time_stamp" : gas_data_dict["Timestamp"],
		"flag" : gas_data_dict["flag"],
		})	

@bp.route('/get_real_live_gas_data_for_table', methods=['GET', 'POST'])
def get_real_live_gas_data_for_table():
	db = get_db()
	cursor = db.cursor()
	sqlcode = """SELECT payload from gas_real_data ORDER BY timestamp DESC LIMIT 100;"""
	try:
		cursor.execute(sqlcode)
	except Exception as err:
		print("Error Message", err.msg)
	results = cursor.fetchall()
	payload = []
	for result in results:
		data = json.loads(result[0])
		payload.append(data)
	cursor.close()	
	return jsonify(payload)

@bp.route('/get_obd_real_data_gauges', methods=['GET', 'POST'])
def get_obd_real_data_gauges():
	db = get_db()
	cursor = db.cursor()
	sqlcode = """SELECT payload from obd_real_data ORDER BY obd_auto_id DESC LIMIT 1;"""
	try:
		cursor.execute(sqlcode)
	except Exception as err:
		print("Error Message", err.msg)
	result = cursor.fetchone()
	print(result[0])
	obd_data_dict = json.loads(result[0])
	cursor.close()	
	return obd_data_dict

# API for generating excel files for the 

@bp.route("/get_obd_data_excel")
def get_obd_data_excel():
	db = get_db()
	cursor = db.cursor()
	sqlcode = """SELECT payload from obd_real_data"""
	try:
		cursor.execute(sqlcode)
	except Exception as err:
		print("Error Message", err.msg)

	results = cursor.fetchall()
	payload = []
	for result in results:
		data = json.loads(result[0])
		payload.append(data)
	df_json = pd.json_normalize(payload)
	df_json.to_excel('Downloads/get_obd_data_excel.xlsx')
	cursor.close()
	try:
		return send_file('Downloads/get_obd_data_excel.xlsx', mimetype='application/vnd.ms-excel', attachment_filename='get_obd_data_excel.xlsx', as_attachment=True)
	except Exception as e:
		return str(e)

@bp.route("/get_gps_data_excel")
def get_gps_data_excel():
	db = get_db()
	cursor = db.cursor()
	sqlcode = """SELECT payload from gps_real_data"""
	try:
		cursor.execute(sqlcode)
	except Exception as err:
		print("Error Message", err.msg)
	
	results = cursor.fetchall()
	payload = []
	for result in results:
		data = json.loads(result[0])
		payload.append(data)
	df_json = pd.json_normalize(payload)
	df_json.to_excel('Downloads/get_gps_data_excel.xlsx')
	cursor.close()
	try:
		return send_file('Downloads/get_gps_data_excel.xlsx', mimetype='application/vnd.ms-excel', attachment_filename='get_gps_data_excel.xlsx', as_attachment=True)
	except Exception as e:
		return str(e)

@bp.route("/get_real_gas_data_excel")
def get_real_gas_data_excel():
	db = get_db()
	cursor = db.cursor()
	sqlcode = """SELECT payload from gas_real_data"""
	try:
		cursor.execute(sqlcode)
	except Exception as err:
		print("Error Message", err.msg)
	results = cursor.fetchall()
	payload = []
	for result in results:
		data = json.loads(result[0])
		payload.append(data)
	df_json = pd.json_normalize(payload)
	df_json.to_excel('Downloads/get_gas_data_excel.xlsx')
	cursor.close()
	try:
		return send_file('Downloads/get_gas_data_excel.xlsx', mimetype='application/vnd.ms-excel', attachment_filename='get_gas_data_excel.xlsx', as_attachment=True)
	except Exception as e:
		return str(e)

# APIs for saving data received from OBD device, GPS and Gas Analyser

@bp.route('/api/save_obd', methods=['GET', 'POST'])
def save_obd_data():
	content = request.json # Retrieve data in json format
	dic_content = json.loads(content) #parse the JSON string to python dictonary . The main reason behind this is to retrieve the timestamp
	timestamp = dic_content['Timestamp']
	dataJson = json.dumps(dic_content) #Convert the dictionary to a json string
	db = get_db()
	cursor = db.cursor()
	sqlcode = """INSERT INTO obd_real_data (timestamp,payload) VALUES (%s, %s)"""
	insertvalues = (timestamp, dataJson)
	try:
		cursor.execute(sqlcode,insertvalues)
		db.commit()
	except Exception as err:
		print("Error Message", err.msg)
	print(cursor.rowcount, "was inserted.")
	cursor.close()
	return "Successfully entered"

@bp.route('/api/save_gps_data', methods=['GET', 'POST'])
def save_gps_data():
	content = request.json
	dic_content = json.loads(content)
	timestamp = dic_content['Timestamp']
	dataJson = json.dumps(dic_content)
	db = get_db()
	cursor = db.cursor()
	sqlcode = """INSERT INTO gps_real_data (timestamp,payload) VALUES (%s, %s)"""
	insertvalues = (timestamp, dataJson)
	try:
		cursor.execute(sqlcode,insertvalues)
		db.commit()
	except Exception as err:
		print("Error Message", err.msg)
	print(cursor.rowcount, "was inserted.")
	cursor.close()
	return "Successfully entered"

@bp.route('/api/save_gas_data', methods=['GET', 'POST'])
def save_gas_data():
	content = request.json
	dic_content = json.loads(content)
	timestamp = dic_content['Timestamp']
	dataJson = json.dumps(dic_content)
	db = get_db()
	cursor = db.cursor()
	sqlcode = """INSERT INTO gas_real_data (timestamp,payload) VALUES (%s, %s)"""
	insertvalues = (timestamp, dataJson)
	try:
		cursor.execute(sqlcode,insertvalues)
		db.commit()
	except Exception as err:
		print("Error Message", err.msg)
	print(cursor.rowcount, "was inserted.")
	cursor.close()
	return "Successfully entered"
