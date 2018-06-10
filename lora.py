from json import loads
from base64 import b64decode
from os import environ
import paho.mqtt.client as mqtt

"""
hscclab latitude: 24.9896, longitude: 121.3187
lib     latitude: 24.988975405763934, longitude: 121.3138246536255
sci5    latitude: 25.0478, longitude: 121.5318
24.9896,121.3187
24.988975405763934,121.3138246536255
25.0478,121.5318
"""

hostname = environ['MQTT_HOST']
username = environ['MQTT_USERNAME']
password = environ['MQTT_PASSWORD']
topic = environ['MQTT_TOPIC']

def linear_lstsq(rssi):
    # Linear least squares
    m = -14.634517649151988
    c = -953.1439210910365
    distance = rssi * m + c
    return distance

def on_message(mqttc, obj, msg):
    # print('TOPIC:{}, QOS:{}\nPAYLOAD: {}'.format(msg.topic, str(msg.qos), str(msg.payload)))
    j = loads(msg.payload)
    print('光敏電阻器(0~65535):', int(b64decode(j['data'])))

    for item in j['rxInfo']:
        tmp = linear_lstsq(item['rssi'])
        if item['name'] == 'gateway-sci5':
            print('gateway-sci5:    {}'.format(tmp))
            environ['sci5'] = str(tmp)
        elif item['name'] == 'gateway-hscclab':
            print('gateway-hscclab: {}'.format(tmp))
            environ['hscclab'] = str(tmp)
        elif item['name'] == 'gateway-lib':
            print('gateway-lib:     {}'.format(tmp))
            environ['lib'] = str(tmp)
        else:
            print('Fatal error: Unexpected gateway.')

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))

def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)

def mqttc_start():
    # If you want to use a specific client id, use mqttc = mqtt.Client("client-id")
    # but note that the client id must be unique on the broker. Leaving the client id parameter empty will generate a random id for you.
    mqttc = mqtt.Client(transport='tls')
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe
    # mqttc.on_log = on_log # Uncomment to enable debug messages

    mqttc.tls_set() # https://github.com/eclipse/paho.mqtt.python#tls_set
    mqttc.username_pw_set(username=username, password=password)
    mqttc.connect(hostname, 1883, 60)
    mqttc.subscribe(topic, 0)

    mqttc.loop_forever()

if __name__ == '__main__':
    mqttc_start()
