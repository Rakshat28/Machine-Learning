class Student:
    def __init__(self, fullname):
        self.name = fullname

s1 = Student("rakshat")
print(s1.name)

# definning a class with instance method

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says woof")

dog1 = Dog("Vanya",20)
dog1.bark()

# inheritance in python

class Parent:
    def __init__(self,property):
        self.property = property
    
    def drive(self):
        print("papa drives a car ")

class Child(Parent):
    def __init__(self,property,car):
        super().__init__(property)
        self.car = car
    def show_car(self):
        print(f"I drive {self.car}")

kamlesh = Child(10000,"Nano")
kamlesh.show_car()
kamlesh.drive()