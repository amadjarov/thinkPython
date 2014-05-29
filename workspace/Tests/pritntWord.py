#===============================================================================
# color = raw_input("Please enter a color to be printed: ")
# 
# a= (color+" ")*9
# b= color +"   "*9 +"  " +color
# print a
# print b
# print b
# print a
#===============================================================================

#===============================================================================
# fname = raw_input ("Please, type in your first name: ")
# if fname:
#     print "bla"
# else:
#     print "daaamn"
#===============================================================================

#===============================================================================
# answer = raw_input ("Please enter a color: ")
#  
# if (answer == "black") or (answer == "white"):
#     print "The color was black or white."
# elif answer >= "k":
#     print "The color starts with a letter that comes after \"k\" in the alphabet."
#===============================================================================

#===============================================================================
# something = raw_input ("Please type something ")
#         
# if something >= "1" and something < ":":
#     something = int(something)
# print "The input", something, "is of type", type(something)
#===============================================================================

#===============================================================================
# import types
# 
# something = input ("Please type something ")
# 
# if type(something) is types.IntType:
#     print "The input was an integer"
# elif type(something) is types.FloatType:
#     print "The input was a real number"
# elif type(something) is types.StringType:
#     print "The input was a string"
#===============================================================================

#===============================================================================
# counter = 1
# while counter <= 5:
#     number = input("Guess the " + str(counter) + ". number ")
#     if number != 5:
#         print "Try again."
#     else:
#         print "Good guess!"
#     counter = counter +1
# else:
#     print "Game over"
#===============================================================================


#===============================================================================
# for counter in range(13, 100, 13):
#         print counter
#===============================================================================

#===============================================================================
# for counter in range(5):
#     number = input("Guess the " + str(counter + 1) + ". number ")
#     if number != 5:
#         print "Try again."
#     else:
#         print "Good guess!"
#         break
#===============================================================================

#===============================================================================
# students = ["Paul Miller", "Kathy Jones", "Susan Smith", "John Doe",
# "James Black"]
# 
# print "The following students are in the class:", students
# 
# new_student = raw_input("Type the name of another student: ")
# students.append(new_student)
# print "The following students are in the class:", students
# 
# number = input("Enter a number: ")
# print "The student number", number , "is", students[number]
# 
# students = ["John Smith", "Mary Miller"] + students
# print "The following students are in the class:", students
#===============================================================================

#===============================================================================
# students = ["Paul Miller", "Kathy Jones", "Susan Smith", "John Doe",
# "James Black"]
# 
# print "The following students are in the class:", students
# 
# del students[-1]
# print "The following students are in the class:", students
# 
# another_student = raw_input("Enter the name of a student to be added/deleted: ")
# if another_student in students:
#         students.remove(another_student)
# else:
#         students.append(another_student)
# 
# print "The following students are in the class:", students
# 
# more_students = students[:]
# 
# more_students.reverse()
# print students
# print more_students
#===============================================================================

#===============================================================================
# students = ["Paul Miller", "Kathy Jones", "Susan Smith", "John Doe",
# "James Black"]
# 
# new_students = students[:]
# 
# for student in new_students:
#     print "Do you want to keep student", student, "?"
#     answer = raw_input ("yes/no ")
#     if answer != "yes":
#         students.remove(student)
# print students
#===============================================================================

relatives ={"Lisa" : "daughter", "Bart" : "son", "Marge" : "mother",
"Homer" : "father", "Santa" : "dog"}

#for k in relatives:
#    print  k, "-->", relatives[k]


for member in relatives.keys():
    print member, "is a", relatives[member] 
