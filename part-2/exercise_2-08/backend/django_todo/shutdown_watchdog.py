import time, os.path

def main():
    while True:
        #If the Django-application has written the file to disk, it is a sign
        #to terminate the known process for the gunicorn and thus resulting
        #container shutdown. For testing/debbuging.
        if os.path.isfile("/usr/src/app/shutdown.now"):
            os.system("kill -9 7")  
        time.sleep(5)

if __name__=="__main__":
    main()