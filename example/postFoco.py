from tuya_iot import TuyaOpenAPI



ACCESS_ID = "ttqsyphfaykiu0z5jkn2"
ACCESS_KEY = "052bdee751bf48bca3b988026dfb9971"
USERNAME = "raulisai97@gmail.com"
PASSWORD = "mbENwEcb6HJwtR4"
ASSET_ID = "1442611653299441664"
DEVICE_ID = "eb27e4d97424cb61c5lgop"
ENDPOINT = "https://openapi.tuyaus.com"


# Set up device_id
DEVICE_ID ="eb27e4d97424cb61c5lgop"




# Init OpenAPI and connect
openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)	
openapi.login(USERNAME, PASSWORD)

commands = {'commands': [
  {
    "code": "switch_led",
    "value": True
  },
  {
    "code": "work_mode",
    "value": "white"
  }]}	
request = openapi.post(f'/v1.0/iot-03/devices/{DEVICE_ID}/commands', commands)	
print(request)



"""[
  {
    "code": "switch_led",
    "value": true
  },
  {
    "code": "work_mode",
    "value": "white"
  },
  {
    "code": "bright_value_v2",
    "value": 1000
  },
  {
    "code": "temp_value_v2",
    "value": 1000
  },
  {
    "code": "colour_data_v2",
    "value": {
      "h": 0,
      "s": 1000,
      "v": 1000
    }
  },
  {
    "code": "scene_data_v2",
    "value": {
      "scene_num": 1,
      "scene_units": [
        {
          "bright": 200,
          "h": 0,
          "s": 0,
          "temperature": 0,
          "unit_change_mode": "static",
          "unit_gradient_duration": 13,
          "unit_switch_duration": 14,
          "v": 0
        }
      ]
    }
  },
  {
    "code": "countdown_1",
    "value": 0
  },
  {
    "code": "control_data",
    "value": {}
  }
]

     "scale": 0,
      "max": 100,
      "step": 1
    },
    "unit_gradient_duration": {
      "min": 0,
      "scale": 0,
      "max": 100,
      "step": 1
    },
    "bright": {
      "min": 0,
      "scale": 0,
      "max": 1000,
      "step": 1
    },
    "temperature": {
      "min": 0,
      "scale": 0,
      "max": 1000,
      "step": 1
    },
    "h": {
      "min": 0,
      "scale": 0,
      "unit": "",
      "max": 360,
      "step": 1
    },
    "s": {
      "min": 0,
      "scale": 0,
      "unit": "",
      "max": 1000,
      "step": 1
    },
    "v": {
      "min": 0,
      "scale": 0,
      "unit": "",
      "max": 1000,
      "step": 1
    }
  }
}

countdown_1	Integer	

{
  "unit": "",
  "min": 0,
  "max": 86400,
  "scale": 0,
  "step": 1

}

control_data	Json	

{
  "change_mode": {
    "range": [
      "direct",
      "gradient"
    ]
  },
  "bright": {
    "min": 0,
    "scale": 0,
    "unit": "",
    "max": 1000,
    "step": 1
  },
  "temperature": {
    "min": 0,
    "scale": 0,
    "unit": "",
    "max": 1000,
    "step": 1
  },
  "h": {
    "min": 0,
    "scale": 0,
    "unit": "",
    "max": 360,
    "step": 1
  },
  "s": {
    "min": 0,
    "scale": 0,
    "unit": "",
    "max": 255,
    "step": 1
  },
  "v": {
    "min": 0,
    "scale": 0,
    "unit": "",
    "max": 255,
    "step": 1
  }
}
"""