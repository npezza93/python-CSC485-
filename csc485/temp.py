#######################################################
###       Group 3: Nick Pezza and Kevin Flavin      ###
###    CSC 485 Special Topics in Computer Science   ###
###       Dr. Pyzdrowski - MW 4:00pm - 5:15pm       ###
###     Python Program 5 - The Family Relations     ###
#######################################################

import os

#Open Input Method-------------------------------------------------------------------------------------------------------------------
#called in Load Method
#opens the input file name for reading
def open_input():
    choice = True
    i_name = input("Whats the name of the input file? ")                        # gets name of input file from user    
    while not os.path.isfile(i_name) and choice:                                # loops if the file doesnt exist
        print (i_name + " does not exist.")             
        choice = input("Enter another file(1) or quit(2)? ")                    # asks if user wants to enter a new file name or quit
        if "1" == choice:   
            i_name = input("Whats the name of the input file? ")                # gets the new name 
        elif "2" == choice:
            choice = False                                                      # quits
            i_name = False
    return i_name

#Open output method------------------------------------------------------------------------------------------------------------------------------
#called in Save case
# opens the output file for writing 
def open_output():
    flag = True                                                                 # init variable
    o_file = False
    o_name = input("Whats the name of the output file? ")                       # gets name of output file
    while os.path.isfile(o_name) and flag:                                      # loops if the file exists
        print (o_name + " already exists.")
        choice = input("Overwrite(1), pick a different file(2), or return to main menu(3)? ")  # asks if user wants to overwrite, pick dif, or quit
        if choice == "1":
            o_file = open(o_name, "w")                                          # overwrites file and exits loop
            flag = False
        elif choice == "2":
            o_name = input("Whats the name of the output file? ")               # asks for new file name
        elif choice == "3":
            flag = False                                                        # exits loop
    if flag:                                                                    # if not overwrite or quit
        o_file = open(o_name, "w")
    else:
        if not o_file:                                                          # if quit 
            o_file = False
    return o_file   

#Looper Method------------------------------------------------------------------------------------------------------------------------------------
#called in the load method
def looper(i, lines, keywords):
    flag = True
    flag2 = True
    family = dict()																#init the family dict
    i += 1
    while flag:
        if lines[i] == "NAME":
            flag = False														#don't process if it is not a relation
        else:
            if lines[i] in keywords:											#if its a relation, add it
                relation = lines[i]
                members = []
                i += 1															#increment i
                while flag2 and lines[i] not in keywords:						#while it is not a relation
                    members.append(lines[i])									#add the line from file to members
                    i += 1														#increment i
                    if i > (len(lines)-1):										#check for end of file
                        flag2 = False
                        flag = False
                family[relation] = members										#add the members with the relation to family
    return family			

#Load Method-------------------------------------------------------------------------------------------------------------------------------------
#called in Load case	
def load(people):
    in_name = open_input()
    if in_name:
		#intialize the keywords and dictionaries
        in_f = open(in_name, "r")
        keywords = ["FATHER","MOTHER", "SPOUSE", "DAUGHTER", "SON", "NAME"]
        people = dict()
        should_be = []
        file = []
        nm_flag = False
        
		#read and strip each line of the file
        for line in in_f:
            file.append(line.strip())
        
		#place each line to their member
        for i in range(0, len(file)):
            if nm_flag and file[i] not in keywords and file[i] not in people:
                family = looper(i, file, keywords)
               
                for person in people:
                    tree = people[person]
                    for rel in tree:
                        if len(tree[rel]) >0: 
                            for names in tree[rel]:
                                if names == file[i].upper():
                                    should_be.append([person, rel])
                #check for matches
                for person in should_be:
                    if person[1] == "FATHER" or person[1] == "MOTHER":
                        if person[0] in family["SON"] or person[0] in family["DAUGHTER"]:
                            should_be.remove([person[0],person[1]])
                    elif person[1] == "SON" or person[1] == "DAUGHTER":
                        if person[0] in family["FATHER"] or person[0] in family["MOTHER"]:
                            should_be.remove([person[0],person[1]])
                    elif person[1] == "SPOUSE":
                        if person[0] in family["SPOUSE"]:
                            should_be.remove([person[0],person[1]])
        
                if len(should_be) <= 0:                    
                    people[file[i]] = family
                else:
                    for person in should_be:
                        if person[1] == "FATHER" or person[1] == "MOTHER":
                            print(person[0] + " should be " + file[i].upper() + "'s son or daughter")
                        elif person[1] == "SON" or person[1] == "DAUGHTER":
                            print(person[0] + " should be " + file[i].upper() + "'s mother or father")
                        elif person[1] == "SPOUSE":
                            print(person[0] + " should be " + file[i].upper() + "'s spouse")
                    print(file[i].upper() + " will not be added to the database due to inconsistencies in the genealogy.")
                nm_flag =  False
            else:
                nm_flag = False
            
			#reset the flag if its a new person entry
            if file[i].strip().upper() == "NAME":
                nm_flag = True

        in_f.close()														#close the input file
    return people															#return the filled dictionary

#Add Method-------------------------------------------------------------------------------------------------------------------------------------
#called in add case
def add_person(people):
	#set the keywords and dictionaries
    keywords = ["FATHER","MOTHER", "SPOUSE", "DAUGHTER", "SON"]
    individual = dict()
    family = dict()
    should_be = []
    
	#enter the name and check if it exists
    name = input("Enter the name of a person: ").strip()
    if name.upper() not in people and name != "":
		#if it doesn't exist enter the family
        print (name.upper() + "'s family:")
        for keyword in keywords:
            members = []
            member_name = input("ENTER "+ keyword + "S name: ").strip()
            while member_name != "":
                members.append(member_name.upper())
                member_name = input("ENTER ANOTHER " + keyword + "S NAME: ").strip()
            family[keyword] = members
        
        for person in people:
            tree = people[person]
            for rel in tree:
                if len(tree[rel]) >0: 
                    for names in tree[rel]:
                        if names == name.upper():
                            should_be.append([person, rel])
        
        consistency = True
        
		#check if theres matches
        for person in should_be:
            if person[1] == "FATHER" or person[1] == "MOTHER":
                if person[0] in family["SON"] or person[0] in family["DAUGHTER"]:
                    should_be.remove([person[0],person[1]])
            elif person[1] == "SON" or person[1] == "DAUGHTER":
                if person[0] in family["FATHER"] or person[0] in family["MOTHER"]:
                    should_be.remove([person[0],person[1]])
            elif person[1] == "SPOUSE":
                if person[0] in family["SPOUSE"]:
                    should_be.remove([person[0],person[1]])
        
        if len(should_be) <= 0:
            individual[name.upper()] = family
            print("\n" + name.upper() +"S FAMILY:")
            for rel in family:
                print ("\n" + rel.upper())
                print ("-----------------")
                for names in family[rel]:
                    print(names)
            if input("(C) CONFIRM this tree or anything else to reject it: ").upper() != "C":
                individual = False
        else:
            for person in should_be:
                if person[1] == "FATHER" or person[1] == "MOTHER":
                    print(person[0] + " should be " + name.upper() + "'s son or daughter")
                elif person[1] == "SON" or person[1] == "DAUGHTER":
                    print(person[0] + " should be " + name.upper() + "'s mother or father")
                elif person[1] == "SPOUSE":
                    print(person[0] + " should be " + name.upper() + "'s spouse")
            print(name.upper() + " will not be added to the database due to inconsistencies in the genealogy.")
            individual = False
    else:
        print (name.upper() + " already exists!")
        individual = False
    return individual


#------------------------------------------------------------------------------------------------------
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ ---  Main ---  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#------------------------------------------------------------------------------------------------------

#list and directory that program runs off of
people = dict()
flag = True

while flag:
	#display the commands for the user to enter
    print("What would you like to do:\n\t(A) ADD a person \n\t(L) LOAD a person from a file")
    print ("\t(S) SAVE people to a file \n\t(V) VIEW the people described\n\t(I) INFORMATION about a person")
    print ("\t(Q) QUIT\n")
    
	
    selection = input().upper()													#input to handle the command, capitalized for matching
	
#Add----------------------------------------------------------------------------------------------------------------------------------------------  
    if selection == "A" or selection == "ADD":
        new_person = add_person(people)
        if new_person:
            people = dict(list(new_person.items()) + list(people.items()))		#add to directory if confirmed
        print("\n")    
  #Load-------------------------------------------------------------------------------------------------------------------------------------------           
    elif selection == "L" or selection == "LOAD":
        temp = load(people)
        people = dict(list(temp.items()) + list(people.items()))				#add to directory
        print("\n")
  #Save-------------------------------------------------------------------------------------------------------------------------------------------      
    elif selection == "S" or selection == "SAVE":
        out_f = open_output()
        if out_f:
            for person in people:												#write NAME and then the person to the file
                out_f.write("NAME\n" + person.upper() + "\n")
                tree = people[person]
                for rel in tree:												#write the relationship and then the name to the file
                    out_f.write(rel.upper() + "\n")
                    for names in tree[rel]:
                        out_f.write(names+"\n")
            out_f.close()														#close file
        print("\n")    
  #View-------------------------------------------------------- ----------------------------------------------------------------------------------    
    elif selection == "V" or selection == "VIEW":
        if len(people.keys()) > 0:												#printing the people with descibred family's to screen
            print("\nDescribed:")
            for person in people.keys():
                print(person.upper())
                
            print("\nReferenced but not yet described:")						#printing the other names entered to the screen
            for person in people:
                tree = people[person]
                for rel in tree:
                    if len(tree[rel]) >0: 
                        for names in tree[rel]:
                            print(names)
            print()
        else:
            print("\nThere are no people in the database!\n")
        print("\n")
		
  #Info--------------------------------------------------------------------------------------------------------------------------------------------       
    elif selection == "I" or selection == "INFORMATION":
        if len(people.keys()) > 0:
            flag2 = True
            while flag2:
                print("Choose one of the following to get information about:")					#input for user name 
                for person in people:
                    print(person.upper())
                choice = input("\n").strip()

                if choice == "":
                    flag2 = False
                else:
                    if choice.strip().upper() in people:										#if it is in the directory, print the name + family to screen
                        family = people[choice.upper()]
                        print("\nFATHER          MOTHER          SPOUSE          SON             DAUGHTER        ")
                        print("-------------------------------------------------------------------------------")
						#place each relation
                        mothers = family["MOTHER"]
                        fathers = family["FATHER"]
                        sons = family["SON"]
                        daughters = family["DAUGHTER"]
                        spouses = family["SPOUSE"]
						
						#will loop for however many times the max entry is and align each relation in columns
                        for i in range(0,max(len(mothers),len(fathers),len(sons),len(daughters),len(spouses))):
                            try:																#print the fathers name then spaces to align columns
                                print (fathers[i], end="")
                                for n in range(0, (16-len(fathers[i]))):
                                    print(" ", end="")
                            except IndexError: 													#if no father, print 16 spaces
                                print ("                ",end="")
                            try:
                                print (mothers[i], end="")										#print the mothers name then spaces to align columns
                                for n in range(0, (16-len(mothers[i]))):
                                    print(" ", end="")
                            except IndexError: 													#if no mother, print 16 spaces
                                print ("                ",end="")
                            try:
                                print (spouses[i], end="")										#print the spouses name then spaces to align columns
                                for n in range(0, (16-len(spouses[i]))):
                                    print(" ", end="")
                            except IndexError: 													#if no spouse, print 16 spaces
                                print ("                ",end="")
                            try:
                                print (sons[i], end="")											#print the sons name then spaces to align columns
                                for n in range(0, (16-len(sons[i]))):
                                    print(" ", end="")  
                            except IndexError: 													#if no son, print 16 spaces
                                print ("                ",end="") 
                            try:
                                print (daughters[i], end="")									#print the daughters name then spaces to align columns
                                for n in range(0, (16-len(daughters[i]))):
                                    print(" ", end="")
                            except IndexError: 
                                print ("                ",end="")  								#if no daughter, print 16 spaces
                            print()
                        print()
                    else:
                        print(choice.upper() + " is not yet described!")						#output for non-matching input
        else:
            print("\nThere are no people in the database!\n")
        print("\n")
#Quit-----------------------------------------------------------------------------------------------------------------------------------------------    
    elif selection == "Q" or selection == "QUIT":
        flag = False																			#ends loop for main
		
#Invalid--------------------------------------------------------------------------------------------------------------------------------------------
    else:
        print("Not a valid command!\n")