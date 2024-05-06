
#https://pypi.org/project/langdetect/
from langdetect import detect, detect_langs
import inspect

#if you're unsure about the attributes of the returned objects, 
# you can inspect them programmatically. For example:

result = detect_langs("Yo soy un individuo")
print("-----------------Ex#1--------------------") 
print("Attributes of detect_langs:", result[0].__dict__)  # Print the attributes of the first LangDetectResult object

print("About the class:", type(detect_langs), dir(detect_langs))
# Break:A break statement in Python alters the flow of a loop by terminating it once a specified condition is met.
# Continue: The continue statement in Python is used to skip the remaining code inside a loop for the current iteration only.
# Pass: The pass statement in Python is used when a statement or a condition is required to be present in the program, 
# but we don’t want any command or code to execute. It’s typically used as a placeholder for future code.


# There is a significant difference between pass and continue, and they are not interchangeable. 

# continue forces the loop to start at the next iteration, whereas pass means, “there is no code to execute here,” 
# and it will continue through the remainder of the loop body.


#Example
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

# Create an instance of the Book class
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

# Inspect the attributes of the instance

print("-----------------Ex#2--------------------") 
print("Attributes of book1:", book1.__dict__)


print("About the class:", type(Book), dir(Book))
