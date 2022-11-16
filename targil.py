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
weight=float(input("Weight "))
type=((input("(K)g or (L)bs ")))
if type.lower()=='l':
    res=float(weight*0.45359237)
    print('Weight in Kg ' ,res )
else:
    res=float(weight/0.45359237)
    print('Weight in bs ' ,res )


