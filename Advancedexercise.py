# Question 1
import math
a = 5
b = 10
c = 7
a = a + 3
print(a)
b = b * 2
print(b)
c = c % 4 
print(c)
sr = math.sqrt (a^2 + b^2 + c^2)
print( "result is","{:.2f}".format(sr))

# Question 2
x = 5
y = 12
z = 6
is_even = (x % 2 == 0)
is_positive = (y > 0)
is_in_range = ((z >= 10) and (z <= 50))
final_condition = ((x % 2 == 0) and (y > 0) and (z >= 10 and z <= 50))
print(final_condition)

# question 3
score = float(input("enter score:"))
apply = score + 5 - 10
final_score = max(100, min(0, apply))
if score >= 90:
  print("grade is A")
elif score >= 80:
  print("grade is B")
elif score >= 70:
  print("grade is C")
elif score >= 60:
  print("grade is D")
elif score <= 50:
  print("grade is F")
print(score)

# question 4
num1 = float(input("enter 1st number: "))
num2 = float(input("enter 2nd number: "))
operation = input("enter a operation(+, -, *, /, %, **):")
if operation == "+":
   result = num1 + num2
   print(round(result, 3))
elif operation == "-":
  result = num1 - num2
  print(round(result, 3))
elif operation == "*":
  result = num1 * num2
  print(round(result, 3))
elif operation == "%":
  result = num1 % num2
  print(round(result, 3))
elif operation == "**":
  result = num1 ** num2
  print(round(result, 3))
elif operation == "/":
  if ( num2==0 ):
   print("cannot divide by zero")
else:
  result = num1 / num2
  print(round(result, 3))