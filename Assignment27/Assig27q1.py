'''Write a Python program to implement a class named BookStore with the following specifications:
The class should contain two instance variables:
Name (Book Name)
Author (Book Author)
The class should contain one class variable:
NoOfBooks (initialize it to 0)
Define a constructor (__init__) that accepts Name and Author and initializes the instance variables.
Inside the constructor, increment the class variable NoOfBooks by 1 whenever a new object is created.
Implement an instance method:
Display() -should display book details in the following format:'''


class BookStore:

    # Class Variable
    NoOfBooks = 0

    # Constructor
    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks += 1

    # Display Method
    def Display(self):
        print(self.Name, "by", self.Author,
              ". No of books:", BookStore.NoOfBooks)


def main():

    obj1 = BookStore("Linux System Programming", "Robert Love")
    obj1.Display()

    obj2 = BookStore("C Programming", "Dennis Ritchie")
    obj2.Display()


if __name__ == "__main__":
    main()