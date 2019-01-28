

def findoperator(s):
    if (s.find("+")!=-1):
        #print("let's add!")
        return "+"
    elif (s.find("-")!=-1):
        #print("let's subtract!")
        return "-"
    elif (s.find("*")!=-1):
        #print("let's multiply!")
        return "*"
    elif (s.find("/")!=-1):
        #print("let's divide!")
        return "/"
    else:
        #print("what are you trying to do?")
        return "?"

def findParam1(s):
    op = findoperator(s)
    opIndex = s.find(op)       
    return s[0:opIndex]

def findParam2(s):
    op = findoperator(s)
    opIndex = s.find(op) 
    length = len(s)
    return s[opIndex+1:length]

#executable code

while (True):
    formula = input("what would you like to calculate?")
    op = findoperator(formula)
    
    if (op == "?"):
        print("I don't know what are you trying to calculate!")
    else:
        param1 = findParam1(formula)
        param2 = findParam2(formula)

        param1 = int(param1)
        param2 = int(param2)

        if (op == "+"):
            print(param1 + param2)
        elif (op == "-"):
            print(param1 - param2)
        elif (op == "*"):
            print(param1 * param2)
        elif (op == "/"):
            print(param1 / param2)

        
    



      
