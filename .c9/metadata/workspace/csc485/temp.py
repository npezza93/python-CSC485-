{"filter":false,"title":"temp.py","tooltip":"/csc485/temp.py","undoManager":{"mark":27,"position":27,"stack":[[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":0},"end":{"row":0,"column":55}},"text":"#######################################################"},{"action":"insertText","range":{"start":{"row":0,"column":55},"end":{"row":1,"column":0}},"text":"\n"},{"action":"insertLines","range":{"start":{"row":1,"column":0},"end":{"row":44,"column":0}},"lines":["### Group 3: Nick Pezza and Kevin Flavin\t\t\t###","### CSC 485 Special Topics in Computer Science\t\t###","### Dr. Pyzdrowski - MW 4:00pm - 5:15pm\t\t\t\t###","### Python Program 2 - The Averaging Program\t\t###","#######################################################","","# initialize variables for the loop","flag = True\t\t\t\t\t\t\t\t\t\t\t\t\t# kicks out of the infinite loop","count = 0\t\t\t\t\t\t\t\t\t\t\t\t\t# keeps count of how many grades are entered","total_grades = 0\t\t\t\t\t\t\t\t\t\t\t# stores the sum of the grades entered","","# infinite that stops if outside range or not an int","while flag:","    try:","        x = float(input('Enter a grade: '))    \t\t\t\t# grabs the grade and converts to int","        if x<0 or x>100:\t\t\t\t\t\t\t\t\t# checks if outside range","            flag=False\t\t\t\t\t\t\t\t\t\t# ends loop if outside range","        else:","            count += 1 \t\t\t\t\t\t\t\t\t\t# increments count if all clear","            total_grades += x\t\t\t\t\t\t\t\t# accumulates sum","    except ValueError:\t\t\t\t\t\t\t\t\t\t# if not an int ends loop","        flag = False","        ","if count != 0:","\tavg = total_grades//count \t\t\t\t\t\t\t\t# calculates the avg of the grades","","\t# determines the letter grade based on the avg\t\t\t\t","\tif avg >= 90:\t","\t    letter = 'A'","\telif avg >=80 and avg <90:","\t    letter = 'B'","\telif avg >=70 and avg <80:","\t    letter = 'C'","\telif avg >=60 and avg <70:","\t    letter = 'D'","\telse:","\t    letter = 'F'","","\tprint ('\\nCount: ', str(count))\t\t\t\t\t\t\t# prints how many grades were entered\t\t","\tprint ('Total of grades entered: ', str(total_grades))\t# prints the sum of all the grades","\tprint ('Average: ', str(avg), '(', letter,')')\t\t\t# prints the average of the grades along with the letter grade","else:","\tprint (\"No grades were entered\")"]}]}],[{"group":"doc","deltas":[{"action":"removeLines","range":{"start":{"row":0,"column":0},"end":{"row":44,"column":0}},"nl":"\n","lines":["#######################################################","### Group 3: Nick Pezza and Kevin Flavin\t\t\t###","### CSC 485 Special Topics in Computer Science\t\t###","### Dr. Pyzdrowski - MW 4:00pm - 5:15pm\t\t\t\t###","### Python Program 2 - The Averaging Program\t\t###","#######################################################","","# initialize variables for the loop","flag = True\t\t\t\t\t\t\t\t\t\t\t\t\t# kicks out of the infinite loop","count = 0\t\t\t\t\t\t\t\t\t\t\t\t\t# keeps count of how many grades are entered","total_grades = 0\t\t\t\t\t\t\t\t\t\t\t# stores the sum of the grades entered","","# infinite that stops if outside range or not an int","while flag:","    try:","        x = float(input('Enter a grade: '))    \t\t\t\t# grabs the grade and converts to int","        if x<0 or x>100:\t\t\t\t\t\t\t\t\t# checks if outside range","            flag=False\t\t\t\t\t\t\t\t\t\t# ends loop if outside range","        else:","            count += 1 \t\t\t\t\t\t\t\t\t\t# increments count if all clear","            total_grades += x\t\t\t\t\t\t\t\t# accumulates sum","    except ValueError:\t\t\t\t\t\t\t\t\t\t# if not an int ends loop","        flag = False","        ","if count != 0:","\tavg = total_grades//count \t\t\t\t\t\t\t\t# calculates the avg of the grades","","\t# determines the letter grade based on the avg\t\t\t\t","\tif avg >= 90:\t","\t    letter = 'A'","\telif avg >=80 and avg <90:","\t    letter = 'B'","\telif avg >=70 and avg <80:","\t    letter = 'C'","\telif avg >=60 and avg <70:","\t    letter = 'D'","\telse:","\t    letter = 'F'","","\tprint ('\\nCount: ', str(count))\t\t\t\t\t\t\t# prints how many grades were entered\t\t","\tprint ('Total of grades entered: ', str(total_grades))\t# prints the sum of all the grades","\tprint ('Average: ', str(avg), '(', letter,')')\t\t\t# prints the average of the grades along with the letter grade","else:","\tprint (\"No grades were entered\")"]},{"action":"insertText","range":{"start":{"row":0,"column":0},"end":{"row":0,"column":55}},"text":"#######################################################"},{"action":"insertText","range":{"start":{"row":0,"column":55},"end":{"row":1,"column":0}},"text":"\n"},{"action":"insertLines","range":{"start":{"row":1,"column":0},"end":{"row":337,"column":0}},"lines":["###       Group 3: Nick Pezza and Kevin Flavin      ###","###    CSC 485 Special Topics in Computer Science   ###","###       Dr. Pyzdrowski - MW 4:00pm - 5:15pm       ###","###     Python Program 5 - The Family Relations     ###","#######################################################","","import os","","#Open Input Method-------------------------------------------------------------------------------------------------------------------","#called in Load Method","#opens the input file name for reading","def open_input():","    choice = True","    i_name = input(\"Whats the name of the input file? \")                        # gets name of input file from user    ","    while not os.path.isfile(i_name) and choice:                                # loops if the file doesnt exist","        print (i_name + \" does not exist.\")             ","        choice = input(\"Enter another file(1) or quit(2)? \")                    # asks if user wants to enter a new file name or quit","        if \"1\" == choice:   ","            i_name = input(\"Whats the name of the input file? \")                # gets the new name ","        elif \"2\" == choice:","            choice = False                                                      # quits","            i_name = False","    return i_name","","#Open output method------------------------------------------------------------------------------------------------------------------------------","#called in Save case","# opens the output file for writing ","def open_output():","    flag = True                                                                 # init variable","    o_file = False","    o_name = input(\"Whats the name of the output file? \")                       # gets name of output file","    while os.path.isfile(o_name) and flag:                                      # loops if the file exists","        print (o_name + \" already exists.\")","        choice = input(\"Overwrite(1), pick a different file(2), or return to main menu(3)? \")  # asks if user wants to overwrite, pick dif, or quit","        if choice == \"1\":","            o_file = open(o_name, \"w\")                                          # overwrites file and exits loop","            flag = False","        elif choice == \"2\":","            o_name = input(\"Whats the name of the output file? \")               # asks for new file name","        elif choice == \"3\":","            flag = False                                                        # exits loop","    if flag:                                                                    # if not overwrite or quit","        o_file = open(o_name, \"w\")","    else:","        if not o_file:                                                          # if quit ","            o_file = False","    return o_file   ","","#Looper Method------------------------------------------------------------------------------------------------------------------------------------","#called in the load method","def looper(i, lines, keywords):","    flag = True","    flag2 = True","    family = dict()\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t#init the family dict","    i += 1","    while flag:","        if lines[i] == \"NAME\":","            flag = False\t\t\t\t\t\t\t\t\t\t\t\t\t\t#don't process if it is not a relation","        else:","            if lines[i] in keywords:\t\t\t\t\t\t\t\t\t\t\t#if its a relation, add it","                relation = lines[i]","                members = []","                i += 1\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t#increment i","                while flag2 and lines[i] not in keywords:\t\t\t\t\t\t#while it is not a relation","                    members.append(lines[i])\t\t\t\t\t\t\t\t\t#add the line from file to members","                    i += 1\t\t\t\t\t\t\t\t\t\t\t\t\t\t#increment i","                    if i > (len(lines)-1):\t\t\t\t\t\t\t\t\t\t#check for end of file","                        flag2 = False","                        flag = False","                family[relation] = members\t\t\t\t\t\t\t\t\t\t#add the members with the relation to family","    return family\t\t\t","","#Load Method-------------------------------------------------------------------------------------------------------------------------------------","#called in Load case\t","def load(people):","    in_name = open_input()","    if in_name:","\t\t#intialize the keywords and dictionaries","        in_f = open(in_name, \"r\")","        keywords = [\"FATHER\",\"MOTHER\", \"SPOUSE\", \"DAUGHTER\", \"SON\", \"NAME\"]","        people = dict()","        should_be = []","        file = []","        nm_flag = False","        ","\t\t#read and strip each line of the file","        for line in in_f:","            file.append(line.strip())","        ","\t\t#place each line to their member","        for i in range(0, len(file)):","            if nm_flag and file[i] not in keywords and file[i] not in people:","                family = looper(i, file, keywords)","               ","                for person in people:","                    tree = people[person]","                    for rel in tree:","                        if len(tree[rel]) >0: ","                            for names in tree[rel]:","                                if names == file[i].upper():","                                    should_be.append([person, rel])","                #check for matches","                for person in should_be:","                    if person[1] == \"FATHER\" or person[1] == \"MOTHER\":","                        if person[0] in family[\"SON\"] or person[0] in family[\"DAUGHTER\"]:","                            should_be.remove([person[0],person[1]])","                    elif person[1] == \"SON\" or person[1] == \"DAUGHTER\":","                        if person[0] in family[\"FATHER\"] or person[0] in family[\"MOTHER\"]:","                            should_be.remove([person[0],person[1]])","                    elif person[1] == \"SPOUSE\":","                        if person[0] in family[\"SPOUSE\"]:","                            should_be.remove([person[0],person[1]])","        ","                if len(should_be) <= 0:                    ","                    people[file[i]] = family","                else:","                    for person in should_be:","                        if person[1] == \"FATHER\" or person[1] == \"MOTHER\":","                            print(person[0] + \" should be \" + file[i].upper() + \"'s son or daughter\")","                        elif person[1] == \"SON\" or person[1] == \"DAUGHTER\":","                            print(person[0] + \" should be \" + file[i].upper() + \"'s mother or father\")","                        elif person[1] == \"SPOUSE\":","                            print(person[0] + \" should be \" + file[i].upper() + \"'s spouse\")","                    print(file[i].upper() + \" will not be added to the database due to inconsistencies in the genealogy.\")","                nm_flag =  False","            else:","                nm_flag = False","            ","\t\t\t#reset the flag if its a new person entry","            if file[i].strip().upper() == \"NAME\":","                nm_flag = True","","        in_f.close()\t\t\t\t\t\t\t\t\t\t\t\t\t\t#close the input file","    return people\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t#return the filled dictionary","","#Add Method-------------------------------------------------------------------------------------------------------------------------------------","#called in add case","def add_person(people):","\t#set the keywords and dictionaries","    keywords = [\"FATHER\",\"MOTHER\", \"SPOUSE\", \"DAUGHTER\", \"SON\"]","    individual = dict()","    family = dict()","    should_be = []","    ","\t#enter the name and check if it exists","    name = input(\"Enter the name of a person: \").strip()","    if name.upper() not in people and name != \"\":","\t\t#if it doesn't exist enter the family","        print (name.upper() + \"'s family:\")","        for keyword in keywords:","            members = []","            member_name = input(\"ENTER \"+ keyword + \"S name: \").strip()","            while member_name != \"\":","                members.append(member_name.upper())","                member_name = input(\"ENTER ANOTHER \" + keyword + \"S NAME: \").strip()","            family[keyword] = members","        ","        for person in people:","            tree = people[person]","            for rel in tree:","                if len(tree[rel]) >0: ","                    for names in tree[rel]:","                        if names == name.upper():","                            should_be.append([person, rel])","        ","        consistency = True","        ","\t\t#check if theres matches","        for person in should_be:","            if person[1] == \"FATHER\" or person[1] == \"MOTHER\":","                if person[0] in family[\"SON\"] or person[0] in family[\"DAUGHTER\"]:","                    should_be.remove([person[0],person[1]])","            elif person[1] == \"SON\" or person[1] == \"DAUGHTER\":","                if person[0] in family[\"FATHER\"] or person[0] in family[\"MOTHER\"]:","                    should_be.remove([person[0],person[1]])","            elif person[1] == \"SPOUSE\":","                if person[0] in family[\"SPOUSE\"]:","                    should_be.remove([person[0],person[1]])","        ","        if len(should_be) <= 0:","            individual[name.upper()] = family","            print(\"\\n\" + name.upper() +\"S FAMILY:\")","            for rel in family:","                print (\"\\n\" + rel.upper())","                print (\"-----------------\")","                for names in family[rel]:","                    print(names)","            ch = input(\"(C) CONFIRM this tree or anything else to reject it: \").upper()","            if ch != \"C\" or ch != \"CONFIRM\":","                individual = False","        else:","            for person in should_be:","                if person[1] == \"FATHER\" or person[1] == \"MOTHER\":","                    print(person[0] + \" should be \" + name.upper() + \"'s son or daughter\")","                elif person[1] == \"SON\" or person[1] == \"DAUGHTER\":","                    print(person[0] + \" should be \" + name.upper() + \"'s mother or father\")","                elif person[1] == \"SPOUSE\":","                    print(person[0] + \" should be \" + name.upper() + \"'s spouse\")","            print(name.upper() + \" will not be added to the database due to inconsistencies in the genealogy.\")","            individual = False","    else:","        print (name.upper() + \" already exists!\")","        individual = False","    return individual","","","#------------------------------------------------------------------------------------------------------","#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ ---  Main ---  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$","#------------------------------------------------------------------------------------------------------","","#list and directory that program runs off of","people = dict()","flag = True","","while flag:","\t#display the commands for the user to enter","    print(\"What would you like to do:\\n\\t(A) ADD a person \\n\\t(L) LOAD a person from a file\")","    print (\"\\t(S) SAVE people to a file \\n\\t(V) VIEW the people described\\n\\t(I) INFORMATION about a person\")","    print (\"\\t(Q) QUIT\\n\")","    ","\t","    selection = input().upper()\t\t\t\t\t\t\t\t\t\t\t\t\t#input to handle the command, capitalized for matching","\t","#Add----------------------------------------------------------------------------------------------------------------------------------------------  ","    if selection == \"A\" or selection == \"ADD\":","        new_person = add_person(people)","        if new_person:","            people = dict(list(new_person.items()) + list(people.items()))\t\t#add to directory if confirmed","        print(\"\\n\")    ","  #Load-------------------------------------------------------------------------------------------------------------------------------------------           ","    elif selection == \"L\" or selection == \"LOAD\":","        temp = load()","        people = dict(list(temp.items()) + list(people.items()))\t\t\t\t#add to directory","        print(\"\\n\")","  #Save-------------------------------------------------------------------------------------------------------------------------------------------      ","    elif selection == \"S\" or selection == \"SAVE\":","        out_f = open_output()","        if out_f:","            for person in people:\t\t\t\t\t\t\t\t\t\t\t\t#write NAME and then the person to the file","                out_f.write(\"NAME\\n\" + person.upper() + \"\\n\")","                tree = people[person]","                for rel in tree:\t\t\t\t\t\t\t\t\t\t\t\t#write the relationship and then the name to the file","                    out_f.write(rel.upper() + \"\\n\")","                    for names in tree[rel]:","                        out_f.write(names+\"\\n\")","            out_f.close()\t\t\t\t\t\t\t\t\t\t\t\t\t\t#close file","        print(\"\\n\")    ","  #View-------------------------------------------------------- ----------------------------------------------------------------------------------    ","    elif selection == \"V\" or selection == \"VIEW\":","        if len(people.keys()) > 0:\t\t\t\t\t\t\t\t\t\t\t\t#printing the people with descibred family's to screen","            print(\"\\nDescribed:\")","            for person in people.keys():","                print(person.upper())","                ","            print(\"\\nReferenced but not yet described:\")\t\t\t\t\t\t#printing the other names entered to the screen","            for person in people:","                tree = people[person]","                for rel in tree:","                    if len(tree[rel]) >0: ","                        for names in tree[rel]:","                            print(names)","            print()","        else:","            print(\"\\nThere are no people in the database!\\n\")","        print(\"\\n\")","\t\t","  #Info--------------------------------------------------------------------------------------------------------------------------------------------       ","    elif selection == \"I\" or selection == \"INFORMATION\":","        if len(people.keys()) > 0:","            flag2 = True","            while flag2:","                print(\"Choose one of the following to get information about:\")\t\t\t\t\t#input for user name ","                for person in people:","                    print(person.upper())","                choice = input(\"\\n\").strip()","","                if choice == \"\":","                    flag2 = False","                else:","                    if choice.strip().upper() in people:\t\t\t\t\t\t\t\t\t\t#if it is in the directory, print the name + family to screen","                        family = people[choice.upper()]","                        print(\"\\nFATHER          MOTHER          SPOUSE          SON             DAUGHTER        \")","                        print(\"-------------------------------------------------------------------------------\")","\t\t\t\t\t\t#place each relation","                        mothers = family[\"MOTHER\"]","                        fathers = family[\"FATHER\"]","                        sons = family[\"SON\"]","                        daughters = family[\"DAUGHTER\"]","                        spouses = family[\"SPOUSE\"]","\t\t\t\t\t\t","\t\t\t\t\t\t#will loop for however many times the max entry is and align each relation in columns","                        for i in range(0,max(len(mothers),len(fathers),len(sons),len(daughters),len(spouses))):","                            try:\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t#print the fathers name then spaces to align columns","                                print (fathers[i], end=\"\")","                                for n in range(0, (16-len(fathers[i]))):","                                    print(\" \", end=\"\")","                            except IndexError: \t\t\t\t\t\t\t\t\t\t\t\t\t#if no father, print 16 spaces","                                print (\"                \",end=\"\")","                            try:","                                print (mothers[i], end=\"\")\t\t\t\t\t\t\t\t\t\t#print the mothers name then spaces to align columns","                                for n in range(0, (16-len(mothers[i]))):","                                    print(\" \", end=\"\")","                            except IndexError: \t\t\t\t\t\t\t\t\t\t\t\t\t#if no mother, print 16 spaces","                                print (\"                \",end=\"\")","                            try:","                                print (spouses[i], end=\"\")\t\t\t\t\t\t\t\t\t\t#print the spouses name then spaces to align columns","                                for n in range(0, (16-len(spouses[i]))):","                                    print(\" \", end=\"\")","                            except IndexError: \t\t\t\t\t\t\t\t\t\t\t\t\t#if no spouse, print 16 spaces","                                print (\"                \",end=\"\")","                            try:","                                print (sons[i], end=\"\")\t\t\t\t\t\t\t\t\t\t\t#print the sons name then spaces to align columns","                                for n in range(0, (16-len(sons[i]))):","                                    print(\" \", end=\"\")  ","                            except IndexError: \t\t\t\t\t\t\t\t\t\t\t\t\t#if no son, print 16 spaces","                                print (\"                \",end=\"\") ","                            try:","                                print (daughters[i], end=\"\")\t\t\t\t\t\t\t\t\t#print the daughters name then spaces to align columns","                                for n in range(0, (16-len(daughters[i]))):","                                    print(\" \", end=\"\")","                            except IndexError: ","                                print (\"                \",end=\"\")  \t\t\t\t\t\t\t\t#if no daughter, print 16 spaces","                            print()","                        print()","                    else:","                        print(choice.upper() + \" is not yet described!\")\t\t\t\t\t\t#output for non-matching input","        else:","            print(\"\\nThere are no people in the database!\\n\")","        print(\"\\n\")","#Quit-----------------------------------------------------------------------------------------------------------------------------------------------    ","    elif selection == \"Q\" or selection == \"QUIT\":","        flag = False\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t#ends loop for main","\t\t","#Invalid--------------------------------------------------------------------------------------------------------------------------------------------","    else:","        print(\"Not a valid command!\\n\")"]},{"action":"insertText","range":{"start":{"row":337,"column":0},"end":{"row":337,"column":13}},"text":"\t\tprint(\"\\n\")"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":337,"column":1},"end":{"row":337,"column":2}},"text":"\t"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":337,"column":0},"end":{"row":337,"column":12}},"text":"\tprint(\"\\n\")"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":336,"column":39},"end":{"row":337,"column":0}},"text":"\n"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":232,"column":20},"end":{"row":232,"column":21}},"text":"p"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":232,"column":21},"end":{"row":232,"column":22}},"text":"r"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":232,"column":21},"end":{"row":232,"column":22}},"text":"r"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":232,"column":21},"end":{"row":232,"column":22}},"text":"e"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":232,"column":22},"end":{"row":232,"column":23}},"text":"o"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":232,"column":23},"end":{"row":232,"column":24}},"text":"p"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":232,"column":24},"end":{"row":232,"column":25}},"text":"l"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":232,"column":25},"end":{"row":232,"column":26}},"text":"e"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":189,"column":15},"end":{"row":189,"column":17}},"text":"ch"},{"action":"insertText","range":{"start":{"row":189,"column":15},"end":{"row":189,"column":85}},"text":"input(\"(C) CONFIRM this tree or anything else to reject it: \").upper()"}]}],[{"group":"doc","deltas":[{"action":"removeLines","range":{"start":{"row":188,"column":0},"end":{"row":189,"column":0}},"nl":"\n","lines":["            ch = input(\"(C) CONFIRM this tree or anything else to reject it: \").upper()"]}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":188,"column":103},"end":{"row":188,"column":110}},"text":"CONFIRM"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":188,"column":102},"end":{"row":188,"column":103}},"text":"\""}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":188,"column":101},"end":{"row":188,"column":102}},"text":" "}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":188,"column":100},"end":{"row":188,"column":101}},"text":"="}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":188,"column":99},"end":{"row":188,"column":100}},"text":"!"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":188,"column":99},"end":{"row":188,"column":100}},"text":"\""}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":188,"column":98},"end":{"row":188,"column":99}},"text":" "}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":188,"column":97},"end":{"row":188,"column":98}},"text":"h"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":188,"column":96},"end":{"row":188,"column":97}},"text":"c"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":188,"column":95},"end":{"row":188,"column":96}},"text":" "}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":188,"column":94},"end":{"row":188,"column":95}},"text":"r"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":188,"column":93},"end":{"row":188,"column":94}},"text":"o"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":188,"column":92},"end":{"row":188,"column":93}},"text":" "}]}]]},"ace":{"folds":[],"scrolltop":3406,"scrollleft":0,"selection":{"start":{"row":188,"column":92},"end":{"row":188,"column":92},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1412798198530,"hash":"8cacb501683f3bb2ab2e0f6e69321a6ec4770d0f"}