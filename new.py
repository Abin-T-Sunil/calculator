#calculator
def add(x,y):
 return x+y

def sub(x,y):
 return x-y

def multiply(x,y):
 return x*y

def divide(x,y):
 return x/y

print("select operations.")
print("+.Addition")
print("-.subraction")
print("*.multiplication")
print("/.division")

choice=input("enter the choice: ")
num1=float(input("enter the first number: "))
num2=float(input("enter the second number: "))

if choice =="+":
  print(add(num1,num2))
elif choice=="-":
 print(sub(num1,num2))
elif choice=="*":
 print(multiply(num1,num2))
elif choice=="/":
 print(divide(num1,num2))
else:
 print("invalid output")
