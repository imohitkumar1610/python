# a = input("enter your name ") #but this function allows the user to give input in string format ONLY
# print(a)

# greeting = "good morning"
# name = "mohit"
# print(type(name))
# print(name +" "+ greeting) string concatination
# print(name[4]) asking for a particular cahractor but you can not change any character of any string 
# print(name[0:3]) //this means print the character of that particualr string strating from 0 too 3 characters

# a = input("enter yout name\n")

# print(a, "goodafternoon")

letter = '''Dear <|NAME|>,
you are selected!

date: <|DATE|>'''

name = input("enter your name\n")
date = input("enter date\n")

letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)

print(letter)