num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# greatest common divisor
if(num1>num2):
  n=num1
else:
  n=num2
result=0;
for i in range(n+1):
  if(num1%i==0 and num2%i==0):
    result=i

print("The GCD of", num1, "and", num2, "is", result)
