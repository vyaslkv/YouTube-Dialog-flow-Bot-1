import os.path
import sys
import json
try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = '576ef8f0c5ad4bf797dc7cd4d9f4fbe5'
YOUTUBE_ACCESS_KEY = 'AIzaSyBX3ok8NE8VJQJSCDT_f3I0IPB9lz1VMDU'
URL = 'https://www.googleapis.com/youtube/v3/search'
def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    my_list = []
   
    while True:
        request = ai.text_request()

        request.lang = 'en'  # optional, default value equal 'en'

        request.session_id = "9efa2a4c-b253-405f-8a62-4065471b91a2"

        request.query = input("Bot >")

        response = request.getresponse()
        response = response.read()
        resp = response.decode('UTF-8')
        if request.query=='quit':
            break
        print(resp)    
 #       print (json.loads(response.read())['result']['fulfillment']['speech'])
        #x = json.loads(response.read())["result"]["parameters"]
        for key, value in json.loads(resp)["result"]["parameters"].items():
            if len(value)!=0:
                my_list.append({key:value})
        if len(my_list)==0:
            print("Oops")
        else:
            test = my_list[0][list(my_list[0].keys())[0]]
            test = str(test).replace("[", "")
            test = str(test).replace("]", "")
            print(test)
            import requests
            youtube_url = URL + '?q=' + test + '&part=snippet' + '&key=' + YOUTUBE_ACCESS_KEY
            response = requests.get(youtube_url)
            target_url = 'https://www.youtube.com/watch?v=' + json.loads(response.text)['items'][0]['id']['videoId']
            print(target_url)
            my_list.clear()
                 


if __name__ == '__main__':
    main()
