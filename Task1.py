class Student:
    def __init__(self, name='noname', age=0, srBall=''):
        self.name = name
        self.age = age
        self.srBall = srBall


    def set_name(self, name):
        self.name = name


    def set_age(self, age):
        self.age = age


    def srBall(self, srBall):
        self.srBall = srBall


    def set_grades(self, grade):
        self.grade = grade


    def get_name(self):
        print(self.name)


    def get_age(self):
        print(self.age)


    def get_grades(self):
        print(self.grade)


student = Student()
student.set_name('name')
student.set_age(13 )
student.set_grades(23)
student.get_name()
student.get_age()
student.get_grades()