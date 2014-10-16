#######################################################
### Group 3: Nick Pezza and Kevin Flavin			###
### CSC 485 Special Topics in Computer Science		###
### Dr. Pyzdrowski - MW 4:00pm - 5:15pm				###
### Python Program 3 - Word Count Program    		###
#######################################################

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
        choice = input("Overwrite(1), pick a different file(2), or quit(3)? ")  # asks if user wants to overwrite, pick dif, or quit
        if choice == "1":
            o_file = open(o_name, "w")                                          # overwrites file and exits loop
            flag = False
        elif choice == "2":
            o_name = input("Whats the name of the output file? ")               # asks for new file name
        elif choice == "3":
            flag = False                                                        # exits loop
    if flag:                                                                # if not overwrite or quit
        o_file = open(o_name, "w")
    else:
        if not o_file:                                                          # if quit 
            o_file = False
    return o_file                                           

import os

i_name = open_input()                                                           # gets the name of the input file
if i_name:                                                                      # if the user didnt quit continue 
    with open(i_name, "r") as input_file:                                       # reads in the entire file to variable whole
        whole = input_file.read()
    
    i_file = open(i_name, "r")                                                  # opens input file for reading 
    
    # inits variables for word searching
    word_array = []
    num_a = []
    
    # loops through the file line by line
    for line in i_file:
        flag = False                                                            # inits flag 
        words = line.replace(","," ").split()                                   # splits sentence into a list of words
        for word in words:                                                      # loops through all the words in the word list 
            try:
                float(word)                                                     # tests if the "word" is a number
                num_a.append(word)                                              # if it is adds to number array
            except ValueError:                                                  # if not a number i.e. a word
                word = word.strip('\t,~`!@^&*()\n#$%_+=<>?/\|}{[]:;"')                              # strips off random characters from the front and back
                flag = False                    
                for array in word_array:                                        # runs through current word array to check duplicates
                    if word in array[0]:                                        # if word already occured increment count and set flag
                        flag = True
                        array[1] += 1
            
                if not flag:                                                    # if word doesnt exist add it to word array
                    word_array.append([word.strip('\t,~`!@^&*()\n#$%_+=<>?/\|}{[]:;"'), 1 ])
    
    i_file.close()                                                              # closes the input file
    
    o_file = open_output()                                                      # opens the output file
    if o_file:                                                                  # if the user didnt quit continue on
        o_file.write("*** Original File ***\n\n"+whole+"\n\n*** Word Count ***\n\n") # prints header and input file
        
        for array in word_array:                                                # loops through word array and prints word and count
            o_file.write(str(array[0]) + " - " + str(array[1]) + "\n")
        o_file.write("\n*** Alphabetic List ***\n\n")                           # prints header
        for array in sorted(word_array,key=lambda x: x[0].lower()):             # loops through sorted word array and reprints
            o_file.write(str(array[0]) + " - " + str(array[1]) + "\n")
        o_file.write("\n*** Numbers ***\n\n")                                   # prints header
        for num in num_a:                                                       # prints the numbers by occurance
          o_file.write(str(num)+'\n')
        o_file.write("\n")  
        for num in num_a:                                                       # concatenates all the numbers together 
          o_file.write(str(num))        
        o_file.close()                                                          # closes output file