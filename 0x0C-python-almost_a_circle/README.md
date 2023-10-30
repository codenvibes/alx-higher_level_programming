# **0x0C. PYTHON - ALMOST A CIRCLE**
`Python` `OOP`

# Background Context
The AirBnB project is a big part of the Higher level curriculum. This project will help you be ready for it.

In this project, you will review everything about Python:
- Import
- Exceptions
- Class
- Private attribute
- Getter/Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read/Write file

You will also learn about:
- `args` and `kwargs`
- Serialization/Deserialization
- JSON

# Resources
- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

<!-- man or help:
- `` -->

# Learning Objectives
<details>
<summary><h3>What is Unit testing and how to implement it in a large project</h3></summary>

Unit testing is a software testing technique where individual components or units of a software application are tested in isolation to ensure they work as expected. These "units" are typically functions, methods, or classes, and the goal of unit testing is to verify that each unit performs its intended functionality correctly. Unit tests are typically automated and are written by developers to catch and prevent regressions (unexpected issues) in their code as it evolves.

Here are the steps to implement unit testing in Python:

1. Choose a Testing Framework:
   Python has several testing frameworks available, but two of the most popular ones are `unittest` (inspired by Java's JUnit) and `pytest`. You can choose the one that best fits your project's requirements. In this example, we'll use `unittest`.

2. Create Test Cases:
   Write test cases for each unit of code you want to test. Test cases are functions or methods that verify specific behaviors of your code. They typically follow a naming convention like `test_something()` to indicate that they are tests.

3. Import the Testing Framework:
   Import the testing framework you've chosen at the beginning of your test file.

4. Write Test Functions:
   Write test functions within your test file that use the testing framework's assertions to check if the actual output of your code matches the expected output. Common assertions include `assertEqual()`, `assertTrue()`, `assertFalse()`, etc.

5. Organize Your Tests:
   Group related test functions into test classes. These test classes should inherit from the testing framework's base class (e.g., `unittest.TestCase`).

6. Run the Tests:
   Use the testing framework's test runner to execute your tests. You can usually run tests from the command line or integrate them into your development environment.

7. Analyze Test Results:
   After running the tests, the testing framework will provide feedback on which tests passed and which failed. If a test fails, you'll need to investigate and fix the underlying issue in your code.

Here's a simple example of unit testing in Python using the `unittest` framework:

```python
import unittest

# The code you want to test (a simple function)
def add(a, b):
    return a + b

# Create a test class that inherits from unittest.TestCase
class TestAddition(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)  # Check if 2 + 3 equals 5

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)  # Check if -2 + -3 equals -5

    def test_add_mixed_numbers(self):
        self.assertEqual(add(2, -3), -1)  # Check if 2 + -3 equals -1

if __name__ == '__main__':
    unittest.main()
```

To run these tests, save the code in a `.py` file (e.g., `test_math.py`) and execute it using Python. The `unittest.main()` function will discover and run the test cases, and you'll see the test results in the console.

Remember to write test cases that cover various scenarios and edge cases to ensure the robustness of your code. Unit testing is an essential practice in software development to catch and fix bugs early in the development process.
</details>

<details>
<summary><h3>How to serialize and deserialize a Class</h3></summary>

Serialization and deserialization are processes used to convert complex data structures like classes and objects into a format that can be easily stored, transmitted, or reconstructed later. Python provides several modules and libraries for serialization and deserialization, with two of the most common being `pickle` and `json`. 

Here's how to serialize and deserialize a class in Python using both `pickle` and `json`:

<br>
<p align="center">※※※※※※※※※※※※</p>

#### Using `pickle` (Python-specific):

`pickle` is a Python-specific module that can serialize and deserialize Python objects. It can handle complex Python objects, including classes and instances, but it is not recommended to use it with untrusted or unauthenticated data as it may execute arbitrary code during deserialization.

```python
import pickle

# Define a simple class
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of the class
obj = MyClass("Alice", 30)

# Serialize the object to a binary string
serialized_obj = pickle.dumps(obj)

# Save the serialized object to a file
with open("myclass.pickle", "wb") as file:
    file.write(serialized_obj)

# Deserialize the object from the file
with open("myclass.pickle", "rb") as file:
    deserialized_obj = pickle.load(file)

# Now, deserialized_obj is an instance of MyClass
print(deserialized_obj.name)  # Output: Alice
print(deserialized_obj.age)   # Output: 30
```

<br>
<p align="center">※※※※※※※※※※※※</p>

#### Using `json` (cross-language):

`json` is a more widely used format for serialization because it's human-readable and cross-language compatible. However, it can only serialize simple data types (e.g., dictionaries, lists, strings, numbers).

To serialize a class instance with `json`, you need to convert the object's attributes into a dictionary and then serialize the dictionary:

```python
import json

# Define a class
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of the class
obj = MyClass("Alice", 30)

# Convert the object to a dictionary
obj_dict = {"name": obj.name, "age": obj.age}

# Serialize the dictionary to a JSON string
serialized_obj = json.dumps(obj_dict)

# Save the JSON string to a file
with open("myclass.json", "w") as file:
    file.write(serialized_obj)

# Deserialize the object from the file
with open("myclass.json", "r") as file:
    deserialized_obj_dict = json.load(file)

# Create an instance of the class from the dictionary
deserialized_obj = MyClass(deserialized_obj_dict["name"], deserialized_obj_dict["age"])

# Now, deserialized_obj is an instance of MyClass
print(deserialized_obj.name)  # Output: Alice
print(deserialized_obj.age)   # Output: 30
```

Keep in mind that when using `json`, you can only serialize simple data types and not complex behaviors or methods defined within a class. If you need to preserve the behavior of a class, `pickle` might be a better choice for Python-specific applications.
</details>

<details>
<summary><h3>How to write and read a JSON file</h3></summary>

Writing and reading a JSON file in Python is straightforward, thanks to the built-in `json` module. Here are the steps to write and read a JSON file:

<br>
<p align="center">※※※※※※※※※※※※</p>

#### Writing a JSON File:

1. Create a Python dictionary or list that you want to store as JSON data.

2. Use the `json.dump()` function to write the data to a JSON file. This function takes two arguments: the data to write and the file object to write to.

3. Ensure that the file is opened in write mode (`"w"` or `"wb"` for binary mode) and that you specify the filename with a `.json` extension.

```python
import json

# Data to write to the JSON file (a dictionary in this example)
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Specify the filename
filename = "data.json"

# Write the data to the JSON file
with open(filename, "w") as json_file:
    json.dump(data, json_file, indent=4)  # indent for pretty formatting (optional)
```

This code will create a JSON file named "data.json" and write the `data` dictionary to it.

<br>
<p align="center">※※※※※※※※※※※※</p>

#### Reading a JSON File:

1. Open the JSON file in read mode (`"r"` or `"rb"` for binary mode).

2. Use the `json.load()` function to read the JSON data from the file and parse it into a Python dictionary or list.

```python
import json

# Specify the filename to read from
filename = "data.json"

# Read the JSON data from the file
with open(filename, "r") as json_file:
    loaded_data = json.load(json_file)

# Now, loaded_data is a Python dictionary containing the JSON data
print(loaded_data)
```

This code will read the JSON data from "data.json" and store it in the `loaded_data` variable as a Python dictionary.

Make sure that the JSON file exists in the specified location before attempting to read from it, or handle exceptions to deal with potential file not found errors.

Remember that the `json` module is suitable for handling simple data structures like dictionaries and lists. If you need to work with more complex objects or custom classes, you might consider using other serialization techniques like `pickle` or a dedicated data serialization library.
</details>

<details>
<summary><h3>What is <code>*args</code> and how to use it</h3></summary>
</details>

<details>
<summary><h3>What is <code>**kwargs</code> and how to use it</h3></summary>
</details>

<details>
<summary><h3>How to handle named arguments in a function</h3></summary>
</details>

# Requirements
<details>
<summary><h3>Python Scripts</h3></summary>

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation `python3 -c 'print(__import__("my_module").__doc__)'`
- All your classes should have a documentation `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
- All your functions (inside and outside a class) should have a documentation `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
</details>

<details>
<summary><h3>Python Unit Tests</h3></summary>

- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- You have to use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- All your test files should be python files (extension: `.py`)
- All your test files and folders should start with `test_`
- Your file organization in the tests folder should be the same as your project: ex: for `models/base.py`, unit tests must be in: `tests/test_models/test_base.py`
- All your tests should be executed by using this command: `python3 -m unittest discover tests`
- You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base.py`
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case
</details>

# Tasks
<details>
<summary>

### 0. If it's not tested it doesn't work
`mandatory`

File: [tests/]()
</summary>

All your files, classes and methods must be unit tested and be PEP 8 validated.
```bash
guillaume@ubuntu:~/$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/$
```
Note that this is just an example. The number of tests you create can be different from the above example.
</details>

<details>
<summary>

### 1. Base class
`mandatory`

File: [models/base.py](), [models/__init__.py]()
</summary>

Write the first class `Base`:

Create a folder named `models` with an empty file `__init__.py` inside - with this file, the folder will become a Python package

Create a file named `models/base.py`:

- Class `Base`:
    - private class attribute `__nb_objects = 0`
    - class constructor: `def __init__(self, id=None):`:
        - if `id` is not `None`, assign the public instance attribute `id` with this argument value - you can assume `id` is an integer and you don’t need to test the type of it
        - otherwise, increment `__nb_objects` and assign the new value to the public instance attribute `id`

This class will be the “base” of all other classes in this project. The goal of it is to manage `id` attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)
```bash
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

guillaume@ubuntu:~/$ ./0-main.py
1
2
3
12
4
guillaume@ubuntu:~/$ 
```
</details>

<details>
<summary>

### 2. First Rectangle
`mandatory`

File: [models/rectangle.py]()
</summary>

Write the class `Rectangle` that inherits from `Base`:

- In the file `models/rectangle.py`
- Class `Rectangle` inherits from `Base`
- Private instance attributes, each with its own public getter and setter:
    - `__width` -> `width`
    - `__height` -> `height`
    - `__x` -> `x`
    - `__y` -> `y`
- Class constructor: `def __init__(self, width, height, x=0, y=0, id=None)`:
    - Call the super class with `id` - this super call with use the logic of the `__init__` of the `Base` class
    - Assign each argument `width`, `height`, `x` and `y` to the right attribute
Why private attributes with getter/setter? Why not directly public attribute?

Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes.
```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)

guillaume@ubuntu:~/$ ./1-main.py
1
2
12
guillaume@ubuntu:~/$ 
```
</details>

<details>
<summary>

### 3. Validate attributes
`mandatory`

File: [models/rectangle.py]()
</summary>

Update the class `Rectangle` by adding validation of all setter methods and instantiation (`id` excluded):

- If the input is not an integer, raise the `TypeError` exception with the message: `<name of the attribute> must be an integer`. Example: `width must be an integer`
- If `width` or `height` is under or equals 0, raise the `ValueError` exception with the message: `<name of the attribute> must be > 0`. Example: `width must be > 0`
- If `x` or `y` is under 0, raise the `ValueError` exception with the message: `<name of the attribute> must be >= 0`. Example: `x must be >= 0`
```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    try:
        Rectangle(10, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ ./2-main.py
[TypeError] height must be an integer
[ValueError] width must be > 0
[TypeError] x must be an integer
[ValueError] y must be >= 0
guillaume@ubuntu:~/$ 
```
</details>

<details>
<summary>

### 4. Area first
`mandatory`

File: [models/rectangle.py]()
</summary>

Update the class `Rectangle` by adding the public method `def area(self):` that returns the area value of the `Rectangle` instance.
```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
""" 3-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())

guillaume@ubuntu:~/$ ./3-main.py
6
20
56
guillaume@ubuntu:~/$ 
```
</details>

<details>
<summary>

### 5. Display #0
`mandatory`

File: [models/rectangle.py]()
</summary>

Update the class `Rectangle` by adding the public method `def display(self):` that prints in stdout the `Rectangle` instance with the character `#` - you don’t need to handle `x` and `y` here.
```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
""" 4-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6)
    r1.display()

    print("---")

    r1 = Rectangle(2, 2)
    r1.display()

guillaume@ubuntu:~/$ ./4-main.py
####
####
####
####
####
####
---
##
##
guillaume@ubuntu:~/$ 
```
</details>

<details>
<summary>

### 6. __str__
`mandatory`

File: [models/rectangle.py]()
</summary>

Update the class `Rectangle` by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`
```
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
""" 5-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6, 2, 1, 12)
    print(r1)

    r2 = Rectangle(5, 5, 1)
    print(r2)

guillaume@ubuntu:~/$ ./5-main.py
[Rectangle] (12) 2/1 - 4/6
[Rectangle] (1) 1/0 - 5/5
guillaume@ubuntu:~/$ 
```
</details>

<details>
<summary>

### 7. Display #1
`mandatory`

File: [models/rectangle.py]()
</summary>

Update the class `Rectangle` by improving the public method `def display(self):` to print in stdout the `Rectangle` instance with the character `#` by taking care of `x` and `y`
```
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
""" 6-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(2, 3, 2, 2)
    r1.display()

    print("---")

    r2 = Rectangle(3, 2, 1, 0)
    r2.display()

guillaume@ubuntu:~/$ ./6-main.py | cat -e
$
$
  ##$
  ##$
  ##$
---$
 ###$
 ###$
guillaume@ubuntu:~/$ 
```
</details>

<details>
<summary>

### 8. Update #0
`mandatory`

File: [models/rectangle.py]()
</summary>

Update the class `Rectangle` by adding the public method `def update(self, *args):` that assigns an argument to each attribute:

- 1st argument should be the `id` attribute
- 2nd argument should be the `width` attribute
- 3rd argument should be the `height` attribute
- 4th argument should be the `x` attribute
- 5th argument should be the `y` attribute

This type of argument is called a “no-keyword argument” - Argument order is super important.
```
guillaume@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
""" Doc """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(89)
    print(r1)

    r1.update(89, 2)
    print(r1)

    r1.update(89, 2, 3)
    print(r1)

    r1.update(89, 2, 3, 4)
    print(r1)

    r1.update(89, 2, 3, 4, 5)
    print(r1)

guillaume@ubuntu:~/$ ./7-main.py
[Rectangle] (1) 10/10 - 10/10
[Rectangle] (89) 10/10 - 10/10
[Rectangle] (89) 10/10 - 2/10
[Rectangle] (89) 10/10 - 2/3
[Rectangle] (89) 4/10 - 2/3
[Rectangle] (89) 4/5 - 2/3
guillaume@ubuntu:~/$ 
```
</details>

<details>
<summary>

### 9. Update #1
`mandatory`

File: [models/rectangle.py]()
</summary>

Update the class `Rectangle` by updating the public method `def update(self, *args):` by changing the prototype to `update(self, *args, **kwargs)` that assigns a key/value argument to attributes:

- `**kwargs` can be thought of as a double pointer to a dictionary: key/value
    - As Python doesn’t have pointers, `**kwargs` is not literally a double pointer – describing it as such is just a way of explaining its behavior in terms you’re already familiar with
- `**kwargs` must be skipped if `*args` exists and is not empty
- Each key in this dictionary represents an attribute to the instance

This type of argument is called a “key-worded argument”. Argument order is not important.
```
guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
""" 8-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(height=1)
    print(r1)

    r1.update(width=1, x=2)
    print(r1)

    r1.update(y=1, width=2, x=3, id=89)
    print(r1)

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)

guillaume@ubuntu:~/$ ./8-main.py
[Rectangle] (1) 10/10 - 10/10
[Rectangle] (1) 10/10 - 10/1
[Rectangle] (1) 2/10 - 1/1
[Rectangle] (89) 3/1 - 2/1
[Rectangle] (89) 1/3 - 4/2
guillaume@ubuntu:~/$ 
```
</details>

<details>
<summary>

### 10. And now, the Square!
`mandatory`

File: [models/square.py]()
</summary>


</details>

<details>
<summary>

### 11. Square size
`mandatory`

File: [models/square.py]()
</summary>


</details>

<details>
<summary>

### 12. Square update
`mandatory`

File: [models/square.py]()
</summary>


</details>

<details>
<summary>

### 13. Rectangle instance to dictionary representation
`mandatory`

File: [models/rectangle.py]()
</summary>


</details>

<details>
<summary>

### 14. Square instance to dictionary representation
`mandatory`

File: [models/square.py]()
</summary>


</details>

<details>
<summary>

### 15. Dictionary to JSON string
`mandatory`

File: [models/base.py]()
</summary>


</details>

<details>
<summary>

### 16. JSON string to file
`mandatory`

File: [models/base.py]()
</summary>


</details>

<details>
<summary>

### 17. JSON string to dictionary
`mandatory`

File: [models/base.py]()
</summary>


</details>

<details>
<summary>

### 18. Dictionary to Instance
`mandatory`

File: [models/base.py]()
</summary>


</details>

<details>
<summary>

### 19. File to instances
`mandatory`

File: [models/base.py]()
</summary>


</details>

<details>
<summary>

### 20. JSON ok, but CSV?
`#advanced`

File: [models/]()
</summary>


</details>

<details>
<summary>

### 21. Let's draw it
`#advanced`

File: [models/base.py]()
</summary>


</details>

