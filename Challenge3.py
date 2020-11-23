class Person:
    def __init__(self, name, address, numCourses, courses):
        self.name = name
        self.address = address
        self.numCourses = list(numCourses)
        self.courses = list(courses)


class Student(Person):
    def __init__(self, name, address, numCourses, courses, grades):
        Person.__init__(name, address, numCourses, courses)
        self.grades = grades

    def getAverageGrade(self):
        x = 0
        for i in self.grades:
            x += i
        return float(x/len(self.grades))

class Teacher(Person):
    def __init__(self, name, address, numCourses, courses):
        Person.__init__(name, address, numCourses, courses)

    def addCourse(self, course):
        if course in self.courses:
            return False
        else:
            self.courses.append(course)

    def removeCourse(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            return False
