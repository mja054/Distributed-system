import requests
import time

def long_poll():
    while True:
        try:
            # Initiating a long polling request to the server
            response = requests.get('http://127.0.0.1:5000/get_data', timeout=None)

            # Handle the received data (for demonstration, just printing to console)
            data = response.json()
            print("Received data:", data)

            # Update the UI or perform other actions based on the received data
            # For demonstration, printing the received message
            print("Message:", data["message"])

        except requests.RequestException as e:
            # Handle errors (for demonstration, just printing to console)
            print("Error in long polling request:", str(e))

        # Simulating a pause before making the next long polling request
        time.sleep(1)

if __name__ == '__main__':
    long_poll()

