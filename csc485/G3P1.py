#######################################################
### Group 3: Nick Pezza and Kevin Flavin			###
### CSC 485 Special Topics in Computer Science		###
### Dr. Pyzdrowski - MW 4:00pm - 5:15pm				###
### Python Program 1 - When will trains meet again	###
#######################################################

# get the two cities names
city1 = input("Enter the name of the departure city: ")
city2 = input("Enter the name of the destination city: ")

# print the beginning of the word problem
print("\nA train is leaving", city1, "headed for", city2, ".\nFollowing the departure of the first train, a second train leaves the station on a parallel track.")
print("\nWhat time will the second train catch up to the first?\n")

# gets all the user inout about the trains
speed1 = int(input("What is the speed of the 1st train? (In MPH)"))
time1 = int(input("What time does the train leave the station?"))
speed2 = int(input("What is the speed of the 2nd train? (In MPH)"))
time2 = int(input("How many hours later does the 2nd train leave?"))
destination = int(input("How long is the trip? (In miles) "))

# calculates the closing speed of the second train
closespd = speed2 - speed1

# calculates the the meeting time 
initiald = speed1 * time2
closetime = initiald/closespd
closetimehrs = initiald//closespd
closetimemin = (closetime*60)%60
closetimesec = (closetimemin*60)%60

# calculates the meeting distance and percentage
closedist = closetime * speed2
closeperc = closedist/destination*100.0

# prints the world problem with the inputs given
print("\nA train left " + city1 + " at time " + str(time1) + " traveling at " + str(speed1) + "MPH headed for " + city2 + " " + str(destination) + " miles away.")
print ("Following the departure of the first train, a second train leaves the station at time " + str(time2) + " on a parallel track traveling at " + str(speed2) + "MPH.")

# if the second train catches the first prints when and where it does else it says they didnt meet
if closedist < destination:
	print("The second train catches up " + str('%.2f'%closedist) + " miles away which is " + str('%.1f%%'%closeperc) + " of the total distance of the trip")
	print("The second train catches up in " + str(closetimehrs) + " hour(s), " + str('%.0f'%closetimemin) + " minute(s), and " + str('%.2f'%closetimesec) + " seconds")
else:
	print("The second train does not catch the first")  