class bike:
    def __init__(self,model,brand,engineCC):
        self.model=model
        self.brand=brand
        self.engineCC=engineCC
    def bikeInfoExtra(self,modification,rider):
        self.rider=rider
        self.modification=modification
        return f"{rider} has the best bike in the world with {modification} modification.It's bike is {self.model} with {str(self.engineCC)}CC"


bike1=bike("GSA 1250 R","BMW",1250)
print(bike1.bikeInfoExtra("zero","Ali"))

# //there are four pillars of oop 
# 1)inheritance
# 2)encapsulation
# 3)abstraction
# 4)polymorphism


# encapsulation means that our variables should only be accessible in the class only.Although we need to public some of the variables but we use it to private some of the variables.Variables can be encapsulated by (__) self.__name
class car:
    def __init__(self,model,brand,engineCC):
        self.__model=model
        self.__brand=brand
        self.__engineCC=engineCC
    def bikeInfoExtra(self,modification,rider):
        self.__rider=rider
        self.__modification=modification
        
        return f"{rider} has the best bike in the world with {modification} modification.It's bike is {self.__model} with {str(self.__engineCC)}CC"
    def getProperty(self):
        return self.__model
    
car1=car("swift","suzuki",2024)
print(car1.bikeInfoExtra("zero","waqar"))


# //interitance in which all properties of the parent is inherited to the child

class Parent:
    def __init__(self,age):
        self.age=age
    def useProperties(self):
        return f"I'm {self.age} years old"
class Child(Parent):
    def __init__(self,name,age):
        super().__init__(age)
        self.__name=name
    def UsingParentProperty(self):
        return f"My name is {self.__name} age is {self.age}"
person1=Child("Ali",23)
print(person1.age)
print(person1.UsingParentProperty())
# person1.age
print(person1.useProperties())




# //abstraCTION IS used to hide the complexities of the parent class so we can define logic in child class
class Person:
    def __init__(self,age):
        self.age=age
    def useProperties(self):
        pass
    def abstraction(self):
        pass
class ChildPerson(Parent):
    def __init__(self,name,age):
        super().__init__(age)
        self.__name=name
    def UsingParentProperty(self):
          return f"My name is {self.__name} age is {self.age}"
    def abstraction(self):
        self.__name





# // polymorphism in which two classes inherit one class is called polymorphism
class Animal:
    def sound(self):
        pass
class Cat(Animal):
    def sound(self):
        return "Meow"
class Dog(Animal):
    def sound(self):
        return "Woow"
def make_sound(animal):
    print(animal.sound())      

animal1=Dog()
animal2=Cat()
make_sound(animal1)
make_sound(animal2)



        