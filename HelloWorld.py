"""print("Hello world, I'm bessie")
print(8 * "\n")
print("end")
f= "Bessiee"
print(f)

name = input("Please enter your name ")
print("my name is", name)

print("I am multiplying")
num1 = int(input("Please enter your first number "))
num2 = int(input("please enter your 2nd number "))

print("Answer is", num1 * num2)

print("I am dividing")
num3 = int(input("pleae enter a number "))
if num3 == 0:
    print("number is 0")

else:
    print("Answer is", num2 / num3)

print("Comparing numbers ")
num5 = int(input("Please enter a number "))
if num5> 0:
    print("The number is greater than zero")

elif num5<0:
    print("The number is less than 0")

else:
    print("The number is zero") """

#Functions
def Hello():
    print("Hello")


def GetInteger():
    num = int(input("Enter an integer "))
    return num

def Cube(x):
    num= int(input(x))
    result = num**3
    return result

def Main():
   """ print("Start")
    Hello()
    print( GetInteger())
    print(Cube("Please enter a number "))

    num7 = int(input("enter a number "))
    for step in range (num7):
        print(step)"""




if __name__=="__main__":
    Main()
