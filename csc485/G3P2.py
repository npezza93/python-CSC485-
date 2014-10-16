#######################################################
### Group 3: Nick Pezza and Kevin Flavin			###
### CSC 485 Special Topics in Computer Science		###
### Dr. Pyzdrowski - MW 4:00pm - 5:15pm				###
### Python Program 2 - The Averaging Program		###
#######################################################

# initialize variables for the loop
flag = True													# kicks out of the infinite loop
count = 0													# keeps count of how many grades are entered
total_grades = 0											# stores the sum of the grades entered

# infinite that stops if outside range or not an int
while flag:
    try:
        x = float(input('Enter a grade: '))    				# grabs the grade and converts to int
        if x<0 or x>100:									# checks if outside range
            flag=False										# ends loop if outside range
        else:
            count += 1 										# increments count if all clear
            total_grades += x								# accumulates sum
    except ValueError:										# if not an int ends loop
        flag = False
        
if count != 0:
	avg = total_grades//count 								# calculates the avg of the grades

	# determines the letter grade based on the avg				
	if avg >= 90:	
	    letter = 'A'
	elif avg >=80 and avg <90:
	    letter = 'B'
	elif avg >=70 and avg <80:
	    letter = 'C'
	elif avg >=60 and avg <70:
	    letter = 'D'
	else:
	    letter = 'F'

	print ('\nCount: ', str(count))							# prints how many grades were entered		
	print ('Total of grades entered: ', str(total_grades))	# prints the sum of all the grades
	print ('Average: ', str(avg), '(', letter,')')			# prints the average of the grades along with the letter grade
else:
	print ("No grades were entered")
