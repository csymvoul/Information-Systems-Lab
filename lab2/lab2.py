import time 

def main():
    while True:
        print({'msg': 'Info log','time':time.time()})
        time.sleep(2)

if __name__=="__main__":
    main()
