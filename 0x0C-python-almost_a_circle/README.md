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
- args and kwargs
- Serialization/Deserialization
- SON

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
</details>

<details>
<summary><h3>How to serialize and deserialize a Class</h3></summary>
</details>

<details>
<summary><h3>How to write and read a JSON file</h3></summary>
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


</details>

<details>
<summary>

### 3. Validate attributes
`mandatory`

File: [models/rectangle.py]()
</summary>


</details>

<details>
<summary>

### 4. Area first
`mandatory`

File: [models/rectangle.py]()
</summary>


</details>

<details>
<summary>

### 5. Display #0
`mandatory`

File: [models/rectangle.py]()
</summary>


</details>

<details>
<summary>

### 6. __str__
`mandatory`

File: [models/rectangle.py]()
</summary>


</details>

<details>
<summary>

### 7. Display #1
`mandatory`

File: [models/rectangle.py]()
</summary>


</details>

<details>
<summary>

### 8. Update #0
`mandatory`

File: [models/rectangle.py]()
</summary>


</details>

<details>
<summary>

### 9. Update #1
`mandatory`

File: [models/rectangle.py]()
</summary>


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

