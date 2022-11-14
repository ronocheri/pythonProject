# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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
    print_range(10)

# Press the green button in the gutter to run the script.
print(__name__)
if __name__ == '__main__':
    print_hi('PyCharm')
