class Student:
    'contains students, email, name ...'

    def __init__(self, name ="John Doe", courses =[]):
        self.name = name
        self.courses = courses
        print "Created a class instance for "+ name

    def printDetails(self):
        print "Name: ", self.name
        print "Courses: ", self.courses

    def enroll(self, course):
        self.courses.append(course)

student1 = Student("Mary", ["L548"])

print "Input the courses which", student1.name, "is enrolled in."
newcourse = raw_input ("Type the course number or 'stop' ")

while newcourse != "stop":
    student1.enroll(newcourse)
    print "Input the courses which", student1.name, "is enrolled in."
    newcourse = raw_input ("Type the course number or 'stop' ")

student1.printDetails() 