#simple input from user+output
'''patient=input("What is your name?")
birthYear=input("What is your birth year?")
age=2022-int(birthYear)
isNewPaitent=input("Are you a new patient?")

print('Hello patient, ' ,patient,"age:",age, "new?:",isNewPaitent )
'''

#simple sum of 2 numbers
'''num1=float(input("num1 "))
num2=float(input("num2 "))
res=float(num1+num2)

print('result, ' ,res )
'''

#simple convert weight from L to K and vice verca
'''weight=float(input("Weight "))
type=((input("(K)g or (L)bs ")))
if type.lower()=='l':
    res=float(weight*0.45359237)
    print('Weight in Kg ' ,res )
else:
    res=float(weight/0.45359237)
    print('Weight in bs ' ,res )
'''

#An example of dictionary
'''months={
    1:"January",
    2:"Februaty",
    3:"March"
}

print(months.get(0,"Doesn't exists"))

def raise_to_power(base,pow):
    res=1
    while pow>1:
        res*=base
        pow=pow-1
    return res

print(raise_to_power(2,4))
'''
import usefullTools
usefullTools.hello("Ron")

from main import Person
person1= Person("Mor",22)
print(person1.name,",",person1.age)
