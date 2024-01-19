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

"First-class everything" is not a term typically associated with Object-Oriented Programming (OOP). Instead, it's more closely related to the concept of "first-class citizens" in programming languages. 

In programming language design, when something is said to be a "first-class citizen," it means that this entity (usually a data type or a function) is treated the same way as other entities in the language. It has the same rights and privileges, and it can be manipulated and used in the same way as any other data type or function.

For example:

1. **First-Class Functions**: In a language with first-class functions, functions are treated as first-class citizens. This means you can assign functions to variables, pass them as arguments to other functions, and return them from functions.

2. **First-Class Objects**: Similarly, in some languages, objects or data structures can be treated as first-class citizens. This means you can store them in variables, pass them as parameters to functions, and return them from functions just like any other data type.

In the context of Object-Oriented Programming, the focus is more on objects and classes rather than the concept of "first-class everything." However, some languages that support OOP principles may also support first-class functions or first-class objects, allowing you to work with them in a flexible and versatile manner. The idea is to provide programmers with a higher degree of flexibility and expressiveness in their code.

So, in summary, "first-class everything" is not a standard term in OOP, but it relates to the broader concept of first-class citizens in programming languages, which can apply to both OOP and non-OOP languages.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is a class</b></summary><br>

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

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is an object and an instance</b></summary><br>

In the context of Object-Oriented Programming (OOP), "object" and "instance" are related terms that are often used interchangeably, but they have slightly different connotations:

1. **Object**: An object is a fundamental concept in OOP. It is a concrete, tangible entity that represents a specific instance of a class. Objects have attributes (data) and behaviors (methods) associated with them. For example, if you have a class called "Car," an object of that class could represent a particular car with specific characteristics such as its color, make, model, and current speed. Objects are created from classes and are instances of those classes.

2. **Instance**: An instance, in the context of OOP, is synonymous with an object. When you create an object from a class, you are creating an instance of that class. So, if you have a "Car" class and you create a "red Ford Mustang" object from it, that object is an instance of the "Car" class. Instances or objects are unique and distinct, and you can create multiple instances of the same class, each with its own set of attribute values.

In summary, an object is a specific, individual entity that represents a real-world or conceptual thing, and an instance is a term often used interchangeably with object to refer to these individual entities created from a class. Objects (instances) are the building blocks of OOP, and they encapsulate both data and behavior related to a specific concept or entity.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is the difference between a class and an object or instance</b></summary><br>

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

<br>

***In summary, a class serves as a blueprint for creating objects, while objects (instances) are concrete entities created from that blueprint, each with its own state and behavior. Classes define the common structure, and objects represent specific instances of that structure in your program.***

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is an attribute</b></summary><br>

In the context of programming and object-oriented programming (OOP), an attribute is a characteristic or property that is associated with an object, class, or data structure. Attributes define the state or characteristics of an object and can have values that describe the object's characteristics.

Attributes are often used to represent the data or variables within a class or object. They can store information about the object's state or characteristics, and these values can be accessed and manipulated through methods or functions associated with the class or object.

Here's a simple example in Python to illustrate attributes within a class:

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # 'name' is an attribute that stores the person's name
        self.age = age    # 'age' is an attribute that stores the person's age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an instance of the Person class
person1 = Person("Alice", 30)

# Accessing attributes
print(person1.name)  # Output: "Alice"
print(person1.age)   # Output: 30

# Calling a method that uses attributes
person1.say_hello()  # Output: "Hello, my name is Alice and I am 30 years old."
```

In this example, the `Person` class has two attributes, `name` and `age`, which store the name and age of a person. These attributes are initialized when a new `Person` object is created and can be accessed and used within the class methods, such as `say_hello()`. Attributes help define the state of individual objects created from the class.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What are and how to use public, protected and private attributes</b></summary><br>

In object-oriented programming (OOP), public, protected, and private are access modifiers used to control the visibility and accessibility of class attributes (variables) and methods (functions). These access modifiers help enforce encapsulation, which is one of the fundamental principles of OOP. Here's an explanation of each access modifier and how to use them:

1. **Public**:
   - **Accessibility**: Public attributes and methods are accessible from anywhere, both inside and outside the class.
   - **Example**:

   ```python
   class MyClass:
       def __init__(self):
           self.public_var = 10

       def public_method(self):
           return "This is a public method"

   obj = MyClass()
   print(obj.public_var)          # Accessing a public attribute
   print(obj.public_method())     # Accessing a public method
   ```

2. **Protected**:
   - **Accessibility**: Protected attributes and methods are not truly private but are intended to be used only within the class and its subclasses. In Python, conventionally, you prefix the attribute or method name with a single underscore (e.g., `_protected_var`) to indicate that it's protected.
   - **Example**:

   ```python
   class MyClass:
       def __init__(self):
           self._protected_var = 20

       def _protected_method(self):
           return "This is a protected method"

   obj = MyClass()
   print(obj._protected_var)            # Accessing a protected attribute (not recommended but possible)
   print(obj._protected_method())       # Accessing a protected method (not recommended but possible)
   ```

3. **Private**:
   - **Accessibility**: Private attributes and methods are meant to be used only within the class where they are defined. In Python, you prefix the attribute or method name with double underscores (e.g., `__private_var`) to indicate that it's private.
   - **Example**:

   ```python
   class MyClass:
       def __init__(self):
           self.__private_var = 30

       def __private_method(self):
           return "This is a private method"

   obj = MyClass()
   # Attempting to access private attributes/methods from outside the class will result in an error
   # print(obj.__private_var)              # This will raise an AttributeError
   # print(obj.__private_method())         # This will raise an AttributeError
   ```

In Python, even though you can access protected and private attributes/methods from outside the class using their names, it's considered a convention to respect the single underscore (_) and double underscore (__) prefixes as indications of the intended access level. Developers should not access protected and private members directly, but rather use the public methods provided by the class to interact with them. This helps maintain encapsulation and ensures that the internal implementation of the class can change without affecting external code that uses the class.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is <code>self</code></b></summary><br>

The use of "self" in programming is a concept that primarily appears in object-oriented languages like Python. It refers to a special variable or keyword that is used within a class to access the attributes and methods of an object created from that class. The choice of the word "self" is a convention in Python, but other programming languages may use different keywords like "this."

In Python, when you define methods within a class, you typically include the "self" parameter as the first parameter in those methods. This parameter represents the instance of the class itself, and it allows you to refer to the attributes and methods of that instance.

Here's a basic example in Python to illustrate the use of "self":

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)

# Creating an object of MyClass
obj = MyClass(42)

# Accessing an attribute using "self"
print(obj.value)  # Prints 42

# Calling a method using "self"
obj.print_value()  # Prints 42
```

In the `__init__` constructor and `print_value` method, you can see that "self" is used to access the "value" attribute of the object and to call the "print_value" method on that specific object.

The use of "self" helps differentiate between instance-level attributes/methods and class-level attributes/methods, allowing you to work with and manipulate object-specific data within a class.

<br>
<p align="center">※※※※※※※※※※※※</p>
<br>

In object-oriented programming, there is a distinction between instance-level attributes/methods and class-level attributes/methods, and understanding this difference is crucial for designing and using classes effectively. Here's an explanation of each:

1. **Instance-Level Attributes/Methods**:

   - **Attributes**: These are variables that belong to a specific instance (object) of a class. Each object created from a class can have its own unique values for these attributes. Instance attributes are defined within the constructor method (`__init__` in Python) and are typically initialized with values specific to that instance.

   - **Methods**: These are functions defined within a class that can operate on the attributes of a specific instance. Methods are called on individual objects, and they can access and modify instance-specific data. In Python, the first parameter of instance methods is conventionally named "self," which refers to the instance itself.

   Example (Python):

   ```python
   class Dog:
       def __init__(self, name):
           self.name = name  # Instance attribute

       def bark(self):
           print(f"{self.name} says Woof!")  # Instance method
   ```

   In this example, "name" is an instance attribute, and "bark" is an instance method. Each "Dog" object can have its own unique "name" attribute value.

2. **Class-Level Attributes/Methods**:

   - **Attributes**: These are variables that belong to the class itself, rather than to individual instances. They are shared among all instances of the class. Class attributes are typically defined outside of any method within the class and are the same for all objects of that class.

   - **Methods**: These are functions that are defined within the class but are meant to operate on the class itself or on class-level attributes. They are not tied to individual instances and cannot access instance-specific data. Class methods are typically defined using the `@classmethod` decorator in Python.

   Example (Python):

   ```python
   class Circle:
       pi = 3.14159265359  # Class attribute

       @classmethod
       def circumference(cls, radius):
           return 2 * cls.pi * radius  # Class method
   ```

   In this example, "pi" is a class attribute, and "circumference" is a class method. All "Circle" objects share the same value of "pi."

In summary, instance-level attributes and methods are specific to individual objects created from a class, allowing each object to have its own state and behavior. Class-level attributes and methods, on the other hand, are shared among all instances of the class and are typically used for characteristics or behaviors that are common to all objects of that class.

<br>
<p align="center">※※※※※※※※※※※※</p>
<br>

In the code example provided, `cls` is not a reserved keyword in Python; rather, it's a common naming convention used for the first parameter of a class method. The name `cls` is short for "class," and it is used to refer to the class itself within the method. You can technically use any name you like for this parameter, but using `cls` is a widely followed convention, and it makes the code more readable and self-explanatory.

Here's the relevant part of the code for reference:

```python
class Circle:
    pi = 3.14159265359  # Class attribute

    @classmethod
    def circumference(cls, radius):
        return 2 * cls.pi * radius  # Class method
```

In this code, `cls` is used as the first parameter of the `circumference` class method. When you call a class method like `Circle.circumference(radius)`, Python automatically passes the class itself (in this case, the `Circle` class) as the first argument (`cls`). You can then use `cls` within the method to access class-level attributes or perform class-specific operations.

So, in the context of this code, `cls.pi` refers to the class attribute `pi` defined in the `Circle` class. It allows you to access the class-level constant value of π (pi) within the method.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is a method</b></summary><br>

In computer programming, a method is a function or procedure that is associated with an object or a class in the context of Object-Oriented Programming (OOP). Methods define the behaviors or actions that objects of a class can perform. They are an integral part of encapsulation and allow you to define the operations that can be performed on the data (attributes) of an object.

Here are some key points about methods:

1. **Belong to Objects or Classes**: Methods can be associated with either individual objects (instance methods) or with the class itself (class or static methods).

2. **Behavior Definition**: Methods define what an object can do or how it can interact with other objects. They encapsulate the functionality that operates on the object's data.

3. **Access to Object Data**: Methods typically have access to the object's attributes, allowing them to read or modify the state of the object.

4. **Method Signature**: A method's signature includes its name and the parameters it accepts. The combination of a method's name and its parameter list is known as the method's signature. The return type (what the method returns) is also part of the signature.

Here's a simple example in Python:

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}'s engine is started.")

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry")

# Calling the start_engine method on the my_car object
my_car.start_engine()  # Output: "Toyota Camry's engine is started."
```

In this example, `start_engine` is a method of the `Car` class. It defines the behavior of starting the car's engine when called on a `Car` object. When we call `my_car.start_engine()`, it executes the code within the `start_engine` method, using the attributes of the `my_car` object to provide context-specific behavior.

Methods are essential in OOP because they allow you to bundle data (attributes) and behavior (methods) together within a class, promoting encapsulation and providing a clear and organized way to interact with objects.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is the special <code>__init__</code> method and how to use it</b></summary><br>

The `__init__` method is a special method in Python that is used for initializing objects created from a class. It is also known as the constructor method because it is automatically called when you create a new instance (object) of a class. This method allows you to set up the initial state of an object by defining its attributes or performing any necessary setup tasks.

Here's the basic syntax for defining and using the `__init__` method in a Python class:

```python
class MyClass:
    def __init__(self, parameter1, parameter2, ...):
        # Initialization code here
        self.attribute1 = parameter1
        self.attribute2 = parameter2
        # ...

# Creating an instance of MyClass and passing values to the __init__ method
my_object = MyClass(value1, value2, ...)
```

Here's what's happening in the code above:

1. We define a class named `MyClass`.

2. Inside the class, we define the `__init__` method. It takes at least one parameter, `self`, which represents the instance of the class being created. You can also include other parameters to initialize the object's attributes.

3. Within the `__init__` method, we set up the initial state of the object by assigning values to its attributes using the `self` keyword. These attributes can be accessed and modified throughout the object's lifetime.

4. When we create an instance of `MyClass` (e.g., `my_object = MyClass(value1, value2, ...)`), the `__init__` method is automatically called with the provided arguments, and it initializes the object's attributes accordingly.

Here's a simple example:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating a Person object
person1 = Person("Alice", 30)

# Accessing object attributes
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30
```

In this example, the `__init__` method initializes the `name` and `age` attributes of the `Person` object when it is created. You can customize the `__init__` method to perform any necessary setup for your class instances, and it allows you to ensure that objects are properly initialized upon creation.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is Data Abstraction, Data Encapsulation, and Information Hiding</b></summary><br>

Data Abstraction, Data Encapsulation, and Information Hiding are related concepts in Object-Oriented Programming (OOP) that contribute to the principles of encapsulation and abstraction. They help in organizing and controlling access to data within a class, making the code more modular and maintainable.

1. **Data Abstraction**:
   - Data abstraction is the process of simplifying complex reality by modeling classes based on the essential properties and behaviors of objects while ignoring the non-essential details.
   - It involves defining a class that represents a real-world entity or concept and focusing on what the object does rather than how it does it.
   - Abstraction helps in managing complexity by allowing developers to work with high-level, abstract representations of data and functionality.

2. **Data Encapsulation**:
   - Data encapsulation, also known as data hiding, is a fundamental concept in OOP that combines data and the methods that operate on that data into a single unit called a class.
   - It enforces the idea that an object's internal state (data or attributes) should not be directly accessible from outside the object. Instead, interactions with the object's data should occur through well-defined methods.
   - By encapsulating data, you can control access to it and protect it from unintended modification. This improves data integrity and helps maintain a stable interface for interacting with the object.

3. **Information Hiding**:
   - Information hiding is a principle that emphasizes the importance of hiding the implementation details of a class while exposing only the necessary information or interface to the outside world.
   - It is closely related to data encapsulation and is often used interchangeably with it. However, information hiding also includes the idea of selectively exposing certain aspects of an object's behavior while keeping others hidden.
   - The goal of information hiding is to reduce complexity by allowing developers to work with the public interface of a class without needing to know how the class internally achieves its functionality.

In summary, data abstraction focuses on modeling objects at a high level, data encapsulation ensures that data and methods are packaged together within a class and accessed through a controlled interface, and information hiding aims to hide unnecessary implementation details while exposing a clear and well-defined public interface to the users of a class. These concepts collectively contribute to the principles of encapsulation and abstraction in OOP, promoting modularity and maintainability in software development.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is a property</b></summary><br>

In the context of programming and software development, a property is a characteristic or attribute of an object or data structure. Properties are used to describe the state or characteristics of an object, and they often have associated values. Properties are a fundamental concept in object-oriented programming (OOP) and are typically encapsulated within classes.

Here are a few key points about properties:

1. **Attributes of Objects**: <br> Properties represent the characteristics or attributes of objects. For example, in a "Person" class, properties might include "name," "age," and "address."

2. **Accessors and Mutators**: <br> Properties often have associated accessors and mutators. Accessors (or getters) are methods that allow you to retrieve the value of a property, while mutators (or setters) are methods that allow you to modify the value of a property. These accessors and mutators help control how the property is read from and written to.

3. **Encapsulation**: <br> Properties are an essential part of encapsulation in object-oriented programming. They allow you to hide the internal state of an object and provide controlled access to it. This means that the internal data of an object is not directly accessible from outside the object, and access is only possible through defined methods (accessors and mutators).

4. **Data Validation**: <br> Properties can include logic for data validation. For example, when setting the "age" property of a "Person" object, you can include validation rules to ensure that the age is within a valid range.

5. **Visibility Modifiers**: <br> In many programming languages, you can specify visibility modifiers for properties to control their accessibility. Common visibility modifiers include "public" (accessible from anywhere), "private" (accessible only within the class), and "protected" (accessible within the class and its subclasses).

Here's a simplified example in Python, where a "Person" class has properties for name and age with associated accessors and mutators:

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter method for the name property
    def get_name(self):
        return self._name

    # Setter method for the name property
    def set_name(self, name):
        self._name = name

    # Getter method for the age property
    def get_age(self):
        return self._age

    # Setter method for the age property with data validation
    def set_age(self, age):
        if age >= 0:
            self._age = age

# Creating a Person object
person = Person("Alice", 30)

# Accessing and modifying properties using accessors and mutators
print(person.get_name())  # Output: Alice
person.set_name("Bob")
print(person.get_name())  # Output: Bob

print(person.get_age())   # Output: 30
person.set_age(25)
print(person.get_age())   # Output: 25
```

In this example, the `name` and `age` properties are encapsulated within the "Person" class, and their access is controlled through getter and setter methods. This allows for data validation and controlled access to the properties.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is the difference between an attribute and a property in Python</b></summary><br>

In Python, the terms "attribute" and "property" are related but have distinct meanings:

1. **Attribute**:

   - An attribute is a characteristic or piece of data associated with an object. It can be thought of as a variable that belongs to an object and holds information about the object's state.
   - Attributes in Python are typically defined within a class to represent the object's properties. They can be accessed using dot notation (e.g., `object.attribute`) to retrieve or modify their values.
   - Attributes can be public, which means they can be accessed directly from outside the class, or they can be made private by using a single underscore prefix (e.g., `_attribute`) to indicate that they are intended for internal use within the class.

   Here's an example of defining and using an attribute in Python:

   ```python
   class Person:
       def __init__(self, name):
           self.name = name  # 'name' is an attribute of the 'Person' class

   person1 = Person("Alice")
   print(person1.name)  # Accessing the 'name' attribute
   ```

2. **Property**:

   - A property, on the other hand, is a special kind of attribute that is accessed or modified using methods like `getter` and `setter` methods. Properties are used to control the access and modification of an object's attribute values.
   - Properties allow you to add custom logic or validation when getting or setting the attribute's value, which can be useful for maintaining data integrity or implementing computed attributes.
   - In Python, you can define properties using the `@property` decorator for the getter method and the `@<attribute>.setter` decorator for the setter method.

   Here's an example of using properties in Python:

   ```python
   class Circle:
       def __init__(self, radius):
           self._radius = radius  # Private attribute

       @property
       def radius(self):
           return self._radius

       @radius.setter
       def radius(self, value):
           if value < 0:
               raise ValueError("Radius cannot be negative")
           self._radius = value

   circle = Circle(5)
   print(circle.radius)  # Accessing the 'radius' property
   circle.radius = 7    # Modifying the 'radius' property
   ```

In summary, attributes are basic data members of a class, while properties are a way to control access to and modification of attributes by using methods to get and set their values with additional logic if needed. Properties are often used when you want to encapsulate and validate attribute access in Python classes.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is the Pythonic way to write getters and setters in Python</b></summary><br>

In Python, you can create getters and setters for class attributes using properties and decorators. The Pythonic way to write getters and setters is to use the `@property` decorator for the getter and the `@<attribute_name>.setter` decorator for the setter. This approach allows you to maintain a clean and simple syntax while providing controlled access to class attributes. Here's an example:

```python
class MyClass:
    def __init__(self, value):
        self._value = value  # Private attribute with an underscore prefix

    @property
    def value(self):
        """Getter method for _value."""
        return self._value

    @value.setter
    def value(self, new_value):
        """Setter method for _value."""
        if new_value >= 0:
            self._value = new_value
        else:
            raise ValueError("Value must be non-negative")

# Creating an instance of MyClass
obj = MyClass(10)

# Using the getter
print(obj.value)  # This calls the value() method and returns 10

# Using the setter
obj.value = 20  # This calls the value.setter method and sets _value to 20

# Using the setter with an invalid value
# This will raise a ValueError because the setter enforces a non-negative constraint
obj.value = -5
```

In this example:

- The `_value` attribute is considered private by convention (not enforced by the language) because it has an underscore prefix. It indicates that it should not be accessed directly from outside the class.

- The `@property` decorator is used to define a getter method for the `value` attribute. When you access `obj.value`, it calls the `value()` method, returning the value of `_value`.

- The `@value.setter` decorator is used to define a setter method for the `value` attribute. When you assign a value to `obj.value`, it calls the `value.setter` method, allowing you to enforce constraints or perform any necessary validation.

This approach adheres to the Pythonic principle of "we are all consenting adults here," which means that it trusts the programmer to use the public interface correctly and only provides special methods like getters and setters when necessary. It promotes clean, readable code while still allowing for controlled attribute access when needed.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to dynamically create arbitrary new attributes for existing instances of a class</b></summary><br>

In Python, you can dynamically create arbitrary new attributes for existing instances of a class by simply assigning values to them using the dot notation. Python allows you to add new attributes to an object on-the-fly, which is one of its dynamic features. Here's an example of how to do this:

```python
class MyClass:
    def __init__(self, initial_value):
        self.initial_value = initial_value

# Create an instance of MyClass
obj = MyClass(42)

# Dynamically add a new attribute to the instance
obj.new_attribute = "Hello, World!"

# Access the newly created attribute
print(obj.new_attribute)  # Output: Hello, World!
```

In the example above:

1. We define a class `MyClass` with an `__init__` method that initializes an attribute `initial_value`.

2. We create an instance of `MyClass` named `obj` with an initial value of 42.

3. We dynamically add a new attribute `new_attribute` to the `obj` instance by simply assigning a value to it using the dot notation.

4. We access and print the value of the newly created attribute, demonstrating that it's accessible just like any other attribute of the instance.

This flexibility can be useful, but it's important to use it judiciously, as adding too many dynamic attributes can make code harder to understand and maintain. Additionally, it's a good practice to document the attributes that a class is expected to have, so other developers working on the code can understand its structure and use.

Keep in mind that if you try to access an attribute that hasn't been assigned yet, you'll get an `AttributeError`. So, it's a good practice to check if an attribute exists before accessing it using the `hasattr()` function or a `try...except` block.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to bind attributes to object and classes</b></summary><br>

In Python, you can bind attributes to both objects (instances) and classes. Binding attributes to objects allows you to store specific data or behavior for individual instances, while binding attributes to classes allows you to store data or behavior shared among all instances of that class. Here's how you can do both:

### Binding Attributes to Objects (Instances):

You can bind attributes to specific instances of a class by assigning values to them within the methods of the class or directly on the instance using the dot notation. Here's an example:

```python
class MyClass:
    def __init__(self, initial_value):
        self.instance_attribute = initial_value

# Create two instances of MyClass
obj1 = MyClass(42)
obj2 = MyClass(123)

# Bind an attribute to obj1
obj1.dynamic_attribute = "Hello, World!"

# Access instance attributes
print(obj1.instance_attribute)  # Output: 42
print(obj2.instance_attribute)  # Output: 123

# Access the dynamically added attribute
print(obj1.dynamic_attribute)   # Output: Hello, World!
# This will raise an AttributeError for obj2 because it doesn't have 'dynamic_attribute'
```

In this example, `instance_attribute` is an attribute that is initialized in the constructor (`__init__`) and `dynamic_attribute` is a dynamically added attribute to `obj1`.

### Binding Attributes to Classes:

You can also bind attributes directly to the class itself. These attributes are shared among all instances of the class. You typically use class attributes to store data that is common to all instances or to define class-level methods. Here's an example:

```python
class MyClass:
    class_attribute = "This is a class attribute"

    def __init__(self, initial_value):
        self.instance_attribute = initial_value

# Create two instances of MyClass
obj1 = MyClass(42)
obj2 = MyClass(123)

# Access class attribute
print(MyClass.class_attribute)  # Output: This is a class attribute

# Access instance attributes
print(obj1.instance_attribute)  # Output: 42
print(obj2.instance_attribute)  # Output: 123
```

In this example, `class_attribute` is a class attribute shared among all instances of `MyClass`. You can access it using the class name or any instance of the class.

Remember that class attributes are common to all instances of the class and can be useful for sharing data or behavior that is consistent across all instances. Instance attributes, on the other hand, are unique to each instance and allow you to store individual data or behavior for each object.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is the <code>__dict__</code> of a class and/or instance of a class and what does it contain</b></summary><br>

In Python, the `__dict__` attribute is a dictionary that stores the namespace of a class or an instance of a class. It contains the names and values of all attributes and methods associated with that class or instance. Here's how it works for both classes and instances:

1. **Class `__dict__`**:
   
   For a class, `Class.__dict__` contains the attributes and methods defined in the class. These can include class variables, methods, and other attributes. Here's an example:

   ```python
   class MyClass:
       class_variable = 42

       def __init__(self, value):
           self.value = value

   print(MyClass.__dict__)
   ```

   Output:
   ```
   {'__module__': '__main__', 'class_variable': 42, '__init__': <function MyClass.__init__ at 0x...>, '__dict__': <attribute '__dict__' of 'MyClass' objects>, '__weakref__': <attribute '__weakref__' of 'MyClass' objects>, '__doc__': None}
   ```

   In this case, `MyClass.__dict__` contains information about the class itself, including the `class_variable` and the `__init__` method.

2. **Instance `__dict__`**:

   For an instance of a class, `Instance.__dict__` contains the attributes specific to that instance. These are typically the instance variables, which are unique to each instance of the class. Here's an example:

   ```python
   obj = MyClass(10)
   obj.dynamic_attribute = "Hello, World!"

   print(obj.__dict__)
   ```

   Output:
   ```
   {'value': 10, 'dynamic_attribute': 'Hello, World!'}
   ```

   In this case, `obj.__dict__` contains the instance-specific attributes, which are `value` and `dynamic_attribute`. It does not include the `class_variable` defined in the class.

You can manipulate the `__dict__` of an instance to add, modify, or remove attributes dynamically, but it's generally better to use standard attribute assignment and access methods for clarity and maintainability unless you have a specific reason to work directly with the `__dict__`.

Keep in mind that `__dict__` is one of Python's introspection features, and it allows you to inspect and modify objects at runtime, which can be powerful but should be used with caution to avoid unexpected behavior.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How does Python find the attributes of an object or class</b></summary><br>

In Python, the process of finding attributes (attributes are variables or methods associated with an object or class) of an object or class involves a mechanism called attribute resolution. The attribute resolution process depends on whether you're trying to access an attribute of an object or a class attribute. Here's how Python finds attributes:

1. **Object Attributes:**

   When you access an attribute of an object using the dot notation (`obj.attribute`), Python follows these steps to find the attribute:
   
   a. Python first checks if the attribute exists directly in the instance. If it does, Python uses that attribute.

   b. If the attribute is not found in the instance, Python looks for it in the class of the instance. If the attribute exists in the class, Python uses it.

   c. If the attribute is not found in the instance or its class, Python checks the base classes (if the class inherits from other classes). This process continues up the class hierarchy until the attribute is found or until Python reaches the top-level base class, which is typically the `object` class.

   d. If Python doesn't find the attribute in any of the above steps, it raises an `AttributeError`.

   Here's an example:

   ```python
   class MyClass:
       class_attribute = "I'm a class attribute"

       def __init__(self):
           self.instance_attribute = "I'm an instance attribute"

   obj = MyClass()

   print(obj.instance_attribute)  # Accessing an instance attribute
   print(obj.class_attribute)     # Accessing a class attribute through an instance
   ```

2. **Class Attributes:**

   When you access a class attribute (an attribute associated with the class itself) directly using the class name (`ClassName.attribute`), Python looks for the attribute in the following order:

   a. Python first checks if the attribute exists in the class itself. If it does, Python uses that attribute.

   b. If the attribute is not found in the class, Python checks the base classes (if the class inherits from other classes) following the same inheritance chain described above.

   c. If Python doesn't find the attribute in any of the above steps, it raises an `AttributeError`.

   Here's an example:

   ```python
   class ParentClass:
       class_attribute = "I'm a class attribute in the parent class"

   class ChildClass(ParentClass):
       pass

   print(ChildClass.class_attribute)  # Accessing a class attribute from a subclass
   ```

This attribute resolution process allows Python to support inheritance and attribute access in a way that's consistent with the class hierarchy. It ensures that the most specific definition of an attribute is used when accessed, but it falls back to more general definitions if needed.

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

