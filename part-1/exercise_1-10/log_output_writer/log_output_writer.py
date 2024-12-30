import time, os

logfile = os.environ.get('LOGFILE_PATH', "log-output.txt")

def write_log(message):
    f = open(logfile, "w")
    f.write(message)
    f.close()

def main():
    while True:
        message = time.strftime("%Y-%m-%dT%H:%M:%S")
        print("{} written to logfile: {}".format(message, logfile))
        write_log(message)
        time.sleep(5)

if __name__=="__main__":
    main()

