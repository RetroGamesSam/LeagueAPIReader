import http.client
import json

leagueserver = "euw1.api.riotgames.com"
requestpath = "/lol/summoner/v4/summoners/by-name/"
summonername = "insert summonername here"
APIkey = "insert API-Key here"

class SummonerStats():
    def __init__(self, summonername, leagueserver, requestpath, APIkey):
        self.summonername = summonername
        self.leagueserver = leagueserver
        self.requestpath = requestpath
        self.APIkey = APIkey
        self.html = ""
        self.jsondata = ""
   
    def getAPIResponse(self):
        verb = http.client.HTTPSConnection(self.leagueserver)
        verb.request("GET", self.requestpath + self.summonername + "?api_key=" + self.APIkey)
        resp = verb.getresponse()
        self.html = resp.read()
        return self.html

    def league_input_to_list(self):
        input = str(self.html).split("'")[1]
        self.jsondata = json.loads(str(input))
        print(self.jsondata)
        return self.jsondata

    def getSummonerLvl(self):
        if self.jsondata.get("status").get("status_code") != 404:
            print("Summoner Level: " + str(self.jsondata.get("summonerLevel")))
        else:
            print("Error")
    
    def getSummonerName(self):
        if self.jsondata.get("status").get("status_code") != 404:
            print("Summoner Name: " + str(self.jsondata.get("name")))
        else:
            print("Error")

mySummoner = SummonerStats(summonername, leagueserver, requestpath, APIkey)
mySummoner.getAPIResponse()
mySummoner.league_input_to_list()
mySummoner.getSummonerLvl()
mySummoner.getSummonerName()