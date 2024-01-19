<h1 align="center"><b>0x06. PYTHON - CLASSES AND OBJECTS</b></h1>
<div align="center"><code>Python</code> <code>OOP</code></div>

<br>

## Background Context
OOP is a totally new concept for all of you (especially those who think they know about it :)). It’s VERY important that you read at least all the material that is listed bellow (and skip what we recommend you to skip, you will see them later in the curriculum).

As usual, make sure you type (never copy and paste), test, understand all examples shown in the following links (including those in the video), test again etc. The biggest and most important takeaway of this project is: experiment by yourself OOP, play with it!

Read or watch the below resources in the order presented.

<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->

<br>

## Resources
<details>
<summary><b><a href="https://python.swaroopch.com/oop.html">Object Oriented Programming</a>  (Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, <code>classmethod</code> and <code>staticmethod</code> yet)</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://python-course.eu/oop/object-oriented-programming.php">Object-Oriented Programming</a> (Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The <code>__init__</code> Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”)</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://python-course.eu/oop/properties-vs-getters-and-setters.php">Properties vs. Getters and Setters</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://www.youtube.com/watch?v=1AGyBuVCTeE&">Learn to Program 9 : Object Oriented Programming</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://www.youtube.com/watch?v=apACNr7DC_s">Python Classes and Objects</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://www.youtube.com/watch?v=-DP1i2ZU9gk">Object Oriented Programming</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<!-- <br>

**man or help:**
- `` -->

<br>

## Learning Objectives
<details>
<summary><b><a href=" "> </a>Why Python programming is awesome</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is OOP</b></summary><br>

OOP stands for Object-Oriented Programming, which is a programming paradigm or methodology used in software development. It is based on the concept of "objects," which are instances of classes, and the principles of encapsulation, inheritance, and polymorphism. Here are the core concepts of OOP:

1. **Classes and Objects**: In OOP, a class is a blueprint or template for creating objects. Objects are instances of classes, and they represent real-world entities or concepts. For example, you can have a "Car" class that defines the properties and behaviors of a car, and then create individual car objects based on that class.
   ```py
   # Define a simple class
   class Dog:
       def __init__(self, name, age):
           self.name = name
           self.age = age
   
       def bark(self):
           print(f"{self.name} says Woof!")
   
   # Create objects of the Dog class
   dog1 = Dog("Buddy", 3)
   dog2 = Dog("Max", 5)
   
   # Access object attributes and call methods
   print(f"{dog1.name} is {dog1.age} years old.")
   dog2.bark()
   ```

2. **Encapsulation**: Encapsulation is the practice of bundling data (attributes) and methods (functions) that operate on that data into a single unit called a class. It allows you to hide the internal details of how an object works and only expose a well-defined interface to interact with the object. This helps in controlling access to data and prevents unintended modification.
   ```py
   class BankAccount:
       def __init__(self, account_number, balance):
           self.account_number = account_number
           self.__balance = balance  # Private attribute
   
       def deposit(self, amount):
           if amount > 0:
               self.__balance += amount
   
       def withdraw(self, amount):
           if amount > 0 and amount <= self.__balance:
               self.__balance -= amount
           else:
               print("Insufficient funds.")
   
       def get_balance(self):
           return self.__balance
   
   # Create a bank account object
   account = BankAccount("12345", 1000)
   
   # Access and modify balance through methods (encapsulation)
   account.deposit(500)
   account.withdraw(200)
   print(f"Account balance: ${account.get_balance()}")
   ```

3. **Inheritance**: Inheritance is a mechanism that allows you to create a new class (subclass or derived class) based on an existing class (superclass or base class). The subclass inherits the attributes and methods of the superclass and can also add its own attributes and methods or override the inherited ones. It promotes code reuse and the creation of a hierarchy of related classes.
   ```py
   # Base class
   class Shape:
       def __init__(self, color):
           self.color = color
   
       def area(self):
           pass
   
   # Derived classes
   class Circle(Shape):
       def __init__(self, color, radius):
           super().__init__(color)
           self.radius = radius
   
       def area(self):
           return 3.14 * self.radius * self.radius
   
   class Rectangle(Shape):
       def __init__(self, color, width, height):
           super().__init__(color)
           self.width = width
           self.height = height
   
       def area(self):
           return self.width * self.height
   
   # Create shape objects
   circle = Circle("Red", 5)
   rectangle = Rectangle("Blue", 4, 6)
   
   print(f"Circle area: {circle.area()} square units")
   print(f"Rectangle area: {rectangle.area()} square units")
   ```

4. **Polymorphism**: Polymorphism means "many shapes" and refers to the ability of objects of different classes to be treated as objects of a common superclass. It allows you to write code that can work with objects of various classes as long as they share a common interface. Polymorphism can be achieved through method overriding and interfaces/abstract classes in some languages.
   ```py
   # Base class
   class Animal:
       def speak(self):
           pass
   
   # Derived classes
   class Dog(Animal):
       def speak(self):
           return "Woof!"
   
   class Cat(Animal):
       def speak(self):
           return "Meow!"
   
   # Create animal objects and demonstrate polymorphism
   animals = [Dog(), Cat()]
   
   for animal in animals:
       print(animal.speak())
   ```

5. **Abstraction**: Abstraction is the process of simplifying complex reality by modeling classes based on the essential properties and behaviors of objects. It allows you to focus on what an object does rather than how it does it. Abstraction helps in managing complexity and making code more understandable.
    ```py
    from abc import ABC, abstractmethod

    # Abstract base class
    class Shape(ABC):
        def __init__(self, color):
            self.color = color

        @abstractmethod
        def area(self):
            pass

    # Derived classes
    class Circle(Shape):
        def __init__(self, color, radius):
            super().__init__(color)
            self.radius = radius

        def area(self):
            return 3.14 * self.radius * self.radius

    class Rectangle(Shape):
        def __init__(self, color, width, height):
            super().__init__(color)
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

    # Create shape objects
    circle = Circle("Red", 5)
    rectangle = Rectangle("Blue", 4, 6)

    # Abstraction ensures that all subclasses implement the 'area' method
    print(f"Circle area: {circle.area()} square units")
    print(f"Rectangle area: {rectangle.area()} square units")
    ```

OOP promotes modularity, reusability, and maintainability in software development. It is widely used in various programming languages like Java, C++, Python, and C#, among others. Developers use OOP to model real-world entities, organize code, and create software systems that are easier to design, extend, and maintain.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>“first-class everything”</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is a class</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is an object and an instance</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is the difference between a class and an object or instance</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is an attribute</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What are and how to use public, protected and private attributes</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is <code>self</code></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is a method</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is the special <code>__init__</code> method and how to use it</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is Data Abstraction, Data Encapsulation, and Information Hiding</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is a property</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is the difference between an attribute and a property in Python</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is the Pythonic way to write getters and setters in Python</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to dynamically create arbitrary new attributes for existing instances of a class</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to bind attributes to object and classes</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is the <code>__dict__</code> of a class and/or instance of a class and what does it contain</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How does Python find the attributes of an object or class</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to use the <code>getattr</code> function</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<br>

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

<!-- <br>

## More Info -->

<br>

## Quiz questions
<details>
<summary><b>Question 0</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 1</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 2</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 3</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 4</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 5</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 6</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 7</b></summary><br>


<br>
</details>

<br>

## Tasks
<details>
<summary>

### 0. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 1. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 2. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 3. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 4. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 5. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 6. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 7. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 8. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 9. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 10. 
`#advanced`

File: []()
</summary>


</details>

