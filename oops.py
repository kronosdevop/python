class Dog:
    def __init__(self,name):
      self.name = name
      print("created Object with the name :  {}" .format(name))

    def talk(self):
       print("woof woof")    
        
    def printName(self):
       print("my name is : {} " .format(self.name))


charlie=Dog("Charlie")   
bruno=Dog("Bruno")

charlie.talk()
bruno.talk()
bruno.printName()
charlie.printName()



class Dog:
    def __init__(self,name):
      self.name = name
      print("created Object with the name :  {}" .format(name))

    def talk(self):
       print("woof woof")    
        
    def printName(self):
       print("my name is : {} " .format(self.name))


charlie=Dog("Charlie")   
bruno=Dog("Bruno")

charlie.talk()
bruno.talk()
bruno.printName()
charlie.printName()


# please explain the above code line by line
# This code defines a Python class named "Dog" which has some methods and attributes. Here's a line-by-line explanation:

# class Dog:
# Defines a new class named "Dog".

# def __init__(self,name):
# Defines the constructor method for the class "Dog". The "self" parameter is a reference to the instance of the class, and "name" is a parameter passed to the constructor.


# self.name = name
# Assigns the "name" parameter passed to the constructor to the "name" attribute of the class.


# print("created Object with the name :  {}" .format(name))
# Prints a message indicating that an object of the "Dog" class has been created with the given name.


# def talk(self):
# Defines a method named "talk" for the class "Dog".


# print("woof woof")
# Prints a message indicating that the dog is barking.


# def printName(self):
# Defines a method named "printName" for the class "Dog".


# print("my name is : {} " .format(self.name))
# Prints the name of the dog.


# charlie=Dog("Charlie")   
# bruno=Dog("Bruno")
# Creates two instances of the "Dog" class, one named "Charlie" and the other named "Bruno".


# charlie.talk()
# bruno.talk()
# Calls the "talk" method for both instances of the "Dog" class, which prints out the message "woof woof".


# bruno.printName()
# charlie.printName()
# Calls the "printName" method for both instances of the "Dog" class, which prints out the name of each dog.