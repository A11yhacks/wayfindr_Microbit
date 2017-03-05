#Import all the modules we'll need
import microbit
import music
import radio
import speech

previouslyReceivedUniqueID=None

#Sing the before instruction sound and then speak the given phrase. If we're at the end of the root sing the destination sound
def announce(phrase, destinationReached=0):
 speech.sing("um", speed=138, pitch=24)
 speech.sing("um", speed=138, pitch=24)
 microbit.sleep(250)
 speech.say(phrase)
 if destinationReached == 1:
  microbit.sleep(30)
  speech.sing("um", speed=75, pitch=48)
  microbit.sleep(1)
  speech.sing("um", speed=75, pitch=32)
  microbit.sleep(1)
  speech.sing("um", speed=75, pitch=24)


radio.on()
print("Listening...")
while True:
 packet=radio.receive()
 if packet != None: #Make sure we've received something
  #Separate the 2 pieces of data in the received packet
  landmarkID=int(packet[5:])
  uniqueID=int(packet[:4])
  if uniqueID != previouslyReceivedUniqueID: #Make sure that what we've received is different to the last time we were here
   previouslyReceivedUniqueID = uniqueID
   #See if what we've received is something we know about.
   print(packet)
   if landmarkID == 0: announce("Walk forw ud.")
   if landmarkID == 1: announce("Go up the stairs.")
   if landmarkID == 2: announce("Walk through the door.")
   if landmarkID == 3: announce("turn left.")
   if landmarkID == 4: announce("turn right.")
   if landmarkID == 5: announce("destination reached.", destinationReached=1)
