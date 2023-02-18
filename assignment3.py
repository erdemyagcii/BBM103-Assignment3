import sys
f = open(sys.argv[1],"r")
dct = {}
for i in f:
    i = i.split(":")
    (key, value) = (i[0], set(i[1].split()))
    dct[key] = value
f.close()

commands = []
f = open(sys.argv[2],"r")
for line in f :
    commands.append(line.rstrip())
f.close()

f = open("output.txt","w")

def anu(x):
    global dct
    if x not in dct:
        a = {}
        a = set(a)
        dct[x] = a
        f.write("User "+ x + " has been added to the social network successfully\n")
    else:
        f.write("ERROR: Wrong input type! for 'ANU'! -- This user already exists!!\n")

def deu(x):
    global dct
    if x in dct:
        dct.pop(x)
        for i in dct:
            if x in dct[i]:
                dct[i].remove(x)
        f.write("User "+ x +" and his/her all relations have been deleted successfully.\n")
    else:
        f.write("ERROR: Wrong input type! for 'DEU'!--There is no user named "+ x +" !!\n")

def anf(source, target):
    global dct
    if source not in dct and target in dct:
        f.write("ERROR: Wrong input type! for 'ANF'! -- No user named "+ source +" found!!\n")
    elif target not in dct and source in dct:
        f.write("ERROR: Wrong input type! for 'ANF'! -- No user named "+ target +" found!!\n")
    elif (source and target) not in dct:
        f.write("ERROR: Wrong input type! for 'ANF'! -- No user named "+ source +" and " + target +" found!\n")
    elif target in dct[source]:
        f.write("ERROR: A relation between "+ source + " and "+ target + " already exists!!.\n")
    else:
        dct[source].add(target)
        dct[target].add(source)
        f.write("Relation between " + source + " and " + target + " has been added successfully.\n")


def df(source, target):
    global dct
    if source not in dct and target in dct:
        f.write("ERROR: Wrong input type! for 'DEF'! -- No user named "+ source +" found!!\n")
    elif target not in dct and source in dct:
        f.write("ERROR: Wrong input type! for 'DEF'! -- No user named "+ target +" found!!\n")
    elif (source and target) not in dct:
        f.write("ERROR: Wrong input type! for 'DEF'! -- No user named "+ source +" and " + target +" found!\n")
    elif target not in dct[source]:
        f.write("ERROR: No relation between "+ source + " and "+ target + " found!!\n")
    else:
        dct[source].remove(target)
        dct[target].remove(source)
        f.write("Relation between "+ source +  " and "+ target + " has been deleted successfully.\n")

def cf(x):
    if x not in dct:
        f.write("ERROR: Wrong input type! for 'CF'! -- No user named " + x +" found!\n")
    else:
        number = len(dct[x])
        f.write("User " +  x + " has " + str(number) + " friends.\n")

def fpf(x, distance):
    if x not in dct:
        f.write("ERROR: Wrong input type! for 'FPF'! -- No user named " + x + " found!\n") 
    elif distance == 1:
        pos_friends = dct[x]
        f.write("User " + x +" has "+ str(len(dct[x]))+" possible friends when maximum distance is 1\nThese possible friends:")
        first_word = ""
        for w in sorted(pos_friends):
            first_word = first_word.lstrip(" ,") + ", " + w
        f.write("{"+first_word+"}\n")
    elif distance == 2:
        pos_friends = list(dct[x])
        for i in list(dct[x]):
            pos_friends.extend(list(dct[i]))
        pos_friends = set(pos_friends)
        pos_friends.remove(x)
        f.write("User " + x +" has "+ str(len(pos_friends)) +" possible friends when maximum distance is 2\nThese possible friends:")
        first_word = ""
        for w in sorted(pos_friends):
            first_word = first_word.lstrip(" ,") + ", " + w
        f.write("{"+first_word+"}\n")
    elif distance == 3:
        pos_friends = list(dct[x])
        for i in list(dct[x]):
            pos_friends.extend(list(dct[i]))
            for j in list(dct[i]):
                pos_friends.extend(list(dct[j]))
        pos_friends = set(pos_friends)
        pos_friends.remove(x)
        f.write("User " + x +" has "+ str(len(pos_friends)) +" possible friends when maximum distance is 3\nThese possible friends:")
        first_word = ""
        for w in sorted(pos_friends):
            first_word = first_word.lstrip(" ,") + ", " + w
        f.write("{"+first_word+"}\n")
    else:
        f.write("Error about distance!\n")

def sf(x, degree):
    if x not in dct:
        f.write("Error: Wrong input type! for 'SF'! -- No user named " + x +" found!!\n")
    elif not (1 <= degree <= 4):
        f.write("Error: Mutually Degree cannot be less than 1 or greater than 4\n")
    else:
        source_friends = dct[x]
        target_friends = []
        mut1 = []
        mut2 = []
        mut3 = []
        mut4 = []
        for i in source_friends:
            target_friends.extend(list(dct[i]))
        target_friends.sort()
        for j in target_friends:
            a = target_friends.count(j)
            if a == 1:
                mut1.append(j)
            elif a == 2:
                mut2.append(j)
            elif a == 3:
                mut3.append(j)
            else:
                mut4.append(j)
        mut1 = set(mut1)
        mut1.discard(x)
        mut2 = set(mut2)
        mut2.discard(x)
        mut3 = (set(mut3))
        mut3.discard(x)
        mut4 = set(mut4)
        mut4.discard(x)
        
        text_ = []
        if degree == 1:
            f.write("Suggestion List for "+ x + "  when MD is 1:")
            for name in mut1:
                f.write(x +" has 1 mutual friends with " + name+"\n")
                text_.append(name)
            for name in mut2:
                f.write(x +" has 2 mutual friends with " + name+"\n")
                text_.append(name)
            for name in mut3:
                f.write(x +" has 3 mutual friends with " + name+"\n")
                text_.append(name)
            for name in mut3:
                f.write(x +" has 3 mutual friends with " + name+"\n")
                text_.append(name)
            f.write("The suggested friends for "+ x + " :")
            first_word = ",".join(text_)
            f.write("\'"+first_word+"\'\n")
        elif degree == 2:   
            f.write("Suggestion List for "+ x + "  when MD is 2:"+"\n")
            for name in mut2:
                f.write(x +" has 2 mutual friends with " + name+"\n")
                text_.append(name)
            for name in mut3:
                f.write(x +" has 3 mutual friends with " + name+"\n")
                text_.append(name)
            for name in mut4:
                f.write(x +" has 4 mutual friends with " + name+"\n")
                text_.append(name)
            f.write("The suggested friends for "+ x + " :")
            first_word = ",".join(text_)
            f.write("\'"+first_word+"\'\n")
        elif degree == 3:
            f.write("Suggestion List for "+ x + "  when MD is 3:"+"\n")
            for name in mut3:
                f.write(x +" has 3 mutual friends with " + name+"\n")
                text_.append(name)
            for name in mut4:
                f.write(x +" has 4 mutual friends with " + name+"\n")
                text_.append(name)
            f.write("The suggested friends for "+ x + " :")
            first_word = ",".join(text_)
            f.write("\'"+first_word+"\'\n")
        else:
            f.write("Suggestion List for "+ x + "  when MD is :"+"\n")
            for name in mut4:
                f.write(x +" has 4 mutual friends with " + name+"\n")
                text_.append(name)
            f.write("The suggested friends for "+ x + " :")
            first_word = ",".join(text_)
            f.write("\'"+first_word+"\'\n")
                   
for command in commands:
    command = command.split()
    cmd = command[0]
    parameter1 = command[1]
    if cmd == "ANU":
        anu(parameter1)
    elif cmd == "DEU":
        deu(parameter1)
    elif cmd == "ANF":
        parameter2 = command[2]
        anf(parameter1, parameter2)
    elif cmd == "DEF":
        parameter2 = command[2]
        df(parameter1, parameter2)
    elif cmd == "CF":
        cf(parameter1)
    elif cmd == "FPF":
        parameter2 = command[2]
        fpf(parameter1, int(parameter2))
    else:
        parameter2 = command[2]
        sf(parameter1, int(parameter2))

f.close()














    














    

        




