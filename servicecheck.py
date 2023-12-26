import time 
import requests
from plyer import notification

def notifup():
    notification.notify(
    title = "Server up",
    message = "Server is running smoothly",
    timeout = 10
    )
def notifdown():
    notification.notify(
    title = "Server down",
    message = "Server is no longer up :(",
    timeout = 50
    )
def checkservice(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False
    

def main():
    server_url = "https://example.com/"
    interval = 60

    while True:
        if checkservice(server_url):
            print("The server is up")
            notifup()
        else:
            print("The server is down")
            notifdown()
        time.sleep(interval)

if __name__ == "__main__":
    main()

