import wiotp.sdk.device
import time
import os
import datetime
import random

#IBM CREDENTIALS
myConfig = {
"identity": {
"orgId":"94ab7c",
"typeId":"Node",
"deviceId": "esp2"
},
"auth": {
"token": "ChVhYc0Dz(AD*rSw9A"
} }

client = wiotp.sdk.device.DeviceClient (config=myConfig,logHandlers=None)
client.connect ()

#Commands received through App/node red
def myCommandCallback (cmd) :
    print ("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    if (m=="Motor_on"):
        print ("Motor is switched on")
    elif (m=="Motor_off"):
        print ("Motor is switched OFF")
    print (" ")

while True:
    #Generate random sensor values
    soil=random.randint (1,4000)
    temp=random.randint (-10,60)
    ldr=random.randint (0, 1023)
    rain=random.randint (0, 1023)
    ph=random.randint (5, 9)
    #Publish and subscribe to IBM IoT platform
    myData={'Temperature':temp,'Soil_moisture': soil,'Ambient_Light_LDR':ldr,'Rain_sensor':rain,'pH_sensor':ph}
    client.publishEvent (eventId="status", msgFormat="json", data=myData, qos=0 , onPublish=None)
    print ("Published data Successfully: ", myData)
    time.sleep (2)
    client.commandCallback = myCommandCallback
client.disconnect ()
