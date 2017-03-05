#Import all the modules we'll need
import microbit
import music
import radio
import speech

previouslyReceivedUniqueID=None #We need to keep track of the last micro:bit that we received a packet from so that we don't keep on announcing it while it's in range

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
 if packet != None: #Make sure we've received something - E.G. there might not be another micro:bit in range
  #Separate the 2 pieces of data in the received packet
  landmarkID=int(packet[5:])
  uniqueID=int(packet[:4])
  if uniqueID != previouslyReceivedUniqueID: #Make sure that what we've received isn't the same as the last thing we received
   previouslyReceivedUniqueID = uniqueID
   #Speak something depending on which landmarkID we've received
   print(packet)
   if landmarkID == 0: announce("Walk forw ud.")
   if landmarkID == 1: announce("Go up the stairs.")
   if landmarkID == 2: announce("Walk through the door.")
   if landmarkID == 3: announce("turn left.")
   if landmarkID == 4: announce("turn right.")
   if landmarkID == 5: announce("destination reached.", destinationReached=1)
