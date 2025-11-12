# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4
print(a) #output 3
print(b) #output 4
print(a==b) #output False

print(a == b)   #Checks for equality # False
print(a != b)   # checks if is not equal # True
print(a > b)    # checks for greater than  # False
print(a < b)    # checks for less than # True
print(a >= b)   # checks for greater than or equal to # False
print(a <= b)   # Checks for less than or equal; to # True


#predict the output of the following comparisons:
10 > 5 #output true
7 == 2 * 3 + 1 #output true
8 != 8 #output False
4 <= 2 + 2 #output true

# Write 3 examples that result in True and 3 that result in False.
7>6 #output true
8 == 2+2 * 2 #ouput true
16 <= 8* 2 #output true

6 != 6 #output false
14 == 7 +5 #output false
5<2 #output false

# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.

# asking student score
score= int(input("what is your score?"))
# make this program for all grading spectrums
# if the score is between 90 -100.. you got an A
# if the score is between 80-89-- you got an B
# if the score is between 70-79 --- you got an C
# if between 61-69 ... you got a D
# if else you failed

# if score >=60:
 #  print("you passed the test")
#   else:
 #  print("you didn't pass")


# & is and operator
# | is
# ~ is not operator



if score >=90 and score <=100:
    print("you got an A and passed!")
elif score >=80 and score <=89:
     print("you got an B and passed!")
elif score >=70 and score <=79:
     print("you got an C")
elif score >=60 and score <=69:
     print(" you got an D")
else:
     print('you failed, come for ACLAB') 

# ask for password
  # password=input("what is your password")
  # The password must be at least 8 characters long
  #  and contain at least one digit.password = "mypassword1"
password =input("what is your passwork?")
if len(password) >= 8 and any (char.isdigit() for char in password):
     print("Password is valid")
else:
     print("Password is invalid." /
           "it must be at least 8 characters long and contain at least one digit.")
     