import random


#list of numbers for program to choose from
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#list of letters for program to choose from 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
'U', 'V', 'W', 'X', 'Y', 'Z'
]
#list of letters for program to choose from 
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

#takes quantity of how many of each type of character the user wants
#turns into integer for program
nr_numbers = int(input("How many numbers would you like? "))
nr_letters = int(input("How many letters would you like? "))
nr_symbols = int(input("How many symbols would you like? "))

#blank list for program to append characters to 
password_list = []

#for each integer the character inputs in the previous step it takes that
#and creates a for loop between a range of 0 and what the user inputs 

for char in range(1, nr_letters + 1):

    password_list.append(random.choice(letters))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

    print(password_list)
    random.shuffle(password_list)
    print(password_list)


password = ""
for char in password_list:
    password += char

print(f"Your password is: {password} ")




    

