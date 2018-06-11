# LoRa Google Maps

## Build

```shell
pip install paho-mqtt Flask

or

pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

```
cp local.sh.example local.sh
./local.sh
```

## Refs

- https://os.mbed.com/teams/MultiTech/code/Dot-Examples/file/2f5ae37e6c47/examples/src/auto_ota_example.cpp/
- Eclipse Paho™ MQTT Python Client
    - https://github.com/eclipse/paho.mqtt.python
    - https://www.eclipse.org/paho/clients/python/docs/
- https://console.cloud.google.com/
    -  Maps JavaScript API
    -  http://www.oxxostudio.tw/articles/201801/google-maps-4-more-markers.html
    -  http://www.oxxostudio.tw/articles/201802/google-maps-12-rect-circle.html
