#Armstrong Number
num=int(input("Enter a number: "))

print("1.Prime or not \n2.Armstrong \n3.Odd or Even \n4.Factorial")
choice=int(input("Select Operation : "))

if choice==1:
  if num<=1:
      print(num," is not a prime number")
  else:
    for i in range(2,num):
      if(num%i)==0:
        print(num,"is not a prime number")
        break
    else:
        print(num,"is a prime number")
  
elif choice==2:
    
    sum=0
    temp=num
    n=len(str(num))
    while temp>0:
      digit=temp%10
      sum+=digit**3
      temp//=10

    if sum == num:
      print(num,"is Armstrong number")
    else:
      print(num,"is not Armstrong number")

elif choice==3:

  if (num%2)==0:
    print(num,"is even")
  else:
    print(num,"is odd")

elif choice==4:
  result=1
  if num<0:
    print("Invalid")
  else:
    for i in range(num,0,-1):
      result = result*i
    print(f"Factorial of {num} is: {result}")


else:
    print("Wrong choice")


  

    
