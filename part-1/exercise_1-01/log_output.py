import time
import uuid

def main():
    random_string = str(uuid.uuid4())
    while True:
        print(time.strftime("%Y-%m-%dT%H:%M:%S"), random_string, sep=": ")
        time.sleep(5)

if __name__=="__main__":
    main()