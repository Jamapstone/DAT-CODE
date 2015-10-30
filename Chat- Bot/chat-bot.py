import time
import wikipedia

file = open('stopWords.txt', 'r')
stopWords = file.readlines() 

yesValidations = ['yes', 'Yes', 'yeah','Yeah', 'Thats fine']
noValidations = ['no', 'No', 'nah', 'Nah', 'No thanks']
colours = ['black','blue','brown','grey','green','orange','pink','purple',
           'red','white','yellow']

#Question1
response = raw_input ("What is your name? ")
response = response.lower()
response = " " + response + " "

time.sleep(1)
for word in stopWords:
    response = response.replace(" " + word.strip() + " "," ")

print("Hello" + response)
time.sleep(1)


#Question2
response = raw_input ("I'd like to get to know a little about you, is that okay? ")
response = response.lower()
    
responseWords = response.split()
for word in responseWords:
    if word in yesValidations:
        time.sleep(1)
        print("That's Great, on to my first question")
    elif word in noValidations:
        time.sleep(1)
        print("If that's the case no need to continue, Good bye pal!")
        quit()

time.sleep(2)

#Question3
haveGotColour = False
while not haveGotColour:
    response = raw_input ("What is your favorite colour? ")
    response = response.lower()
    responseWords = response.split()
    for word in responseWords:
        if word in colours:
            time.sleep(1)
            haveGotColour = True
    if not haveGotColour:
        time.sleep(1)
        print("Not heard of such a colour, I'm sorry")

print(response +", cool mine is Purple." )
time.sleep(2)

#Question4
response = raw_input ("What is your favorite animal? ")
response = response.lower()
time.sleep(2)

for word in stopWords:
    response = response.replace(" " + word.strip() + " "," ")
    
print wikipedia.summary(response, sentences=2)
print("My favorite is Elephant" )
time.sleep(2)


#Question5
response = raw_input ("What is your favorite number? ")
response = response.lower()
time.sleep(2)
print("How crazy mine is " + response)
time.sleep(2)
print("We have so much in common")
time.sleep(4)

#CompletionGame
answer = 16

print ("And finally I wanna play a game..")
time.sleep(3)
print ("I'm thinking of number between 1- 100")
time.sleep(2)
print ("You have to guess correctly otherwise this computer will self destruct..")
time.sleep(2)
print ("Guess!")

while True:
    guess = int(input(""))

    if guess < answer:
        print ('Higher')
    elif guess > answer:
        print ('Lower')
    else:
        print ('You may live another day.. Enjoy it.')
        break


        
