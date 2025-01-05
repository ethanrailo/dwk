import requests, os
from datetime import datetime, timedelta

def fetch_image_file():
    image_url = "https://picsum.photos/300"
    filename = "/usr/src/app/files/image.jpg"

    try:
        modified_time = os.path.getmtime(filename)
    except:
        #Couldn't get the modified time, so cache miss --> get new image
        download_image(image_url, filename)
    else:
        if modified_time < (datetime.now() - timedelta(hours=1)).timestamp():
            #Image-file is older than 1 hour
            #print(f"image file is not current, modified time: {datetime.fromtimestamp(modified_time)} & current time: {datetime.now()}")
            download_image(image_url, filename)

    with open(filename, 'rb') as f:
        image_data = f.read()

    return image_data

def download_image(url, filename):
  response = requests.get(url, stream=True)

  if response.status_code == 200:
    with open(filename, 'wb') as f:
      for chunk in response.iter_content(1024):
        f.write(chunk)
    #print(f"image written to {filename}")
  else:
    print(f"Failed to download image: {response.status_code}")

def shutdown_if_in_container():
    in_container = os.environ.get('IN_CONTAINER')

    if in_container == "1":
        #This file is monitored by different python-process ("shutdown_watchdog.py")
        #If it exists, the watchdog will terminate known PID for the parent process of gunicorn,
        #resulting in the termination of the container -- for debug and testing purposes.
        f = open("/usr/src/app/shutdown.now", "w")
        f.write("True")
        f.close()

        return True

    return False