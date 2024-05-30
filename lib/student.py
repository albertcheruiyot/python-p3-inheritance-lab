#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  # Call the __init__ method of the User class
        self.knowledge = []
    
    def learn(self, new_knowledge):
        self.knowledge.append(new_knowledge)
        
        pass

student1 = Student("Albert", "Amina")
print(student1.first_name)  
print(student1.last_name)  

student1.learn("Python basics")
student1.learn("Java Basics")
print(student1.knowledge) 