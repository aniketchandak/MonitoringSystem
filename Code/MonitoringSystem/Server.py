from flask import Flask, request, jsonify
import configparser
from Subsystem import Subsystem
from Fan import Fan
from Monitor import Monitor
import logging

subsystems=list()
fans = list()
monitor = Monitor()

config = configparser.ConfigParser()
config.read("configuration.ini")

no_subsystem = int(config['BASIC']['NO_SUBSYSTEM'])
no_fan = int(config['BASIC']['NO_FAN'])
fan_upper_bound = int(config['BOUNDS']['FAN_UPPER_BOUND'])
subsystem_upper_bound = int(config['BOUNDS']['SUBSYSTEM_UPPER_BOUND'])

fan_index = no_fan
subsystem_index = no_subsystem

logging.basicConfig(filename='info.log', level=logging.INFO)
logger = logging.getLogger("monitoring_system")
logger.setLevel(logging.INFO)
filehandle = logging.FileHandler('system.log')
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
filehandle.setFormatter(formatter)
logger.addHandler(filehandle)

logger.info("Sample log")

if fan_upper_bound < no_fan or subsystem_upper_bound<no_subsystem:
    logger.error("Server startup fail: Limit exceeds the upper bound")
    print("System can not start: Check log file")
    exit()
for i in range(no_subsystem):
    subsystem=Subsystem(monitor, i)
    subsystems.append(subsystem)

for i in range(no_fan):
    fan=Fan(monitor, i, 130)
    fans.append(fan)

app=Flask(__name__)


@app.route('/fan',methods=['GET','POST','PUT'])
def fan_operations():
    content=request.json 
    if request.method == 'PUT':
        index = content['index']
        max_speed = content['max_speed']
        fans[index].set_max_rpm(max_speed)
        return 'Fan Speed Updated'

    if request.method == 'GET':
        return jsonify([f.serialize() for f in fans])

    if request.method == 'POST':
        max_speed = content['max_speed']
        new_fan = Fan(monitor, len(fans), max_speed)
        fans.append(new_fan)
        return "Succesfully created fan ", len(fans)-1


@app.route('/subsystem',methods=['GET','POST','PUT'])
def subsystem_operations():
    content=request.json
    if request.method == 'PUT':
        index = content['index']
        temp = content['temperature']
        subsystems[index].set_temp(temp)
        return 'Updated'

    if request.method == 'GET':
        return jsonify([s.serialize() for s in subsystems])

    if request.method == 'POST':
        new_temp = content['temperature']
        new_subsystem = Subsystem(monitor, len(subsystems))
        subsystem.set_temp(new_temp)
        subsystems.append(new_subsystem)
        return "Succesfully created subsystem ", len(fans)-1


app.run(debug=True)











