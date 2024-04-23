################
# exercise 1

letter = input("pick a litter! ")
vowel = "a", "e", "i", "o", "u"

if letter.lower() in vowel:
    print("it is a vowel letetr")
else:
    print(" it is a constant letetr")

#################
#ex2

integer = float(input("pick a number ? "))

if integer <= 999:
    print("This number is lower than 1000")
elif integer >= 2001:
    print("This numbwe is higher than 2000")
else:
    print("this between 1000 and 2000")

#################
#ex3
num_1 = float(input("pick the 1st ? "))
num_2 = float(input("pick the 2nd number ? "))
num_3 = float(input("pick the 3rd number ? "))

sum_of_num = num_1 + num_2 + num_3 #calculate the sum

if num_1 == num_2 == num_3: #if they are the same it will only calculate
    print("These numbers are the same!")
    print( sum_of_num)
    print("The sum of these numbers multiplied by 4 is:", sum_of_num * 4)
else: #if it is the same it will print the sum 
    print("These numbers are different.", sum_of_num)
    
##########################

# ex3

num_1 = int(input("pick the 1st ? "))
num_2 = int(input("pick the 2nd number ? "))
num_3 = int(input("pick the 3rd number ? "))
num_4 = int(input("pick the 4th number ? "))
biggest_num = max(num_1, num_2, num_3, num_4)
print("the biggest nymber is", biggest_num)

#################
# ex5
income = float(input("What is your income? "))

if income <= 67000: 
    tax_rate = 0.24 # 24% tax will be deducted
elif 67000 < income < 97000:
    tax_rate = 0.31 # 31% tax will be deducted
elif income >= 97000:
    tax_rate = 0.34 # 34% tax will be deducted
else:
    print("Error ! ")

tax = income * tax_rate # calculation operation
net_income = tax - income # calculate the remaing of the net income
print("Your net income is", net_income)

##############################
#ex6


letter = input("Pick a letetr with a maximum size of 5:  ")

if len(letter) == 1:
    print(letter *5) #print the letter 5X
elif len(letter) == 2:
    print(letter[::-1]) #this read it as polidrome
elif len(letter) == 3:
    print(letter[-1] + letter[:2]) #this reorder string
elif len(letter) == 4:
    print(letter[::-1]) #this read it as polidrome
elif len(letter) == 5:
    adding_t = "t".join(letter) #"t" will separate each charecter
    print(adding_t)
else:
    print("Invalid ! The word must be between 1 and 5 characters long. ")


#######################

#ex7



if float(input("What is the value of Pi? ")) != 3.14:
    print("Incorrect answer, end of the test.")
else:
    print("Correct! Next question:") 
    
    if input("What is the capital of the Netherlands? ").lower() != "amsterdam":
        print("Incorrect answer, end of the test.")
    else:
        print("Correct! Next question:")
        
        if input("What is the national animal of the Netherlands? ").lower() != "lion":
            print("Incorrect answer, end of the test.")
        else:
            print("Correct! You answered all the questions :)")

