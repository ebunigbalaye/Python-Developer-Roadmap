#Calcuator that adds, subtracts, multiplies,divides, and calculates factorial
def greeting():
    """This function asks the user for their name and prints out a simple greeting"""
    print("Welcome to Muiz's calculator")
    user_name = input("What's your name ?")
    print(f"Hello {user_name}")
def list(nums):
    """This function returns a list of numbers given a string of numbers seperated by " " as input"""
    nums= nums.split(sep=" ")
    numbers = []
    for i in nums:
        j = int(i)
        numbers.append(j)
    return numbers
def add():
    """This function adds the numbers in a list of numbers and prints out the sum """
    nums =  input("Enter the numbers you want to add seperated by spaces:")
    print(sum(list(nums)))
def subtract():
    """This function returns the result when the first number in a list of number subtracts
    the rest of the numbers in that list."""
    nums =  input("Enter the numbers you want to subtract seperated by spaces:")
    numbers = list(nums)
    for i in range(1,len(numbers)):
        numbers[0] -= numbers[i]
    print (numbers[0])
def multiply():
    """This function multiplies all the numbers entered by the user by converting it 
     into a list of numbers  and prints out the product"""
    nums =  input("Enter the numbers you want to multiply seperated by spaces:")
    numbers = list(nums)
    total = 1
    for num in numbers:
        total *= num
    print(total)
def divide():
    """This function divides the first number entered by the user by the subsquent ones
    and prints out the answer"""
    nums =  input("Enter the numbers you want to divide seperated by spaces:")
    numbers = list(nums)
    total = 1
    for i in range(1,len(numbers)):
        numbers[0] /= numbers[i]
    print (numbers[0])
def factorial():
    """This function calculates the factorial of a number   i.e 5! = 5*4*3*2*1"""
    number = int(input("Enter the number you want to get the factorial of :  "))
    factorial = 1
    if number == 0:
        factorial = 1
    else:
        while number >= 1:
            factorial *= number
            number -=1
    print (factorial)

#Code Execution Block
greeting()
print("What mathematical operation do you want to perform ?")
print("""Enter:
      1 for Addition
      2 for Subtraction
      3 for Multiplication
      4 for Division
      5 for Factorial""")
operation = input ("Enter the number that corresponds to the operation you want to perform: ")
if operation == "1":
    add()
elif operation == "2":
    subtract()
elif operation == "3":
    multiply()
elif operation =="4":
    divide()
elif operation == "5":
    factorial()
else:
    print("Invalid Selection")
