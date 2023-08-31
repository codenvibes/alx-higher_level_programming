# **0x06. PYTHON - CLASSES AND OBJECTS**
`Python` `OOP`

# Background Context
OOP is a totally new concept for all of you (especially those who think they know about it :)). It’s VERY important that you read at least all the material that is listed bellow (and skip what we recommend you to skip, you will see them later in the curriculum).

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
</details>

<details>
<summary><h3>“first-class everything”</h3></summary>
</details>

<details>
<summary><h3>What is a class</h3></summary>
</details>

<details>
<summary><h3>What is an object and an instance</h3></summary>
</details>

<details>
<summary><h3>What is the difference between a class and an object or instance</h3></summary>
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


</details>

<details>
<summary>

### 4. Access and update private attribute
`mandatory`

File: [4-square.py]()
</summary>


</details>

<details>
<summary>

### 5. Printing a square
`mandatory`

File: [5-square.py]()
</summary>


</details>

<details>
<summary>

### 6. Coordinates of a square
`mandatory`

File: [6-square.py]()
</summary>


</details>

<details>
<summary>

### 7. Singly linked list
`#advanced`

File: [100-singly_linked_list.py]()
</summary>


</details>

<details>
<summary>

### 8. Print Square instance
`#advanced`

File: [101-square.py]()
</summary>


</details>

<details>
<summary>

### 9. Compare 2 squares
`#advanced`

File: [102-square.py]()
</summary>


</details>

<details>
<summary>

### 10. ByteCode -> Python #5
`#advanced`

File: [103-magic_class.py]()
</summary>


</details>

