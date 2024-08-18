def calculator():
    while True:
     choise = int(input("What your choise ? choose one of the choises:\n.1 Addition\n.2 Subration\n.3 Multiplication\n.4 Devision\n.5 Exponenntation\n.6 Floor\n.7 Exit\n:"))
     if choise == 7:
        break
     if choise== 1:
        a = float(input("Enter number one: "))
        b = float(input("Enter number two: "))
        result = Addition(a,b)
        print(result)
    
     elif choise == 2:
        a = float(input("Enter number one:"))
        b = float(input("Enter number two:"))
        result = Subration(a,b)
        print(result)

     elif choise == 3:
        a = float(input("Enter number one:"))
        b = float(input("Enter number two:"))
        result = Multiplacation(a,b)
        print(result)

     elif choise == 4:
        a = float(input("Enter number one:"))
        b = float(input("Enter number two:"))
        if b == 0:
           print("you can't division by 0")
           break
        result = Division(a,b)
        print(result)

     elif choise == 5:
        a = int(input("Enter number one:"))
        b = int(input("Enter number of power:"))
        result = Exponenntation(a,b)
        print(result)
     elif choise == 6:
        a = int(input("Enter number one:"))
        b = int(input("Enter number two:"))
        if b == 0:
           print("you can't division by 0")
           break
        result = Floor(a,b)
        print(result)
        
     else:
        print("Error you must right one of those choises(1,2,3,4,5,6,7)\n")
    
def Addition(a,b):
    return a+b

def Subration(a,b):
    return a-b

def Multiplacation(a,b):
    return a*b

def Division(a,b):
    return a/b

def Exponenntation(a,b):
    return a**b

def Floor (a,b):
   return a//b

calculator()