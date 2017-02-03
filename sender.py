from microbit import *
import radio
import random

broadcastPower=""
landmarkID="" #What landmark will we be representing?
timeBetweenBroadcasts=100 #How long to wait (in MS) between broadcasts. Decreasing this number will make the system more responsive at the expense of battery life
numberOfLandmarks=6 #How many different landmarks does the root contain?

def selectBroadcastPower():
 display.clear()
 i=0
 print(i)
 button_a.was_pressed()
 button_b.was_pressed()
 while True:
  display.show(str(i), wait=False)
  if button_b.was_pressed(): return i
  if button_a.was_pressed():
   i=i+1
   if i > 7: i=0
   display.clear()
   print(i)

def selectLandmark():
 display.clear()
 i=0
 print(i)
 while True:
  display.show(str(i), delay=100, wait=False)
  if button_b.was_pressed(): return i
  if button_a.was_pressed():
   i=i+1
   if i > numberOfLandmarks-1: i=0
   display.clear()
   print(i)

def startBroadcasting(broadcastPower, landmarkID):
 random.seed(running_time())
 uniqueID=str(random.randint(4999,9999)) #Was previously 1000,9999 but weird issue where it was bias towards 1000 todo does this still happen?
 stringToSend=str(uniqueID)+":"+str(landmarkID) 
 messageToPrint="I am broadcasting "+str(landmarkID)+", at a power level of "+str(broadcastPower)+", with a unique ID of "+str(uniqueID)+"."
 print(messageToPrint)
 display.scroll(messageToPrint, delay=100, wait=True)
 sleep(1000)
 display.clear()
 radio.on()
 radio.config(power=broadcastPower, length=8)
 while True:
  radio.send(stringToSend)
  sleep(timeBetweenBroadcasts)

message="Select my broadcast power using button a then press b to continue."
display.scroll(message, delay=100, wait=False)
print(message)
while broadcastPower == "":
 if button_a.was_pressed():
  broadcastPower=selectBroadcastPower()
display.clear()
message="Select the landmark that I should represent using button a then press b to continue."
display.scroll(message, delay=100, wait=False)
print(message)
while landmarkID == "":
 if button_a.was_pressed():
  landmarkID=selectLandmark()
display.clear()
startBroadcasting(broadcastPower, landmarkID)