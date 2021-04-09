import requests, time 

city = "Athens"
state = "Attiki"
country = "gr"
key = "dcff3a1b197264b4ba1fb5fe20a6ca4b"
url = "https://api.openweathermap.org/data/2.5/weather?q="+city+","+state+","+country+"&appid="+key

def main():
    headers = {"Content-Type":"application/json"}
    try:
        response = requests.get(url=url,headers=headers)
        return response.json()
    except Exception as e:
        print(e)
        return None 
    
if __name__=="__main__":
    print("Weather requester started ...")
    while True:
        resp = main()
        print(resp)
        time.sleep(60)