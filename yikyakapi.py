import string
import requests
import urllib
import urllib2
import socket
import zlib
import random

class YikYakAPI:
    endPointIP = "107.170.53.122"
    endPointURL = "http://yikyakapp.com/YikYakFiles/"
    
    def __init__(self, proxyIP, proxyPort):
        self.proxyIP = proxyIP
        self.proxyPort = proxyPort

    def base(self, file):
		return str(self.endPointURL + file + ".php")
    
    def get(self, file, *paras):
        params = "?" + self.params(paras)
        proxies = { "http": "http://" + self.proxyIP + ":" + self.proxyPort }
		headers = { "User-Agent": "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19" }
        return requests.get(str(self.base(file) + params), proxies=proxies, headers=headers).text
        
    def post(self, file, *paras):
        params = self.params(paras)
        proxies = { "http": "http://" + self.proxyIP + ":" + self.proxyPort }
        headers = { 
		"User-Agent": "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19",
		"Content-Type": "application/x-www-form-urlencoded" }
        print str(self.base(file)) + " - " + params
        return requests.post(str(self.base(file)), proxies=proxies, data=params, headers=headers).text
        
    def params(self, st2r):
        build = ""
        firstRunSkip = False
        switchT = False
        for arg in st2r:
            if (firstRunSkip):
                firstRunSkip = False
                continue
            if (switchT):
                build += "=" + arg + "&"
                switchT = False
            else:
                build += "" + arg
                switchT = True
                
        build = build[:-1]
        return build
            
    
    def getMyTops(self, userID):
        return self.get("getMyTops", "userID", userID)
    
    def getComments(self, userID, messageID):
        return self.get("getComments", "userID", userID, "messageID", messageID)
    
    def deleteMessage(self, userID, messageID):
        return self.get("deleteMessage2", "userID", userID, "messageID", messageID)
        
    def repostMessage(self, userID, messageID, latitude, longitude):
        return self.get("reyakMessage", "messageID", messageID, "userID", userID, "latitude", latitude, "longitude", longitude)

    def upvoteComment(self, userID, commentID):
        return self.get("likeComment", "commentID", commentID, "userID", userID)
    
    def downvoteComment(self, userID, commentID):
        return self.get("downvoteComment", "commentID", commentID, "userID", userID)
        
    def postComment(self, userID, messageID, comment):
        return self.post("postComment", "userID", userID, "messageID", messageID, "comment", urllib.quote_plus(comment))
        
    def getHandleInfo(self, userID):
        return self.get("getHandleInfo", "userID", userID)
        
    def updateHandle(self, userID, handle):
        return self.get("updateHandle", "userID", userID, "handle", handle)
    
    def redeemCode(self, userID, code):
        return self.get("redeemCode", "userID", userID, "code", code)
        
    def getAreaTops(self, lat, long):
        return self.get("getAreaTops", "lat", lat, "long", long)
        
    def postMessage(self, userID, lat, long, distance, message):
        return self.post("sendMessage", "userID", userID, "lat", lat, "long", long, "distance", distance, "message", urllib.quote_plus(message), "hidePin", "0")
        
    def deleteComment(self, userID, messageID, commentID):
        return self.get("deleteComment", "commentID", commentID, "userID", userID, "messageID", messageID)
        
    def updateLocation(self, userID, lat, long):
        return self.get("updateLocation", "userID", userID, "lat", lat, "long", long)
        
    def registerUser(self, userID):
        return self.get("registerUser", "userID", userID)
        
    def getMessages(self, userID):
        return self.get("getMessages", "userID", userID)
        
    def upvoteMessage(self, userID, messageID):
        return self.get("likeMessage", "userID", userID, "messageID", messageID)
        
    def downvoteMessage(self, userID, messageID):
        return self.get("downvoteMessage", "userID", userID, "messageID", messageID)
        
    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    
    def genUserID(self):
        userID = "00000000-0000-0000-0000-000000000000"
        spl = userID.split("-")
        newUserID = ""
        for stp in spl:
            newUserID += self.id_generator(len(stp)) + "-"
        return newUserID[:-1]
        
    def genCoords(self):
        lat = "00.000000"
        long = "00.000000"
        spl1 = lat.split(".")
        spl2 = long.split(".")
        newLat = ""
        for stp in spl1:
            newLat += self.id_generator(len(stp), string.digits) + "."
        newLat = newLat[:-1]
        newLong = ""
        if (int(self.id_generator(1, string.digits)) % 2 == 0):
            newLong += "-"
        for stp in spl2:
            newLong += self.id_generator(len(stp), string.digits) + "."
        newLong = newLong[:-1]
        return [ newLat, newLong ]
        
#yyapi = YikYakAPI()

#request = yyapi.getAreaTops("0","0")
#response = urllib2.urlopen(request)
#the_page = response.read()
#print the_page

# Generate user ID
#print yyapi.genUserID()

#request2 = urllib2.urlopen(yyapi.registerUser("9NR3X8QT-0JBV-UVCK-Q84T-UG1DBNTU8V09")).read()
#print request2

#coords = yyapi.genCoords()
#request = yyapi.updateLocation("9NR3X8QT-0JBV-UVCK-Q84T-UG1DBNTU8V09", coords[0], coords[1])
#response = urllib2.urlopen(request, timeout=30)
#the_page = response.read()
#print the_page

#request = yyapi.postMessage("9NR3X8QT-0JBV-UVCK-Q84T-UG1DBNTU8V09", coords[0], coords[1], "2", "Test")
#response = urllib2.urlopen(request, timeout=30)
#the_page = response.read()
#print the_page

#coords = yyapi.genCoords()

# Register User
#request = yyapi.registerUser(userID)

# Spam flow:

# Generate User ID (format: 00000000-0000-0000-0000-000000000000)
# Register User
# Post defined message at random coordinates
# Get own yak message @ add message ID to array
# Get random message ID from array, upvote it once, then delete it (saves RAM).
# Repeat from step 2

# Eventually...

# Post anonymous message
# Have every single bot upvote it.
