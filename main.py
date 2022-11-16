
#Print  range of numbers
def print_range(number):
    for i in range(number):
        print(i)
    num=5

    while num>0:
        print('num',num)
        num=num-1

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    '''print_range(10)'''


print(__name__)
if __name__ != '__main__':
    print_hi("you aren't running main program")
    '''print_hi('PyCharm')'''

print('Enter your name:')
x = input()
print(x in "aron") #checks if the "aron" contains user's name
print('Hello, ' + x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)