#Wayfindr micro:bit activity

##Intro:

This activity uses multiple micro:bits to teach participants the challenges that blind people face when attempting to navigate an unfamiliar indoor environment using the Wayfindr open standard as a guide. Basic networking concepts are also explored.

##Basic overview (more child-friendly documentation coming soon):

Participants should design a root around a given area whilst consulting the Wayfindr open standard to determine what landmarks should be represented and what information a blind person would need to know about them.
Sender micro:bits are then programmed and deployed, after which the template receiver code should be modified to take into account the designed root.
Participants can then walk the root using their receiver which will speak the phrases that they have associated with each sender as they walk past it.

##Steps:

1. Design a root whilst consulting the standard to determine what landmarks should be represented and what information should be conveyed about them.
2. Assign each landmark a number starting from 0.
3. Open sender.py. Change the values of numberOfLandmarks and timeBetweenBroadcasts as per your requirements although sensible defaults have been provided. NB: it is anticipated that participants will mainly be coding receivers - E.G. this file does not need to be extensively modified.
4. When the sender script is flashed to a micro:bit you are first asked to select the level of power to broadcast at. We have found that 0 is a sensible value to start with. You are then asked to select the landmark that the sender should represent. Note that senders don't have an awareness of landmarks per say - that lives in the receiver. Senders merely let you choose a number that they should broadcast up to numberOfLandmarks-1. When the confirmation message has finished being output the sender will start broadcasting indefinitely.
5. Open receiver.py and consult the code to see how it works. We've run this activity multiple times and have had good success in getting beginner programmers to concentrate on modifying the last few lines - E.G. the series of if statements. The existing phrases come from one of our previous activities. If destinationReached=1 is passed to the announce method a short series of tones is appended to the provided phrase to signify this.
6. Once the necessary modifications have been made, connect a speaker to a micro:bit, flash the code and walk the root to test it. How well did it work? Were the phrases spoken when they should have been?

In most scenarios the root will need some tweaking - E.G. you will have to perform some experimentation to determine the optimum broadcast power and placement of each micro:bit. If you have limited amounts of time it would be advisable to carry out said experiments beforehand and document your findings so that on the day participants can focus on designing their receivers instead of pulling their hair out whilst learning about the perils of radio transmission.

Good luck!
