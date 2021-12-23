import time
import os
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

rootCA = os.path.abspath("../../certs/AmazonRootCA1.pem")
privateKey = os.path.abspath("../../certs/private.pem.key")
cert = os.path.abspath("../../certs/device-certificate.pem.crt")

def helloworld(self, params, packet):
    print ('Receved Message from AWS IoT Core')
    print ('Topic: ' + packet.topic)
    print ("Payload: ", (packet.payload))
    
myMQTTClient = AWSIoTMQTTClient("testChrisFeltClientID")
myMQTTClient.configureEndpoint("a2rfrvyjik0srb-ats.iot.us-east-2.amazonaws.com", 8883)

myMQTTClient.configureCredentials(rootCA, privateKey, cert)

myMQTTClient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2) # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10) # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5) #5 sec

print ('Initiating IoT Core Topic ...')
myMQTTClient.connect()
myMQTTClient.subscribe("test/topic", 1, helloworld)

while True:
    time.sleep(5)

