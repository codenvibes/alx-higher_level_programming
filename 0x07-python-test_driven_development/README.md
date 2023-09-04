# **0x07. PYTHON - TEST-DRIVEN DEVELOPMENT**
`Python` `UnitTests` `TDD`

# Background Context
<details>
<summary><h3>Important notice on intranet checks for Python projects</h3></summary>

Starting from today:
- Based on the requirements of each task, **you should always write the documentation (module(s) + function(s)) and tests first**, before you actually code anything
- The intranet checks for Python projects won’t be released before their first deadline, in order for you to focus more on TDD and think about all possible cases
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case. **But not in the implementation of them!**
- **Don’t trust the user**, always think about all possible edge cases
</details>

# Resources
- [Never forget a test](https://intranet.alxswe.com/concepts/47)
- [doctest — Test interactive Python examples](https://docs.python.org/3.4/library/doctest.html) (until “26.2.3.7. Warnings” included)
- [doctest – Testing through documentation](https://pymotw.com/3/doctest/)
- [Unit Tests in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8)
- [Unittest module](https://www.youtube.com/watch?v=6tNS--WetLI)
- [Interactive and Non-interactive tests](https://mattermost.com/blog/testing-python-understanding-doctest-and-unittest/)

<!-- man or help:
- `` -->

# Learning Objectives
<details>
<summary><h3>Why Python programming is awesome</h3></summary>
</details>

<details>
<summary><h3>What’s an interactive test</h3></summary>
</details>

<details>
<summary><h3>Why tests are important</h3></summary>
</details>

<details>
<summary><h3>How to write Docstrings to create tests</h3></summary>
</details>

<details>
<summary><h3>How to write documentation for each module and function</h3></summary>
</details>

<details>
<summary><h3>What are the basic option flags to create tests</h3></summary>
</details>

<details>
<summary><h3>How to find edge cases</h3></summary>
</details>

# Requirements
<details>
<summary><h3>Python Scripts</h3></summary>

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`
</details>

<details>
<summary><h3>Python Test Cases</h3></summary>

- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: `.txt`)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case – The Checker is checking for tests!
</details>


# Quiz questions
<details>
<summary><h3>Question 0</h3></summary>

Is this module correctly commented?
```py
#!/usr/bin/python3
import sys

""" 
    My calculation module
"""
...
```
- [x] No
- [ ] Yes

> Tips:<br>
Docstring must be before import statements
</details>

<details>
<summary><h3>Question 1</h3></summary>

Is this a standardized way to comment a function in Python?
```py
##########
# Addition function
##########
def add(a, b):
    return a + b
```
- [ ] No
- [ ] Yes
</details>

<details>
<summary><h3>Question 2</h3></summary>

Is this a standardized way to comment a function in Python?
```py
"""" Addition function """
def add(a, b):
    return a + b
```
- [ ] No
- [ ] Yes
</details>

<details>
<summary><h3>Question 3</h3></summary>

Is this a standardized way to comment a function in Python?
```py
def add(a, b):
    """ Addition function """
    return a + b
```
- [ ] No
- [ ] Yes
</details>

<details>
<summary><h3>Question 4</h3></summary>

Based on this code, what should all the test cases be? (select multiple)
```py
def uniq(list):
    """ Returns unique values of a list """
    u_list = []
    for item in list:
        if item not in u_list:
            u_list.append(item)
    return u_list
```
- [ ] list with one element (any type)
- [ ] not a list argument (ex: passing a dictionary to the method)
- [ ] list with twice the same element (same type)
- [ ] list with more than 2 times the same element (same type)
- [ ] list with 2 different element (same type)
- [ ] list with multiple types (integer, string, etc…)
- [ ] empty list
</details>

<details>
<summary><h3>Question 5</h3></summary>

Is this module correctly commented?
```py
#!/usr/bin/python3
""" 
    My calculation module
"""
import sys
...
```
- [ ] No
- [ ] Yes
</details>

<details>
<summary><h3>Question 6</h3></summary>

Is this a standardized way to comment a function in Python?
```py
/* Addition function */
def add(a, b):
    return a + b
```
- [ ] No
- [ ] Yes
</details>

# Tasks
<details>
<summary>

### 0. Integers addition
`mandatory`

File: [0-add_integer.py, tests/0-add_integer.txt]()
</summary>

Write a function that adds 2 integers.

-   Prototype: `def add_integer(a, b=98):`
-   `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message `a must be an integer` or `b must be an integer`
-   `a` and `b` must be first casted to integers if they are float
-   Returns an integer: the addition of `a` and `b`
-   You are not allowed to import any module

```
guillaume@ubuntu:~/0x07$ cat 0-main.py
#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x07$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
9 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
5
guillaume@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
3
guillaume@ubuntu:~/0x07$

```
</details>

<details>
<summary>

### 1. Divide a matrix
`mandatory`

File: [2-matrix_divided.py](), [tests/2-matrix_divided.txt]()
</summary>

Write a function that divides all elements of a matrix.

-   Prototype: `def matrix_divided(matrix, div):`
-   `matrix` must be a list of lists of integers or floats, otherwise raise a `TypeError` exception with the message `matrix must be a matrix (list of lists) of integers/floats`
-   Each row of the `matrix` must be of the same size, otherwise raise a `TypeError` exception with the message `Each row of the matrix must have the same size`
-   `div` must be a number (integer or float), otherwise raise a `TypeError` exception with the message `div must be a number`
-   `div` can't be equal to `0`, otherwise raise a `ZeroDivisionError` exception with the message `division by zero`
-   All elements of the matrix should be divided by `div`, rounded to 2 decimal places
-   Returns a new matrix
-   You are not allowed to import any module

```
guillaume@ubuntu:~/0x07$ cat 2-main.py
#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

guillaume@ubuntu:~/0x07$ ./2-main.py
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2
5 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$

```

Note: you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.
</details>

<details>
<summary>

### 2. Say my name
`mandatory`

File: [3-say_my_name.py](), [tests/3-say_my_name.txt]()
</summary>

Write a function that prints `My name is <first name> <last name>`

-   Prototype: `def say_my_name(first_name, last_name=""):`
-   `first_name` and `last_name` must be strings otherwise, raise a `TypeError` exception with the message `first_name must be a string` or `last_name must be a string`
-   You are not allowed to import any module

```
guillaume@ubuntu:~/0x07$ cat 3-main.py
#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x07$ ./3-main.py | cat -e
My name is John Smith$
My name is Walter White$
My name is Bob $
first_name must be a string$
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
5 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$

```

Note: you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.
</details>

<details>
<summary>

### 3. 
`mandatory`

File: []()
</summary>

Write a function that prints a square with the character `#`.

-   Prototype: `def print_square(size):`
-   `size` is the size length of the square
-   `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
-   if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
-   if `size` is a float and is less than 0, raise a `TypeError` exception with the message `size must be an integer`
-   You are not allowed to import any module

```
guillaume@ubuntu:~/0x07$ cat 4-main.py
#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")

guillaume@ubuntu:~/0x07$ ./4-main.py
####
####
####
####

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

#

size must be >= 0

guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/4-print_square.txt
guillaume@ubuntu:~/0x07$

```
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

