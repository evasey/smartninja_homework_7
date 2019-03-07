

#There are many ways how to join two strings together or how to add data in a string.

#Consider these two strings:

str_one = "Happy"
str_two = "Day"

#We can join them with a plus:

print(str_one + str_two)  # result: HappyDay

#We can add a string in-between:

print(str_one + " " + str_two)  # result: Happy Day

#We can use %s to add them in a string:

print("%s %s" % (str_one, str_two))

#Or, we can use the format() method, with placeholders like {0}:

print("{0} {1}".format(str_one, str_two))

#The preferred approach is the last one, the format() method.