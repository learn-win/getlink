# Hello guys , I am Learn-win
# GITHUB PROFILE LINK : https://github.com/learn-win/
import requests
def check():
    print("--------------------start----------------------------------")
   
   
    api="Replace-Your-Google-Search-Api"
   
   
    search="260102c500dd64dfa"
    search_query=input("Search value: ")
    fileFormat=input("File format: ")
    url="https://www.googleapis.com/customsearch/v1"
    parms={
    'q': search_query,
    'key':api,
    'cx':search,
    'fileType':fileFormat,
    }
    response=requests.get(url, params=parms)
    result=response.json()
    value=result['items']
    j=1
    print("Result are : ",search_query)
    for i in value:
        responseLink=requests.get(i['link']).status_code
        if(responseLink == 200):
            print(j," ",i['title'],":",i['link'])
            j=j+1
    print("--------------------end----------------------------------")

a=input("Enter the 'y' to contine: ")
if a=='y':
     try:
        check()
     except :
        print("Invalid")
else:
    print("Thank You")
