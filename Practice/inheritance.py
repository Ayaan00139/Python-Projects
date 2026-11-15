class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError ("Missing Name")
        self.name=name
...

class Student(Wizard):
    
    def __init__(self,name,house):
        super().__init__(name)
        self.house=house
...

class Professor(Wizard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject
...
wizard=Wizard("Albus") # init method of wizard class called
student=Student("Harry","Gryffindore") # init method of wizard and student class
professor=Professor("Severnus", "Defense")# init method of wizard and professor class