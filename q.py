def checkInputType(uinput):
    try:
        int(uinput)
        print("You entered an integer")
        return
    except:
        try:
            float(uinput)
            print("You Entered a Float")
            return
        except:
            print("You entered a String.")
            return
    



name = input("Please Enter Your Name ")
age = input("Please Enter Your Age ")

print(f"Hello {name}, you are {age} years old.")

dataType = input("Enter Something ")
checkInputType(dataType)


Fawwaz = ['Hello', 'My','Name','Is']
print(Fawwaz)
Fawwaz.append('Fawwaz')
print(Fawwaz)
Fawwaz.remove('Fawwaz')

for chocu in Fawwaz:
    print(chocu.upper())
    

myTuple = (0,1,2,3)
print(myTuple)
firstElement = myTuple[0]
secondElement = myTuple[1]
print(firstElement)
print(secondElement)


myDict = {
    "Fawwaz": "2.0cgpa",
    "Faraz": "4.0cgpa",
    "Arbab": "2.5cgpa",
    "Ibbi": "3.0cgpa",
    "Talha": "2.5cgpa"
}
print(myDict)


listOne = []
listTwo = []

for fawwaz in range (5):
    listOne.append(int(input(f"Enter Int #{fawwaz+1} for first list")))
    
for fawwaz in range (5):
    listTwo.append(int(input(f"Enter Int #{fawwaz+1} for second list")))
    

setOne = set(listOne)
setTwo = set(listTwo)
print(type(setOne))
print(setOne.union(setTwo))
print(setOne.intersection(setTwo))
print(setOne.difference(setTwo))


numCheck = int(input("Bhai jan enter a num again: "))

if numCheck >0:
    print("num is greater than zero")
elif numCheck<0:
    print("num is smaller than zero")
else:
    print("num is zero")
if numCheck % 2 == 0:
    print("num is even")
else:
    print("num is odd")
    
    
    
for fawwaz in range(1,50):
    if fawwaz %3 ==0 and fawwaz %5 != 0:
        print("Fizz")
    if fawwaz %5 ==0 and fawwaz %3 != 0:
        print("Buzz")
    if fawwaz %3 ==0 and fawwaz %5 == 0:
        print("FizzBuzz")

def calcFact():
    factint = int(input("Enter int for factorial calc"))
    
    ans = 1
    
    while(factint != 0):
        ans = ans*factint
        factint-= 1
    print(ans)
        
calcFact()



def checkPrime(num):
    prime = 1
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            prime = 0
            break
    if prime == 1 and num != 1:
        print("Number is prime")
    else:
        print("Number is composite")    
    
        
checkPrime(int(input("Enter number to check for prime"))   )   
 
        
def squareList():
    myList = []
    for i in range(5):
        myList.append(int(input("Enter int")))
    print(myList)
    newList = [x*x for x in myList]
    print(newList)
    
squareList()


def mergeDicts():
    d1 = {'x': 1, 'y': 2}
    d2 = {'y': 3, 'z': 4}

    d1.update(d2)
    print(d1)

mergeDicts()


def removeDuplicate():
    a = [1, 2, 2, 3, 4, 4, 5]
    a = list(set(a))
    print(a)
    
removeDuplicate()
    
 def isPalindrome(s):
    return s == s[::-1]


isPalindrome("bob")

def fibonaci(n):
    num1 = 0
    num2 = 1
    next_number = num2  
    count = 1

    while count <= n:
        print(next_number, end=" ")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2


def averageCalc():
    sum = 0
    count = int(input("Enter the count of numbers"))
    for i in range(count):
        num = input("Enter number")
        sum = sum + num
    print(sum/count)
    
    
def multiplication():
       
    for i in range (1,11):
        num = 0
        for j in range(i*10):
            num = num+1
        print(num)
multiplication()        


global username
global password
def register():
    global username
    username = input("Enter username")
    global password
    password = input("Enter password")
    
def login():
    global username
    global password
    if input("Enter username") == username and input("Enter password") == password:
        print("Valid")
    else:
        print("Invalid")
        
register()
login()


def countFrequency():
    mydict = {}
    n = int(input("Enter num of entries"))
    for _ in range(n):
        key = input("Enter key")
        if key in mydict:
            value = mydict[key] + 1
        else:
            value = 1
        mydict.update({key:value})
    print(mydict)
countFrequency()


def tempConverter():
    choice = input("Convert to Celsius(0) or Convert to Fahrenheit(1)?")
    if choice == '0':
        inp = float(input("Enter temp in Fahrenheit"))
        print((inp-32) * 5/9)
    elif choice == '1':
        inp = float(input("Enter temp in Celsius"))
        print((inp * 9/5) + 32)
        

tempConverter()