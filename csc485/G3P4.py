import os
from G3P5 import editPerson, relationships

# opens the input file name for reading
def open_input():
    choice = True
    i_name = input("Whats the name of the input file? ")                        # gets name of input file from user    
    while not os.path.isfile(i_name) and choice:                                        # loops if the file doesnt exist
        print (i_name + " does not exist.")             
        choice = input("Enter another file(1) or quit(2)? ")                    # asks if user wants to enter a new file name or quit
        if "1" == choice:   
            i_name = input("Whats the name of the input file? ")                # gets the new name 
        elif "2" == choice:
            choice = False                                                      # quits
            i_name = False
    return i_name

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

def looper(i, lines, keywords):
    flag = True
    flag2 = True
    family = dict()
    i += 1
    while flag:
        if lines[i] == "NAME":
            flag = False
        else:
            if lines[i] in keywords:
                relation = lines[i]
                members = []
                i += 1
                while flag2 and lines[i] not in keywords:
                    members.append(lines[i])
                    i += 1
                    if i > (len(lines)-1):
                        flag2 = False
                        flag = False
                family[relation] = members
    return family
    
def load(people):
    in_name = open_input()
    if in_name:
        in_f = open(in_name, "r")
        keywords = ["FATHER","MOTHER", "SPOUSE", "DAUGHTER", "SON", "NAME"]
        keywords2 = ["FATHER","MOTHER", "SPOUSE", "DAUGHTER", "SON"]
        people = dict()
        should_be = []
        should_rem = []
        file = []
        nm_flag = False
        
        for line in in_f:
            file.append(line.strip())
        
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
                del should_rem[:]
                del should_be[:]

                if len(should_be) >0:
                    for i in range(len(should_be)):
                        if should_be[i][1] == "FATHER" or should_be[i][1] == "MOTHER":
                            if should_be[i][0] in family["SON"] or should_be[i][0] in family["DAUGHTER"]:
                                should_rem.append(i)
                        elif should_be[i][1] == "SON" or should_be[i][1] == "DAUGHTER":
                            if should_be[i][0] in family["FATHER"] or should_be[i][0] in family["MOTHER"]:
                                should_rem.append(i)
                        elif should_be[i][1] == "SPOUSE":
                            if should_be[i][0] in family["SPOUSE"]:
                                should_rem.append(i)
                
                for i in should_rem:
                    del should_be[i]

                if len(should_be) <= 0:    
                    keys = family.keys()
                    for key in keywords2:
                        if key not in keys:
                            family[key]=[]
                            
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
            
            if file[i].strip().upper() == "NAME":
                nm_flag = True

        in_f.close()
    return people

def add_person(people):
    keywords = ["FATHER","MOTHER", "SPOUSE", "DAUGHTER", "SON"]
    individual = dict()
    family = dict()
    should_be = []
    
    name = input("Enter the name of a person: ").strip()
    
    if name.upper() not in people and name != "":
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




people = dict()
flag = True

while flag:
    print("What would you like to do:\n\t(A) ADD a person \n\t(L) LOAD a person from a file")
    print ("\t(S) SAVE people to a file \n\t(V) VIEW the people described\n\t(I) INFORMATION about a person")
    print ("\t(E) EDIT a person\n\t(D) DELETE a person\n\t(R) RELATIONSHIP of a person")
    print("\t(H) HELP\n\t(U) UPDATE the described lists\n\t(Q) QUIT\n")
    
    selection = input().upper()
    if selection == "A" or selection == "ADD":
        new_person = add_person(people)
        if new_person:
            people = dict(list(new_person.items()) + list(people.items()))
            
            
    elif selection == "L" or selection == "LOAD":
        temp = load(people)
        people = dict(list(temp.items()) + list(people.items()))
        
        
    elif selection == "S" or selection == "SAVE":
        out_f = open_output()
        if out_f:
            for person in people:
                out_f.write("NAME\n" + person.upper() + "\n")
                tree = people[person]
                for rel in tree:
                    out_f.write(rel.upper() + "\n")
                    for names in tree[rel]:
                        out_f.write(names+"\n")
            out_f.close()
            
            
    elif selection == "V" or selection == "VIEW":
        if len(people.keys()) > 0:
            print("\nDescribed:")
            for person in people.keys():
                print(person.upper())
                
            print("\nReferenced but not yet described:")
            keys = people.keys()
            for person in people:
                tree = people[person]
                for rel in tree:
                    if len(tree[rel]) >0: 
                        for names in tree[rel]:
                            if names not in keys:
                                print(names)
            print()
        else:
            print("\nThere are no people in the database!\n")
        
        
    elif selection == "I" or selection == "INFORMATION":
        if len(people.keys()) > 0:
            flag2 = True
            while flag2:
                print("Choose one of the following to get information about:")
                for person in people:
                    print(person.upper())
                choice = input("\n").strip()

                if choice == "":
                    flag2 = False
                else:
                    if choice.strip().upper() in people:
                        family = people[choice.upper()]
                        print("\nFATHER          MOTHER          SPOUSE          SON             DAUGHTER        ")
                        print("-------------------------------------------------------------------------------")
                        mothers = family["MOTHER"]
                        fathers = family["FATHER"]
                        sons = family["SON"]
                        daughters = family["DAUGHTER"]
                        spouses = family["SPOUSE"]
                        for i in range(0,max(len(mothers),len(fathers),len(sons),len(daughters),len(spouses))):
                            try:
                                print (fathers[i], end="")
                                for n in range(0, (16-len(fathers[i]))):
                                    print(" ", end="")
                            except IndexError: 
                                print ("                ",end="")
                            try:
                                print (mothers[i], end="")
                                for n in range(0, (16-len(mothers[i]))):
                                    print(" ", end="")
                            except IndexError: 
                                print ("                ",end="")
                            try:
                                print (spouses[i], end="")
                                for n in range(0, (16-len(spouses[i]))):
                                    print(" ", end="")
                            except IndexError: 
                                print ("                ",end="")
                            try:
                                print (sons[i], end="")
                                for n in range(0, (16-len(sons[i]))):
                                    print(" ", end="")  
                            except IndexError: 
                                print ("                ",end="") 
                            try:
                                print (daughters[i], end="")
                                for n in range(0, (16-len(daughters[i]))):
                                    print(" ", end="")
                            except IndexError: 
                                print ("                ",end="")  
                            print()
                        print()
                    else:
                        print(choice.upper() + " is not yet described!")
        else:
            print("\nThere are no people in the database!\n")
            
    elif selection == "E" or selection == "EDIT":
        people = editPerson(people)
    elif selection == "D" or selection == "DELETE":
        d_quit = False

        while not d_quit:
            print("Choose one of the following to delete:")
            for key in list(people.keys()):
                print(key.title())
            d_flag = True
            
            while d_flag:
                d_person = input("\n").strip().upper()
                if d_person == "":
                    d_quit = True
                    d_flag = False
                elif d_person in people:
                    d_flag = False
            
            if not d_quit:
                print("You are about to delete " + d_person.title() + ". Are you sure? (yes/no)", end="")
                if  input("\n").strip().upper() == "YES":
                    del people[d_person]
                else:
                    print("Deletion aborted. Going to main menu.")
            
    elif selection == "R" or selection == "RELATIONSHIP":
        relationships(people)
    elif selection == "H" or selection == "HELP":
        print("help")
    elif selection == "U" or selection == "UPDATE":
        print("update")
                        
    elif selection == "Q" or selection == "QUIT":
        flag = False
    else:
        print("Not a valid command!\n")