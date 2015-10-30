import twitter, datetime
import sqlite3

user = 514844672

file = open("TwitterCredentials.txt")
creds = file.readline().strip().split(',')

currentSession=open("/Users/joshuamapstone/Library/Application Support/Google/Chrome/Default/Current Session")
rawtext = currentSession.read()
lines = rawtext.splitlines()

historyURL = ""

for line in lines:
 if(line.find("//") != -1):
    startIndex = line.rfind("//") + 2
    endIndex = line.rfind("/")
    historyURL = line[startIndex:endIndex]
    
print(historyURL)

api = twitter.Api(creds[0],creds[1],creds[2],creds[3])
statuses = api.GetUserTimeline(user)
print (statuses[0].text)


timestamp = datetime.datetime.utcnow()

console = sqlite3.connect("/Users/joshuamapstone/Library/Application Support/Google/Chrome/Default/History")
cursor = console.cursor()


cursor.execute("SELECT * FROM urls")

title = cursor.execute("SELECT title FROM urls limit 1" )




rows = cursor.fetchall()

for row in rows:
    response = api.PostUpdate(row[0] + " is a Good Website url found here " + historyURL + " " + str(timestamp))
    print("Status updated to: " + response.text)
    
console.close()


