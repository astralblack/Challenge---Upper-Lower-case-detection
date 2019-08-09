# A program that finds uppercase and lowercase characters, and lists the number of them for the user to see
# Date: 8.8.20
# Created by Astral

def find():
        n = input('Enter some words that describe your perfect waifu: ')
        counter1 = 0
        counter2 = 0

        for x in n:

                if (x.isupper()) == True:
                        counter1+= 1

                elif (x.islower()) == True:
                        counter2+= 1

        print('Uppercase letters: \n', counter1)
        print('Lowercase letters:', counter2)

find()