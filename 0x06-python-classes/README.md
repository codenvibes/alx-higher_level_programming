# **0x06. PYTHON - CLASSES AND OBJECTS**
`Python` `OOP`

# Background Context
**OOP is a totally new concept for all of you (especially those who think they know about it :))**. It’s VERY important that you read at least all the material that is listed bellow (and skip what we recommend you to skip, you will see them later in the curriculum).

As usual, make sure you type (never copy and paste), test, understand all examples shown in the following links (including those in the video), test again etc. The biggest and most important takeaway of this project is: experiment by yourself OOP, play with it!


# Resources
- [Object Oriented Programming](https://python.swaroopch.com/oop.html) (Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, `classmethod` and `staticmethod` yet)
- [Object-Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php) (Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The __init__ Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”)
- [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
- [Learn to Program 9 : Object Oriented Programming](https://www.youtube.com/watch?v=1AGyBuVCTeE)
- [Python Classes and Objects](https://www.youtube.com/watch?v=apACNr7DC_s)
- [Object Oriented Programming](https://www.youtube.com/watch?v=-DP1i2ZU9gk)

<!-- man or help:
- `` -->

# Learning Objectives
<details>
<summary><h3>Why Python programming is awesome</h3></summary>
</details>

<details>
<summary><h3>What is OOP</h3></summary>

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
</details>

<details>
<summary><h3>“first-class everything”</h3></summary>

"First-class everything" is not a term typically associated with Object-Oriented Programming (OOP). Instead, it's more closely related to the concept of "first-class citizens" in programming languages. 

In programming language design, when something is said to be a "first-class citizen," it means that this entity (usually a data type or a function) is treated the same way as other entities in the language. It has the same rights and privileges, and it can be manipulated and used in the same way as any other data type or function.

For example:

1. **First-Class Functions**: In a language with first-class functions, functions are treated as first-class citizens. This means you can assign functions to variables, pass them as arguments to other functions, and return them from functions.

2. **First-Class Objects**: Similarly, in some languages, objects or data structures can be treated as first-class citizens. This means you can store them in variables, pass them as parameters to functions, and return them from functions just like any other data type.

In the context of Object-Oriented Programming, the focus is more on objects and classes rather than the concept of "first-class everything." However, some languages that support OOP principles may also support first-class functions or first-class objects, allowing you to work with them in a flexible and versatile manner. The idea is to provide programmers with a higher degree of flexibility and expressiveness in their code.

So, in summary, "first-class everything" is not a standard term in OOP, but it relates to the broader concept of first-class citizens in programming languages, which can apply to both OOP and non-OOP languages.
</details>

<details>
<summary><h3>What is a class</h3></summary>

In object-oriented programming (OOP), a class is a blueprint or template that defines the structure and behavior of objects. It serves as a blueprint for creating individual objects (instances) that belong to that class. A class defines the attributes (properties) and methods (functions) that the objects created from it will have. Here are the key components of a class:

1. **Attributes (Properties)**: Attributes are the data members or variables that describe the characteristics or state of objects created from the class. They represent the object's data or characteristics. For example, if you have a "Car" class, its attributes might include "color," "make," "model," and "year."

2. **Methods (Functions)**: Methods are the functions or behaviors associated with objects of the class. They define what actions the objects can perform. In the "Car" class example, methods might include "start_engine," "accelerate," "brake," and "turn_off_engine."

3. **Constructor**: A constructor is a special method that is typically called when an object of the class is created. It initializes the object's attributes and performs any necessary setup. Constructors often have the same name as the class and are used to set initial values for object attributes.

4. **Access Control (Public, Private, Protected)**: Many programming languages provide access control modifiers that determine the visibility and accessibility of class members (attributes and methods). Common access control modifiers include:
   - **Public**: Members are accessible from anywhere, including outside the class.
   - **Private**: Members are only accessible within the class itself.
   - **Protected**: Members are accessible within the class and its subclasses (derived classes).

Here's a simple example of a Python class:

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start_engine(self):
        self.is_running = True
        print(f"The {self.year} {self.make} {self.model}'s engine is now running.")

    def stop_engine(self):
        self.is_running = False
        print(f"The {self.year} {self.make} {self.model}'s engine is now stopped.")
```

In this example, "Car" is a class that has attributes like "make," "model," and "year," as well as methods like "start_engine" and "stop_engine." You can create individual car objects based on this class, each with its own values for the attributes. For example:

```python
my_car = Car("Toyota", "Camry", 2022)
my_car.start_engine()
my_car.stop_engine()
```

Classes are fundamental to the concept of object-oriented programming and enable the creation of reusable and organized code by modeling real-world entities or abstract concepts as objects with defined attributes and behaviors.
</details>

<details>
<summary><h3>What is an object and an instance</h3></summary>

In the context of Object-Oriented Programming (OOP), "object" and "instance" are related terms that are often used interchangeably, but they have slightly different connotations:

1. **Object**: An object is a fundamental concept in OOP. It is a concrete, tangible entity that represents a specific instance of a class. Objects have attributes (data) and behaviors (methods) associated with them. For example, if you have a class called "Car," an object of that class could represent a particular car with specific characteristics such as its color, make, model, and current speed. Objects are created from classes and are instances of those classes.

2. **Instance**: An instance, in the context of OOP, is synonymous with an object. When you create an object from a class, you are creating an instance of that class. So, if you have a "Car" class and you create a "red Ford Mustang" object from it, that object is an instance of the "Car" class. Instances or objects are unique and distinct, and you can create multiple instances of the same class, each with its own set of attribute values.

In summary, an object is a specific, individual entity that represents a real-world or conceptual thing, and an instance is a term often used interchangeably with object to refer to these individual entities created from a class. Objects (instances) are the building blocks of OOP, and they encapsulate both data and behavior related to a specific concept or entity.
</details>

<details>
<summary><h3>What is the difference between a class and an object or instance</h3></summary>

In object-oriented programming (OOP), a class and an object (or instance) are closely related but serve different purposes:

1. **Class**:
   - A class is a blueprint or template for creating objects (instances).
   - It defines the structure and behavior that objects of that class will have.
   - A class can include attributes (data members or fields) to represent the properties of objects and methods (functions) to define the behaviors associated with those objects.
   - It acts as a general or abstract concept, describing what objects of that class will be like.

2. **Object (or Instance)**:
   - An object, also referred to as an instance, is a concrete, individual entity created from a class.
   - It is an actual occurrence or realization of the class, with its own unique set of attributes and values.
   - Objects represent specific, tangible items or concepts in your program that you can manipulate and interact with.
   - You can create multiple objects from the same class, and each object will have its own distinct data and state.

To illustrate the difference, consider the analogy of a "Car" class:

- **Class**: The "Car" class would define the general structure and behavior of all cars. It might include attributes like "color," "make," and "model," as well as methods like "startEngine" and "drive."
  
- **Object/Instance**: An object or instance of the "Car" class could be a specific car, such as a red 2023 Toyota Camry. This car object would have its own values for the attributes (e.g., color = "red," make = "Toyota," model = "Camry") and could execute the methods defined in the class (e.g., start the engine or drive).

In summary, a class serves as a blueprint for creating objects, while objects (instances) are concrete entities created from that blueprint, each with its own state and behavior. Classes define the common structure, and objects represent specific instances of that structure in your program.
</details>

<details>
<summary><h3>What is an attribute</h3></summary>
</details>

<details>
<summary><h3>What are and how to use public, protected and private attributes</h3></summary>
</details>

<details>
<summary><h3>What is <code>self</code></h3></summary>
</details>

<details>
<summary><h3>What is a method</h3></summary>
</details>

<details>
<summary><h3>What is the special <code>__init__</code> method and how to use it</h3></summary>
</details>

<details>
<summary><h3>What is Data Abstraction, Data Encapsulation, and Information Hiding</h3></summary>
</details>

<details>
<summary><h3>What is a property</h3></summary>
</details>

<details>
<summary><h3>What is the difference between an attribute and a property in Python</h3></summary>
</details>

<details>
<summary><h3>What is the Pythonic way to write getters and setters in Python</h3></summary>
</details>

<details>
<summary><h3>How to dynamically create arbitrary new attributes for existing instances of a class</h3></summary>
</details>

<details>
<summary><h3>How to bind attributes to object and classes</h3></summary>
</details>

<details>
<summary><h3>What is the <code>__dict__</code> of a class and/or instance of a class and what does it contain</h3></summary>
</details>

<details>
<summary><h3>How does Python find the attributes of an object or class</h3></summary>
</details>

<details>
<summary><h3>How to use the <code>getattr</code> function</h3></summary>
</details>

# Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

# More Info
**Documentation is now mandatory!** Each module, class, and method must contain docstring as comments. [Example Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

# Quiz questions
<details>
<summary><h3>Question 0</h3></summary>

What do these lines print?
```python
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User()
>>> u.id
```
- [ ] User.id
- [ ] Nothing
- [ ] id
- [ ] 89
</details>

<details>
<summary><h3>Question 1</h3></summary>

In this following code, what is __password?
```py
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```
- [ ] A public instance attribute
- [ ] A private instance attribute
- [ ] A protected instance attribute
- [ ] A private class attribute
- [ ] A protected class attribute
- [ ] A public class attribute
</details>

<details>
<summary><h3>Question 2</h3></summary>

In this following code, what is id?
```py
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```
- [ ] A public class attribute
- [ ] A protected class attribute
- [ ] A public instance method
- [ ] A private class attribute
- [ ] A public class method
- [ ] A public instance attribute
</details>

<details>
<summary><h3>Question 3</h3></summary>

In this following code, what is is_new?
```py
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```
- [ ] A public instance attribute
- [ ] A private instance attribute
- [ ] A protected instance attribute
- [ ] A private class attribute
- [ ] A protected class attribute
- [ ] A public class attribute
</details>

<details>
<summary><h3>Question 4</h3></summary>

What do these lines print?
```py
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User("John")
>>> u.name
```
- [ ] John
- [ ] no name
- [ ] None
- [ ] name
</details>

<details>
<summary><h3>Question 5</h3></summary>

What do these lines print?
```py
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User()
>>> u.name
```
- [ ] John
- [ ] no name
- [ ] None
- [ ] name
</details>

<details>
<summary><h3>Question 6</h3></summary>

What do these lines print?
```py
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User()
>>> u.is_new
```
- [ ] False
- [ ] True
- [ ] Nothing
- [ ] is_new
</details>

<details>
<summary><h3>Question 7</h3></summary>

In this following code, what is User?
```py
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```
- [ ] A method
- [ ] An instance
- [ ] An attribute
- [ ] A string
- [ ] A class
</details>

# Tasks
<details>
<summary>

### 0. My first square
`mandatory`

File: [0-square.py]()
</summary>

Write an empty class `Square` that defines a square:
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x06$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

guillaume@ubuntu:~/0x06$ ./0-main.py
<class '0-square.Square'>
{}
guillaume@ubuntu:~/0x06$ 
```
</details>

<details>
<summary>

### 1. Square with size
`mandatory`

File: [1-square.py]()
</summary>

Write a class `Square` that defines a square by: (based on `0-square.py`)
- Private instance attribute: `size`
- Instantiation with `size` (no type/value verification)
- You are not allowed to import any module

**Why?**

Why `size` is private attribute?

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.
```bash
guillaume@ubuntu:~/0x06$ cat 1-main.py
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x06$ ./1-main.py
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
guillaume@ubuntu:~/0x06$ 
```
</details>

<details>
<summary>

### 2. Size validation
`mandatory`

File: [2-square.py]()
</summary>

Write a class `Square` that defines a square by: (based on `1-square.py`)
- Private instance attribute: `size`
- Instantiation with optional size: `def __init__(self, size=0):`
    - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x06$ cat 2-main.py
#!/usr/bin/python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x06$ ./2-main.py
<class '2-square.Square'>
{'_Square__size': 3}
<class '2-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
guillaume@ubuntu:~/0x06$ 
```
</details>

<details>
<summary>

### 3. Area of a square
`mandatory`

File: [3-square.py]()
</summary>

Write a class Square that defines a square by: (based on `2-square.py`)
- Private instance attribute: `size`
- Instantiation with optional `size`: `def __init__(self, size=0):`
    - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Public instance method: `def area(self):` that returns the current square area
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x06$ cat 3-main.py
#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))

guillaume@ubuntu:~/0x06$ ./3-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
guillaume@ubuntu:~/0x06$ 
```
</details>

<details>
<summary>

### 4. Access and update private attribute
`mandatory`

File: [4-square.py]()
</summary>

Write a class `Square` that defines a square by: (based on `3-square.py`)
- Private instance attribute: `size`:
    - property `def size(self):` to retrieve it
    - property setter `def size(self, value):` to set it:
        - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Instantiation with optional `size: def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- You are not allowed to import any module

**Why?**

Why a getter and setter?

Reminder: `size` is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.
```bash
guillaume@ubuntu:~/0x06$ cat 4-main.py
#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x06$ ./4-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
guillaume@ubuntu:~/0x06$ 
```
</details>

<details>
<summary>

### 5. Printing a square
`mandatory`

File: [5-square.py]()
</summary>

Write a class `Square` that defines a square by: (based on `4-square.py`)
- Private instance attribute: `size`:
    - property `def size(self):` to retrieve it
    - property setter `def size(self, value):` to set it:
        - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Instantiation with optional `size: def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
    - if `size` is equal to 0, print an empty line
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x06$ cat 5-main.py
#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")

guillaume@ubuntu:~/0x06$ ./5-main.py
###
###
###
--
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
--

--
guillaume@ubuntu:~/0x06$ 
```
</details>

<details>
<summary>

### 6. Coordinates of a square
`mandatory`

File: [6-square.py]()
</summary>

Write a class `Square` that defines a square by: (based on `5-square.py`)
- Private instance attribute: `size`:
    - property `def size(self):` to retrieve it
    - property setter `def size(self, value):` to set it:
        - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Private instance attribute: `position`:
    - property `def position(self):` to retrieve it
    - property setter `def position(self, value):` to set it:
        - `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`
- Instantiation with optional size and optional `position`: `def __init__(self, size=0, position=(0, 0)):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
    - if `size` is equal to 0, print an empty line
    - `position` should be use by using space - **Don’t fill lines by spaces** when `position[1] > 0`
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x06$ cat 6-main.py
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

guillaume@ubuntu:~/0x06$ ./6-main.py | tr " " "_" | cat -e
###$
###$
###$
--$
$
_###$
_###$
_###$
--$
___###$
___###$
___###$
--$
guillaume@ubuntu:~/0x06$ 
```
</details>

<details>
<summary>

### 7. Singly linked list
`#advanced`

File: [100-singly_linked_list.py]()
</summary>

Write a class `Node` that defines a node of a singly linked list by:
- Private instance attribute: `data`:
    - property `def data(self):` to retrieve it
    - property setter `def data(self, value):` to set it:
        - `data` must be an integer, otherwise raise a `TypeError` exception with the message `data must be an integer`
- Private instance attribute: `next_node`:
    - property `def next_node(self):` to retrieve it
    - property setter `def next_node(self, value):` to set it:
        - `next_node` can be `None` or must be a `Node`, otherwise raise a `TypeError` exception with the message `next_node must be a Node object`
- Instantiation with `data` and `next_node`: `def __init__(self, data, next_node=None):`

And, write a class `SinglyLinkedList` that defines a singly linked list by:
- Private instance attribute: `head` (no setter or getter)
- Simple instantiation: `def __init__(self):`
- Should be printable:
    - print the entire list in stdout
    - one node number by line
- Public instance method: `def sorted_insert(self, value):` that inserts a new `Node` into the correct sorted position in the list (increasing order)
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x06$ cat 100-main.py
#!/usr/bin/python3
SinglyLinkedList = __import__('100-singly_linked_list').SinglyLinkedList

sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)

guillaume@ubuntu:~/0x06$ ./100-main.py
-4
-3
1
2
3
3
4
5
5
10
12
guillaume@ubuntu:~/0x06$ 
```
</details>

<details>
<summary>

### 8. Print Square instance
`#advanced`

File: [101-square.py]()
</summary>

Write a class `Square` that defines a square by: (based on `6-square.py`)
- Private instance attribute: `size`:
    - property `def size(self):` to retrieve it
    - property setter `def size(self, value):` to set it:
        - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Private instance attribute: `position`:
    - property `def position(self):` to retrieve it
    - property setter `def position(self, value):` to set it:
        - `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integer`
- Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0)):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
    - if `size` is equal to 0, print an empty line
    - `position` should be use by using space
- Printing a `Square` instance should have the same behavior as `my_print()`
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x06$ cat 101-main.py
#!/usr/bin/python3
Square = __import__('101-square').Square

my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)

guillaume@ubuntu:~/0x06$ ./101-main.py | tr " " "_" | cat -e
#####$
#####$
#####$
#####$
#####$
--$
$
____#####$
____#####$
____#####$
____#####$
____#####$
guillaume@ubuntu:~/0x06$ 
```
</details>

<details>
<summary>

### 9. Compare 2 squares
`#advanced`

File: [102-square.py]()
</summary>

Write a class `Square` that defines a square by: (based on `4-square.py`)
- Private instance attribute: `size`:
    - property `def size(self):` to retrieve it
    - property setter `def size(self, value):` to set it:
        - size must be a number (float or integer), otherwise raise a `TypeError` exception with the message `size must be a number`
        - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Instantiation with `size`: `def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- `Square` instance can answer to comparators: `==,` `!=`, `>`, `>=`, `<` and `<=` based on the square area
- You are not allowed to import any module
guillaume@ubuntu:~/0x06$ cat 102-main.py
```bash
#!/usr/bin/python3
Square = __import__('102-square').Square

s_5 = Square(5)
s_6 = Square(6)

if s_5 < s_6:
    print("Square 5 < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")
if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")

guillaume@ubuntu:~/0x06$ ./102-main.py
Square 5 < Square 6
Square 5 <= Square 6
Square 5 != Square 6
guillaume@ubuntu:~/0x06$ 
```
</details>

<details>
<summary>

### 10. ByteCode -> Python #5
`#advanced`

File: [103-magic_class.py]()
</summary>

Write the Python class `MagicClass` that does exactly the same as the following Python bytecode:
```bash
Disassembly of __init__:
 10           0 LOAD_CONST               1 (0)
              3 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (_MagicClass__radius)

 11           9 LOAD_GLOBAL              1 (type)
             12 LOAD_FAST                1 (radius)
             15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             18 LOAD_GLOBAL              2 (int)
             21 COMPARE_OP               9 (is not)
             24 POP_JUMP_IF_FALSE       60
             27 LOAD_GLOBAL              1 (type)
             30 LOAD_FAST                1 (radius)
             33 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             36 LOAD_GLOBAL              3 (float)
             39 COMPARE_OP               9 (is not)
             42 POP_JUMP_IF_FALSE       60

 12          45 LOAD_GLOBAL              4 (TypeError)
             48 LOAD_CONST               2 ('radius must be a number')
             51 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             54 RAISE_VARARGS            1
             57 JUMP_FORWARD             0 (to 60)

 13     >>   60 LOAD_FAST                1 (radius)
             63 LOAD_FAST                0 (self)
             66 STORE_ATTR               0 (_MagicClass__radius)
             69 LOAD_CONST               3 (None)
             72 RETURN_VALUE

Disassembly of area:
 17           0 LOAD_FAST                0 (self)
              3 LOAD_ATTR                0 (_MagicClass__radius)
              6 LOAD_CONST               1 (2)
              9 BINARY_POWER
             10 LOAD_GLOBAL              1 (math)
             13 LOAD_ATTR                2 (pi)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE

Disassembly of circumference:
 21           0 LOAD_CONST               1 (2)
              3 LOAD_GLOBAL              0 (math)
              6 LOAD_ATTR                1 (pi)
              9 BINARY_MULTIPLY
             10 LOAD_FAST                0 (self)
             13 LOAD_ATTR                2 (_MagicClass__radius)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE
```
- Tip: [Python bytecode](https://docs.python.org/3.4/library/dis.html)
</details>

