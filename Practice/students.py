class Student:
    def __init__(self,name,house):
        
        self.name=name
        
        self.house=house
    
    def __str__(self):
        return f"{self._name} is from {self._house}"

    @property #Getter
    def name(self):
        return self._name

    @name.setter #Getter
    def name(self,name):
        if not name:#means name==""
            raise ValueError("Missing Name")
        self._name=name

    @property #Getter
    def house(self):
        return self._house

    @house.setter #Setter
    def house(self,house):
        if house not in ["Yes","No"]:
            raise ValueError("Invalid house")
        print("Called")
        self._house=house
    
def main():
    # name, house=get_student()
    # print(f"{name} is from {house}")
    student=get_student()
    print(student)


def get_student():
    name=input("Whats Your Name? ")
    house=input("Whats Your House? ")
    # student= Student(name,house) # Constructor Call
    # return student
    
    return Student(name,house) 
    
    # student=[input("Whats Your Name? "),input("Whats Your House? ")]
    # return student
    # return input("Whats Your Name? "),input("Whats Your House? ") 
    # student ={}
    # student["name"]=input("Whats Your Name? ") \n student["house"]=input("Whats Your House? ")
    #return {name=input("Whats Your Name? "),house=input("Whats Your House? ")}


if __name__=="__main__":
    main()