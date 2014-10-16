def editPerson(people):
    keywords = ["FATHER","MOTHER", "SPOUSE", "DAUGHTER", "SON", "NAME"]
    
    quit = False

    while not quit:
        print("Choose one of the following to edit:")
        for key in list(people.keys()):
            print(key.title())
        flag = True
        
        while flag:
            person = input("\n").strip().upper()
            if person == "":
                quit = True
                flag = False
            elif person in people:
                flag = False
        go_back = False
        
        while not quit and not go_back:
            family = people[person]
            print("\nFATHER          MOTHER          SPOUSE          SON             DAUGHTER        ")
            print("-------------------------------------------------------------------------------")
            mothers = family["MOTHER"]
            fathers = family["FATHER"]
            sons = family["SON"]
            daughters = family["DAUGHTER"]
            spouses = family["SPOUSE"]
            for i in range(0,max(len(mothers),len(fathers),len(sons),len(daughters),len(spouses))):
                try:
                    print (fathers[i].title(), end="")
                    for n in range(0, (16-len(fathers[i]))):
                        print(" ", end="") 
                except IndexError: 
                    print ("                ",end="")
                try:
                    print (mothers[i].title(), end="")
                    for n in range(0, (16-len(mothers[i]))):
                        print(" ", end="")
                except IndexError: 
                    print ("                ",end="")
                try:
                    print (spouses[i].title(), end="")
                    for n in range(0, (16-len(spouses[i]))):
                        print(" ", end="")
                except IndexError: 
                    print ("                ",end="")
                try:
                    print (sons[i].title(), end="")
                    for n in range(0, (16-len(sons[i]))):
                        print(" ", end="")  
                except IndexError: 
                    print ("                ",end="") 
                try:
                    print (daughters[i].title(), end="")
                    for n in range(0, (16-len(daughters[i]))):
                        print(" ", end="")
                except IndexError: 
                    print ("                ",end="")  
                print()
            print()

            print("\nWhat edit function would you like to perform on " + person.title() + ":")
            print("\t(A) ADD a person\n\t(D) DELETE a person\n\t(C) CHANGE a persons name")
            
            fxn_flag = True
            while fxn_flag:
                fxn_choice = input("").strip().upper()
                if fxn_choice == "":
                    go_back = True
                    fxn_flag = False
                elif fxn_choice in ["A","ADD","D","DELETE","C","CHANGE"]:
                    fxn_flag = False
            
            if not go_back:
                if fxn_choice == "A" or fxn_choice == "ADD":
                    add_flag = True
                    while add_flag:
                        add_person = input("What's the name of the person you want to add: ").strip().upper()
                        if add_person != "":
                            add_flag = False
                    add_flag = True
                    while add_flag:
                        add_relation = input("What relation does " + add_person.title() + " have to " + person.title() + ": ").strip().upper()
                        if add_relation in ["FAHTER","MOTHER","SON","DAUGHTER","SPOUSE"]:
                            add_flag = False
                    if input("Add " + add_person.title() + " as " + person.title() + "'s "+ add_relation.lower() + "?(yes/no)").upper() =="YES":
                        family = people[person][add_relation]
                        family.append(add_person)
                        people[person][add_relation] = family
                        go_back = True
                    else:
                        print("Addition aboted. Going back.")
                        go_back = True
                        
                elif fxn_choice == "D" or fxn_choice == "DELETE":
                    delete_flag = True
                    while delete_flag:
                        delete_person = input("What's the name of the person you want to delete: ").strip().upper()
                        if delete_person != "":
                            delete_flag = False
                    
                    tree = people[person]
                    members = []
                    for rel in tree.values():
                        for human in rel:
                            members.append(human)
                    if delete_person in members:
                        if input("Delete " + delete_person.title() + " from " + person.title() + " genealogy?(yes/no)").upper() =="YES":
                            for rel in tree:
                                if delete_person in tree[rel]:
                                    tree[rel].remove(delete_person)
                                    people[delete_person][rel] = tree[rel]
                                    go_back = True
                        else:
                            print("Deletion aboted. Going back.")
                            go_back = True
                    else:
                        print(delete_person.title() + " does not exist. Deletion aboted. Going back.")
                        go_back = True
                elif fxn_choice == "C" or fxn_choice == "CHANGE":
                    ch_flag = True
                    while ch_flag:
                        ch_person = input("What's the name of the person you want to change: ").strip().upper()
                        if ch_person != "":
                            ch_flag = False
                    
                    tree = people[person]
                    members = []
                    for rel in tree.values():
                        for human in rel:
                            members.append(human)
                    members.append(person)
                    if ch_person in members:
                        ch_flag = True
                        while ch_flag:
                            ch_name = input("What's the new name for " + ch_person.title() + ": ").strip().upper()
                            if ch_name != "":
                                ch_flag = False
                        if input("Change " + ch_person.title() + " to " + ch_name.title() + "?(yes/no)").upper() =="YES":
                            if person == ch_person:
                                del people[person]
                                people[ch_name] = tree
                                go_back = True
                            else:
                                for rel in tree:
                                    if ch_person in tree[rel]:
                                        tree[rel].remove(ch_person)
                                        tree[rel].append(ch_name)
                                        people[ch_person][rel] = tree[rel]
                                        go_back = True
                        else:
                            print("Change aboted. Going back.")
                            go_back = True
                    else:
                        print(ch_person.title() + " does not exist. Change aboted. Going back.")
                        go_back = True

    return people

def getFather(tree, people):
    fathers = []
    for person in people:
        try:
            fathers += (tree[person.upper()]["FATHER"])
        except KeyError:
            pass
    return fathers
    
def getMother(tree, people):
    mothers = []
    for person in people:
        try:
            mothers += (tree[person.upper()]["MOTHER"])
        except KeyError:
            pass
    return mothers
    
def getParents(tree, people):
    parents = []
    for person in people:
        try:
            parents += (tree[person.upper()]["FATHER"]) + (tree[person.upper()]["MOTHER"])
        except KeyError:
            pass
    return parents

def getSons(tree, people):
    sons = []
    for person in people:
        try:
            sons += (tree[person.upper()]["SON"])
        except KeyError:
            pass
    return sons
    
def getDaughters(tree, people):
    daughters = []
    for person in people:
        try:
            daughters += (tree[person.upper()]["DAUGHTER"])
        except KeyError:
            pass
    return daughters

def getChildren(tree, people):
    children = []
    for person in people:
        try:
            children += (tree[person.upper()]["SON"]) + (tree[person.upper()]["DAUGHTER"])
        except KeyError:
            pass
    return children

def getUncles(tree, people):
    bio_uncles = getSons(tree, getParents(tree,getParents(tree, people)))
    spo_uncles = getDaughters(tree, getParents(tree,getParents(tree, people)))
    for aunt in spo_uncles:
        try:
            bio_uncles += tree[aunt]["SPOUSE"]
        except KeyError:
            pass
    parents = getParents(tree, people)
    uncles = set(bio_uncles)
    for parent in parents:
        try:
            uncles.remove(parent)
        except KeyError:
            pass
    return uncles

def getAunts(tree, people):
    bio_aunts = getDaughters(tree, getParents(tree,getParents(tree, people)))
    spo_aunts = getSons(tree, getParents(tree,getParents(tree, people)))
    for uncle in spo_aunts:
        try:
            bio_aunts += tree[uncle]["SPOUSE"]
        except KeyError:
            pass
    parents = getParents(tree, people)
    aunts = set(bio_aunts)
    for parent in parents:
        try:
            aunts.remove(parent)
        except KeyError:
            pass
    return aunts
    
def relationships(people):
    keywords = ["GF","GM","GP","F","M","P","B","SIS","SIB","S","D","C","GS","GD","GC","U","A","CO","NE","NI"]
    quit = False

    while not quit:
        print("Choose one of the following to inquire about:")
        for key in list(people.keys()):
            print(key.title())
        flag = True
        
        while flag:
            person = input("\n").strip().upper()
            if person == "":
                quit = True
                flag = False
            elif person in people:
                flag = False
        go_back = False
        while not quit and not go_back:
            print("Choose a relationship: ")
            print("\tGF Grandfathers\n\tGM Grandmothers\n\tGP Grandparents\n\tF Fathers")
            print("\tM Mothers\n\tP Parents\n\tB Brothers\n\tSis Sisters\n\tSib Siblings")
            print("\tS Sons\n\tD Daughters\n\tC Children\n\tGS Grandsons\n\tGD Granddaughters")
            print("\tGC Grandchildren\n\tU Uncles\n\tA Aunts\n\tCo Cousins\n\tNe Nephews\n\tNi Nieces")
            
            flag = True
            go_back = False
            while flag:
                choice = input("\n").strip().upper()
                if choice in keywords:
                    flag = False
                if choice == "":
                    go_back = True
                    flag = False
            
            if not go_back:
                if choice == "GF":
                    gr_fathers = getFather(people,getParents(people, [person]))
                    if len(gr_fathers) == 0:
                        print("\n" + person.title() + " has no grandfathers.\n")
                    else:
                        if len(gr_fathers) > 1:
                            print("\n" + person.title() + "'s grandfather's are ", end="")
                        else:
                            print("\n" + person.title() + "'s grandfather is ", end="")
                        for i in range(len(gr_fathers)):
                            print(gr_fathers[i].title(), end="")
                            if i < (len(gr_fathers)-1):
                                print(" and ", end="")
                            else:
                                print(".\n")
                elif choice == "GM":
                    gr_mothers = getMother(people,getParents(people, [person]))
                    if len(gr_mothers) == 0:
                        print("\n" + person.title() + " has no grandmothers.\n")
                    else:
                        if len(gr_mothers) > 1:
                            print("\n" + person.title() + "'s grandmother's are ", end="")
                        else:
                            print("\n" + person.title() + "'s grandmother is ", end="")
                        for i in range(len(gr_mothers)):
                            print(gr_mothers[i].title(), end="")
                            if i < (len(gr_mothers)-1):
                                print(" and ", end="")
                            else:
                                print(".\n")
                elif choice == "GP":
                    gr_par = getParents(people,getParents(people, [person]))
                    if len(gr_par) == 0:
                        print("\n" + person.title() + " has no grandparents.\n")
                    else:
                        if len(gr_par) > 1:
                            print("\n" + person.title() + "'s grandparent's are ", end="")
                        else:
                            print("\n" + person.title() + "'s grandparent is ", end="")
                        for i in range(len(gr_par)):
                            print(gr_par[i].title(), end="")
                            if i < (len(gr_par)-1):
                                print(" and ", end="")
                            else:
                                print(".\n")
                elif choice == "F":
                    fathers = getFather(people, [person])
                    if len(fathers) == 0:
                        print("\n" + person.title() + " has no fathers.\n")
                    else:
                        if len(fathers) > 1:
                            print("\n" + person.title() + "'s father's are ", end="")
                        else:
                            print("\n" + person.title() + "'s father is ", end="")
                        for i in range(len(fathers)):
                            print(fathers[i].title(), end="")
                            if i < (len(fathers)-1):
                                print(" and ", end="")
                            else:
                                print(".\n")
                elif choice == "M":
                    mothers = getMother(people, [person])
                    if len(mothers) == 0:
                        print("\n" + person.title() + " has no mothers.\n")
                    else:
                        if len(mothers) > 1:
                            print("\n" + person.title() + "'s mother's are ", end="")
                        else:
                            print("\n" + person.title() + "'s mother is ", end="")
                        for i in range(len(mothers)):
                            print(mothers[i].title(), end="")
                            if i < (len(mothers)-1):
                                print(" and ", end="")
                            else:
                                print(".\n")
                elif choice == "P":
                    parents = getParents(people, [person])
                    if len(parents) == 0:
                        print("\n" + person.title() + " has no parents.\n")
                    else:
                        if len(parents) > 1:
                            print("\n" + person.title() + "'s parent's are ", end="")
                        else:
                            print("\n" + person.title() + "'s parent is ", end="")
                        for i in range(len(parents)):
                            print(parents[i].title(), end="")
                            if i < (len(parents)-1):
                                print(" and ", end="")
                            else:
                                print(".\n")
                elif choice == "B":
                    bros = getSons(people, getParents(people, [person]))
                    new_bros = set(bros)
                    try:
                        new_bros.remove(person)
                    except KeyError:
                        print("", end="")
                    bros = list(new_bros)
                    
                    if len(bros) == 0:
                        print("\n" + person.title() + " has no brothers.\n")
                    else:
                        if len(bros) > 1:
                            print("\n" + person.title() + "'s brothers are ", end="")
                        else:
                            print("\n" + person.title() + "'s brother is ", end="")
                        for i in range(len(bros)):
                            print(bros[i].title(), end="")
                            if i < (len(bros)-1):
                                print(" and ", end="")
                            else:
                                print(".\n")              
                elif choice == "SIS":
                    siss = getDaughters(people, getParents(people, [person]))
                    new_siss = set(siss)
                    try:
                        new_siss.remove(person)
                    except KeyError:
                        print("", end="")
                    siss = list(new_siss)
                    
                    if len(siss) == 0:
                        print("\n" + person.title() + " has no sisters.\n")
                    else:
                        if len(siss) > 1:
                            print("\n" + person.title() + "'s sisters are ", end="")
                        else:
                            print("\n" + person.title() + "'s sister is ", end="")
                        for i in range(len(siss)):
                            print(siss[i].title(), end="")
                            if i < (len(siss)-1):
                                print(" and ", end="")
                            else:
                                print(".\n")                    
                elif choice == "SIB":
                    sibs = getDaughters(people, getParents(people, [person])) + getSons(people, getParents(people, [person]))
                    new_sibs = set(sibs)
                    try:
                        new_sibs.remove(person)
                    except KeyError:
                        print("", end="")
                    sibs = list(new_sibs)

                    if len(sibs) == 0:
                        print("\n" + person.title() + " has no siblings.\n")
                    else:
                        if len(sibs) > 1:
                            print("\n" + person.title() + "'s siblings are ", end="")
                        else:
                            print("\n" + person.title() + "'s sibling is ", end="")
                        for i in range(len(sibs)):
                            print(sibs[i].title(), end="")
                            if i < (len(sibs)-1):
                                print(" and ", end="")
                            else:
                                print(".\n") 
                elif choice == "S":
                    sons = getSons(people, [person])
                    if len(sons) == 0:
                        print("\n" + person.title() + " has no sons.\n")
                    else:
                        if len(sons) > 1:
                            print("\n" + person.title() + "'s sons are ", end="")
                        else:
                            print("\n" + person.title() + "'s son is ", end="")
                        for i in range(len(sons)):
                            print(sons[i].title(), end="")
                            if i < (len(sons)-1):
                                print(" and ", end="")
                            else:
                                print(".\n")
                elif choice == "D":
                    daughters = getDaughters(people, [person])
                    if len(daughters) == 0:
                        print("\n" + person.title() + " has no daughters.\n")
                    else:
                        if len(daughters) > 1:
                            print("\n" + person.title() + "'s daughters are ", end="")
                        else:
                            print("\n" + person.title() + "'s daughter is ", end="")
                        for i in range(len(daughters)):
                            print(daughters[i].title(), end="")
                            if i < (len(daughters)-1):
                                print(" and ", end="")
                            else:
                                print(".\n")
                elif choice == "C":
                    children = getChildren(people, [person])
                    if len(children) == 0:
                        print("\n" + person.title() + " has no children.\n")
                    else:
                        if len(children) > 1:
                            print("\n" + person.title() + "'s children are ", end="")
                        else:
                            print("\n" + person.title() + "'s child is ", end="")
                        for i in range(len(children)):
                            print(children[i].title(), end="")
                            if i < (len(children)-1):
                                print(" and ", end="")
                            else:
                                print(".\n")
                elif choice == "GS":
                    g_sons = getSons(people, getChildren(people, [person]))
                    if len(g_sons) == 0:
                        print("\n" + person.title() + " has no grandsons.\n")
                    else:
                        if len(g_sons) > 1:
                            print("\n" + person.title() + "'s grandsons are ", end="")
                        else:
                            print("\n" + person.title() + "'s grandson is ", end="")
                        for i in range(len(g_sons)):
                            print(g_sons[i].title(), end="")
                            if i < (len(g_sons)-1):
                                print(" and ", end="")
                            else:
                                print(".\n")
                elif choice == "GD":
                    g_daught = getDaughters(people, getChildren(people, [person]))
                    if len(g_daught) == 0:
                        print("\n" + person.title() + " has no granddaughters.\n")
                    else:
                        if len(g_daught) > 1:
                            print("\n" + person.title() + "'s granddaughters are ", end="")
                        else:
                            print("\n" + person.title() + "'s granddaughter is ", end="")
                        for i in range(len(g_daught)):
                            print(g_daught[i].title(), end="")
                            if i < (len(g_daught)-1):
                                print(" and ", end="")
                            else:
                                print(".\n")
                elif choice == "GC":
                    g_child = getChildren(people, getChildren(people, [person]))
                    if len(g_child) == 0:
                        print("\n" + person.title() + " has no grandchildren.\n")
                    else:
                        if len(g_child) > 1:
                            print("\n" + person.title() + "'s grandchildren are ", end="")
                        else:
                            print("\n" + person.title() + "'s grandchild is ", end="")
                        for i in range(len(g_child)):
                            print(g_child[i].title(), end="")
                            if i < (len(g_child)-1):
                                print(" and ", end="")
                            else:
                                print(".\n")
                elif choice == "U":
                    uncles = getUncles(people, [person])
                    if len(uncles) == 0:
                        print("\n" + person.title() + " has no uncles.\n")
                    else:
                        if len(uncles) > 1:
                            print("\n" + person.title() + "'s uncles are ", end="")
                        else:
                            print("\n" + person.title() + "'s uncle is ", end="")
                        for i in range(len(uncles)):
                            print(uncles[i].title(), end="")
                            if i < (len(uncles)-1):
                                print(" and ", end="")
                            else:
                                print(".\n")
                elif choice == "A":
                    aunts = getAunts(people, [person])
                    if len(aunts) == 0:
                        print("\n" + person.title() + " has no aunts.\n")
                    else:
                        if len(aunts) > 1:
                            print("\n" + person.title() + "'s aunts are ", end="")
                        else:
                            print("\n" + person.title() + "'s aunt is ", end="")
                        for i in range(len(aunts)):
                            print(aunts[i].title(), end="")
                            if i < (len(aunts)-1):
                                print(" and ", end="")
                            else:
                                print(".\n")
                elif choice == "CO":
                    par_sib = list(getAunts(people, [person])) + list(getUncles(people, [person]))
                    cousins = getChildren(people, par_sib)
                    cousins = list(set(cousins))
                    
                    if len(cousins) == 0:
                        print("\n" + person.title() + " has no cousins.\n")
                    else:
                        if len(cousins) > 1:
                            print("\n" + person.title() + "'s cousins are ", end="")
                        else:
                            print("\n" + person.title() + "'s cousin is ", end="")
                        for i in range(len(cousins)):
                            print(cousins[i].title(), end="")
                            if i < (len(cousins)-1):
                                print(" and ", end="")
                            else:
                                print(".\n")
                elif choice == "NE":
                    sibs = getDaughters(people, getParents(people, [person])) + getSons(people, getParents(people, [person]))
                    sp_sibs = getDaughters(people, getParents(people, people[person]["SPOUSE"])) + getSons(people, getParents(people, people[person]["SPOUSE"]))
            
                    new_sibs = set(sibs + sp_sibs)
            
                    try:
                        new_sibs.remove(person)
                        for spouse in people[person]["SPOUSE"]:
                            new_sibs.remove(spouse)
                    except KeyError:
                        print("", end="")
                    
                    nephs = getSons(people, list(new_sibs))

                    if len(nephs) == 0:
                        print("\n" + person.title() + " has no nephews.\n")
                    else:
                        if len(nephs) > 1:
                            print("\n" + person.title() + "'s nephews are ", end="")
                        else:
                            print("\n" + person.title() + "'s nephew is ", end="")
                        for i in range(len(nephs)):
                            print(nephs[i].title(), end="")
                            if i < (len(nephs)-1):
                                print(" and ", end="")
                            else:
                                print(".\n")
                        
                elif choice == "NI":
                    sibs = getDaughters(people, getParents(people, [person])) + getSons(people, getParents(people, [person]))
                    sp_sibs = getDaughters(people, getParents(people, people[person]["SPOUSE"])) + getSons(people, getParents(people, people[person]["SPOUSE"]))
                    
                    new_sibs = set(sibs + sp_sibs)
                    try:
                        new_sibs.remove(person)
                        for spouse in people[person]["SPOUSE"]:
                            new_sibs.remove(spouse)
                    except KeyError:
                        print("", end="")
                   
                    nieces = getDaughters(people, list(new_sibs))

                    if len(nieces) == 0:
                        print("\n" + person.title() + " has no nieces.\n")
                    else:
                        if len(nieces) > 1:
                            print("\n" + person.title() + "'s nieces are ", end="")
                        else:
                            print("\n" + person.title() + "'s niece is ", end="")
                        for i in range(len(nieces)):
                            print(nieces[i].title(), end="")
                            if i < (len(nieces)-1):
                                print(" and ", end="")
                            else:
                                print(".\n")