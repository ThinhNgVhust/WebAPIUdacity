import json
import httplib2

def getGeocodeLocation(inputString):
    google_api_key = "AIzaSyBLTspAddSftdlMt3mhM6KoY7I1-iVtyrk"
    locationString = inputString.replace(" ","+")
    url = ("https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s"%(locationString,google_api_key)) 
    print(url)
    h = httplib2.Http()
    respone, content = h.request(url,"GET")
    print(respone)
    # result = json.load(content)
    return respone
location ="Tokyo Japan"
getGeocodeLocation(location)