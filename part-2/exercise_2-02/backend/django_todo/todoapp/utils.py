import os

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