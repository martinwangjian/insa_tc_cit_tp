import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
import time as t
import json

# Configuration
# Define ENDPOINT, CLIENT_ID, PATH_TO_CERT, PATH_TO_KEY, PATH_TO_ROOT, MESSAGE, TOPIC, and RANGE
ENDPOINT = "xxxxxxxxxxxxxx-ats.iot.eu-west-1.amazonaws.com"
PATH_TO_CERT = "certificates/xxxxxxxxxx-certificate.pem.crt"
PATH_TO_KEY = "certificates/xxxxxxxxxx-private.pem.key"
PATH_TO_ROOT = "certificates/AmazonRootCA1.pem"
TOPIC = "cxp_insa_tp_iot_mqtt_topic"
CLIENT_ID = "cxp_insa_tp_iot_client_id"
PORT = 8883

myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, PORT)
myAWSIoTMQTTClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)

myAWSIoTMQTTClient.connect()
print('Begin Publish')
print("Topic: {}".format(TOPIC))
# Load sample data
with open('data/data2016-2019.json') as data_file:    
    records = json.load(data_file)

    # Publish each record to mqtt topic every ms
    for record in records:
        print("publish record with date: {}".format(record['fields']['date']))
        myAWSIoTMQTTClient.publish(TOPIC, json.dumps(record), 1)  # 1 = QoS AT_LEAST_ONCE
        t.sleep(1/1000) # ms

print('Publish End')
myAWSIoTMQTTClient.disconnect()
