import serial
import time
import requests
import json

# Firebase database URL
firebase_url = 'https://test-9aa10-default-rtdb.firebaseio.com/'

# Set up the serial connection
ser = serial.Serial('COM7', 9600, timeout=1)

def upload_to_firebase(data):
    # Prepare data in JSON format
    json_data = json.dumps(data)
    # Send data to Firebase
    result = requests.post(firebase_url + '/gyroscope.json', json_data)
    print(f"Data sent to Firebase: {result.status_code}, {result.text}")

while True:
    try:
        # Read line from serial
        line = ser.readline().decode('utf-8').strip()
        if line:
            print(f"Received: {line}")
            # Parse the gyroscope data
            x, y, z = map(float, line.replace('Gyroscope X: ', '').replace(' Y: ', '').replace(' Z: ', '').replace(' dps', '').split(','))
            # Prepare data with timestamp
            data = {
                "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
                "x": x,
                "y": y,
                "z": z
            }
            # Upload data to Firebase
            upload_to_firebase(data)
        time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped by User")
        break
    except Exception as e:
        print(f"Error: {e}")
        break

# Close the serial connection
ser.close()
