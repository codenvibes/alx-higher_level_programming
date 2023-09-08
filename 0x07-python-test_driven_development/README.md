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

An interactive test in Python typically refers to a way of running code interactively and receiving immediate feedback. This is often done using interactive development environments (IDEs), Python shells, or Jupyter notebooks. Interactive testing is a helpful approach for exploring and debugging code, as it allows you to execute small code snippets and see the results without having to write a complete program.

Here are a few common ways to perform interactive testing in Python:

1. **Python REPL (Read-Eval-Print Loop)**: <br> Python comes with a built-in REPL, which allows you to enter Python code line by line and see the output immediately. You can access the Python REPL by running the `python` or `python3` command in your terminal.

   ```python
   $ python
   Python 3.8.2 (default, Feb 24 2020, 17:52:18)
   [GCC 7.3.0] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>> print("Hello, world!")
   Hello, world!
   >>> 5 + 3
   8
   >>> exit()
   ```

2. **Jupyter Notebooks**: <br> Jupyter notebooks provide an interactive and web-based environment for writing and running Python code. You can write and execute code in cells, view the output, and add rich text, images, and explanations in between.

3. **Integrated Development Environments (IDEs)**: <br> Many Python IDEs, such as PyCharm, Visual Studio Code, and Spyder, offer interactive modes where you can run code snippets and get immediate feedback. This is often helpful for debugging and exploring code.

4. **Online Python Interpreters**: <br> Various online platforms allow you to run Python code interactively in a web browser without installing any software locally. Examples include Repl.it and Google Colab.

Interactive testing is particularly useful when you want to experiment with new ideas, test functions or algorithms, and quickly check the behavior of specific code snippets without having to create a full-fledged Python script or program. It's an essential part of the development process for many Python developers.
</details>

<details>
<summary><h3>Why tests are important</h3></summary>

Tests are an integral part of the software development process and play a crucial role in ensuring the reliability, stability, and maintainability of software systems. Here are some key reasons why tests are important in software development:

1. **Bug Detection**: <br> Tests help identify bugs, errors, and issues in the codebase. By systematically testing various parts of the software, developers can catch and fix problems before they become more significant issues in production.

2. **Quality Assurance**: <br> Testing ensures that the software meets the specified requirements and functions correctly. It helps maintain a high level of quality by verifying that the software behaves as expected under various conditions.

3. **Regression Testing**: <br> As software evolves and new features are added, there is a risk of introducing new bugs or breaking existing functionality. Regression testing, which involves re-running tests to check for unintended side effects, helps prevent these issues.

4. **Code Maintenance**: <br> Well-written tests serve as documentation for how the code is supposed to work. They make it easier for developers to understand the codebase, make changes, and refactor without introducing new problems.

5. **Collaboration**: <br> Tests enable collaboration among team members. When one developer writes tests for a particular piece of functionality, other team members can rely on those tests to understand how the code works and build upon it.

6. **Continuous Integration/Continuous Deployment (CI/CD)**: <br> Tests are a critical component of CI/CD pipelines. Automated tests ensure that code changes do not break existing functionality before they are deployed to production, thereby reducing the risk of introducing defects.

7. **Improved Productivity**: <br> While writing tests may require an initial time investment, they can save time in the long run. Bugs caught early in development are often easier and less costly to fix than those discovered later in the development lifecycle.

8. **Confidence**: <br> Having a comprehensive test suite gives developers and stakeholders confidence that the software behaves as intended. This confidence is essential for making informed decisions about releasing the software to end-users.

9. **Documentation**: <br> Tests serve as executable documentation. They provide clear examples of how various parts of the codebase are intended to be used and can help new developers understand the system faster.

10. **User Satisfaction**: <br> Thorough testing leads to a more stable and reliable software product. Users are more satisfied when they experience fewer crashes, errors, and unexpected behavior.

11. **Security**: <br> Security vulnerabilities can have severe consequences. Tests can be used to identify security issues early and ensure that security measures are effective.

In summary, tests are essential for delivering high-quality software that meets user requirements, is maintainable, and can evolve over time. They provide a safety net for developers, reduce the risk of defects in production, and contribute to overall software reliability and robustness.
</details>

<details>
<summary><h3>How to write Docstrings to create tests</h3></summary>

Docstrings are used to document Python code, providing information about a module, class, function, or method. While docstrings themselves are not used to create tests directly, they can be helpful in generating tests or ensuring that your code is testable. Here's how you can write docstrings to support testing in your Python code:

1. **Describe the Function or Method**: <br> Begin your docstring with a brief description of what the function or method does. This helps both developers and testing frameworks understand the purpose of the code.

   ```python
   def add(a, b):
       """
       Adds two numbers and returns the result.

       Parameters:
           a (int): The first number.
           b (int): The second number.

       Returns:
           int: The sum of a and b.
       """
       return a + b
   ```

2. **Document Parameters**: <br> Clearly document the function or method parameters, including their data types and any constraints or requirements. This information can help testers understand how to provide valid inputs.

3. **Document Return Values**: <br> Explain what the function or method returns and the data type of the return value. This helps testers understand what to expect from the function.

4. **Include Examples**: <br> Provide usage examples within the docstring. These examples can serve as test cases for your code.

   ```python
   def add(a, b):
       """
       Adds two numbers and returns the result.

       Parameters:
           a (int): The first number.
           b (int): The second number.

       Returns:
           int: The sum of a and b.

       Examples:
           >>> add(2, 3)
           5
           >>> add(-1, 1)
           0
       """
       return a + b
   ```

5. **Include Edge Cases**: <br> If applicable, include information about edge cases or corner cases that need to be tested.

6. **Mention Side Effects**: <br> If the function has any side effects (e.g., modifying global variables), document them in the docstring.

7. **Use Docstring Formats**: <br> There are various docstring formats, such as reStructuredText (reST) and Google-style docstrings. Pick a format that's commonly used in your project or organization.

While docstrings themselves don't create tests, they serve as valuable documentation for your code, making it easier to write tests. You can use tools like Sphinx to generate documentation from your docstrings, and testing frameworks like `doctest` can extract and execute code examples from docstrings as tests.

Here's an example of how you can use `doctest` to test code based on the examples in the docstring:

```python
import doctest

def add(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of a and b.

    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
    """
    return a + b

if __name__ == "__main__":
    doctest.testmod()
```

Running this script will execute the examples in the docstring as tests and report any failures.
</details>

<details>
<summary><h3>How to write documentation for each module and function</h3></summary>

Writing documentation for each module and function in your Python code is essential for making your codebase understandable, maintainable, and usable by others (including your future self). Python has a standard way of documenting code using docstrings, and tools like Sphinx can help generate documentation in various formats (HTML, PDF, etc.). Here's how you can write documentation for modules and functions:

<br>
<p align="center">※※※※※※※※※※※※</p>
<h3>Writing Module Documentation:</h3>

1. **Module-Level Docstring**: <br> At the top of your module (Python file), include a module-level docstring. This docstring should describe the purpose and contents of the module. Use triple double-quotes (`"""`) for multi-line docstrings.

   ```python
   """This module provides utility functions for working with strings."""
   ```

2. **Module-level Imports**: <br> If your module imports other modules or has any global variables, include a section at the beginning of the module that lists these imports and variables, along with explanations if necessary.

<br>
<p align="center">※※※※※※※※※※※※</p>
<h3>Writing Function Documentation:</h3>

1. **Function-Level Docstring**: <br> For each function, include a docstring just below the function definition. The docstring should describe what the function does, its parameters (arguments), return values, and any exceptions it may raise. Use triple double-quotes for multi-line docstrings.

   ```python
   def add(a, b):
       """
       Adds two numbers.

       Args:
           a (int): The first number.
           b (int): The second number.

       Returns:
           int: The sum of a and b.
       """
       return a + b
   ```

2. **Parameters**: <br> List all parameters with their types and descriptions in the docstring. Mention whether they are required or optional.

3. **Return Values**: <br> Specify the type and description of the return value. If the function doesn't return anything (returns `None`), mention that explicitly.

4. **Raises (if applicable)**: <br> If the function can raise exceptions, list them in a "Raises" section and provide explanations.

5. **Examples**: <br> Provide usage examples of the function in the docstring. Show how to call the function and what to expect as output.

6. **Notes and Additional Information (if needed)**: <br> Include any additional information, notes, or caveats that may be helpful for users of the function.

<br>
<p align="center">※※※※※※※※※※※※</p>

<h3>Using Sphinx for Documentation Generation:</h3>

While docstrings are essential for documenting code, you can use tools like Sphinx to generate user-friendly documentation from your docstrings. Sphinx allows you to create documentation in various formats, including HTML, PDF, and more.

Here's a brief overview of how to use Sphinx:

1. Install Sphinx:

   ```
   pip install sphinx
   ```

2. Create a Sphinx Project: <br> Use the `sphinx-quickstart` command to set up a new Sphinx documentation project. This command will generate the necessary configuration files and directory structure.

3. Write ReStructuredText (RST): <br> Sphinx uses ReStructuredText (RST) as its markup language. Write your documentation in `.rst` files using RST syntax.

4. Include Python Docstrings: <br> Sphinx can automatically extract documentation from your Python docstrings. Use the `autodoc` extension to enable this feature.

5. Build Documentation: <br> Use Sphinx's `make` commands (e.g., `make html` or `make pdf`) to build the documentation in the desired format.

6. Publish: <br> Once you've built the documentation, you can publish it online or distribute it with your code.
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
- [x] No
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
- [x] No
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
- [x] Yes
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
- [x] list with one element (any type)
- [x] not a list argument (ex: passing a dictionary to the method)
- [x] list with twice the same element (same type)
- [x] list with more than 2 times the same element (same type)
- [x] list with 2 different element (same type)
- [x] list with multiple types (integer, string, etc…)
- [x] empty list
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
- [x] Yes
</details>

<details>
<summary><h3>Question 6</h3></summary>

Is this a standardized way to comment a function in Python?
```py
/* Addition function */
def add(a, b):
    return a + b
```
- [x] No
- [ ] Yes
</details>

# Tasks
<details>
<summary>

### 0. Integers addition
`mandatory`

File: [0-add_integer.py](), [tests/0-add_integer.txt]()
</summary>

Write a function that adds 2 integers.

-   Prototype: `def add_integer(a, b=98):`
-   `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message `a must be an integer` or `b must be an integer`
-   `a` and `b` must be first casted to integers if they are float
-   Returns an integer: the addition of `a` and `b`
-   You are not allowed to import any module

```bash
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

```bash
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

```bash
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

### 3. Print square
`mandatory`

File: [4-print_square.py](), [tests/4-print_square.txt]()
</summary>

Write a function that prints a square with the character `#`.

-   Prototype: `def print_square(size):`
-   `size` is the size length of the square
-   `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
-   if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
-   if `size` is a float and is less than 0, raise a `TypeError` exception with the message `size must be an integer`
-   You are not allowed to import any module

```bash
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

### 4. Text indentation
`mandatory`

File: [5-text_indentation.py](), [tests/5-text_indentation.txt]()
</summary>

Write a function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`
- Prototype: `def text_indentation(text):`
- `text` must be a string, otherwise raise a `TypeError` exception with the message `text must be a string`
- There should be no space at the beginning or at the end of each printed line
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x07$ cat 5-main.py
#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")

guillaume@ubuntu:~/0x07$ ./5-main.py | cat -e
Lorem ipsum dolor sit amet, consectetur adipiscing elit.$
$
Quonam modo?$
$
Utrum igitur tibi litteram videor an totas paginas commovere?$
$
Non autem hoc:$
$
igitur ne illud quidem.$
$
Fortasse id optimum, sed ubi illud:$
$
Plus semper voluptatis?$
$
Teneo, inquit, finem illi videri nihil dolere.$
$
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.$
$
Si id dicis, vicimus.$
$
Inde sermone vario sex illa a Dipylo stadia confecimus.$
$
Sin aliud quid voles, postea.$
$
Quae animi affectio suum cuique tribuens atque hanc, quam dico.$
$
Utinam quidem dicerent alium alio beatiorem! Iam ruinas videresguillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/5-text_indentation.txt
guillaume@ubuntu:~/0x07$ 
```
</details>

<details>
<summary>

### 5. Max integer - Unittest
`mandatory`

File: [tests/6-max_integer_test.py]()
</summary>

Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

In this task, you will write unittests for the function `def max_integer(list=[]):`.
- Your test file should be inside a folder `tests`
- You have to use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- Your test file should be python files (extension: `.py`)
- Your test file should be executed by using this command: `python3 -m unittest tests.6-max_integer_test`
- All tests you make must be passable by the function below
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case
```bash
guillaume@ubuntu:~/0x07$ cat 6-max_integer.py
#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

guillaume@ubuntu:~/0x07$ 
guillaume@ubuntu:~/0x07$ cat 6-main.py
#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))
guillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ ./6-main.py
4
4
guillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ python3 -m unittest tests.6-max_integer_test 2>&1 | tail -1
OK
guillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ head -7 tests/6-max_integer_test.py 
#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
guillaume@ubuntu:~/0x07$ 
```
</details>

<details>
<summary>

### 6. Matrix multiplication
`#advanced`

File: [100-matrix_mul.py](), [tests/100-matrix_mul.txt]()
</summary>

Write a function that multiplies 2 matrices:

- Read: [Matrix multiplication - only Matrix product (two matrices)](https://en.wikipedia.org/wiki/Matrix_multiplication)

- Prototype: `def matrix_mul(m_a, m_b):`

- `m_a` and `m_b` must be validated with these requirements in this order

- `m_a` and `m_b` must be an list of lists of integers or floats:

    - if `m_a` or `m_b` is not a list: raise a `TypeError` exception with the message `m_a must be a list` or `m_b must be a list`
    - if `m_a` or `m_b` is not a list of lists: raise a `TypeError` exception with the message `m_a must be a list of lists` or `m_b must be a list of lists`
    - if `m_a` or `m_b` is empty (it means: `= []` or `= [[]]`): raise a `ValueError` exception with the message `m_a can't be empty or m_b can't be empty`
    - if one element of those list of lists is not an integer or a float: raise a `TypeError` exception with the message `m_a should contain only integers or floats` or `m_b should contain only integers or floats`
    - if `m_a` or `m_b` is not a rectangle (all ‘rows’ should be of the same size): raise a `TypeError` exception with the message `each row of m_a must be of the same size` or `each row of m_b must be of the same size`
- If `m_a` and `m_b` can’t be multiplied: raise a `ValueError` exception with the message `m_a and m_b can't be multiplied`

- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x07$ cat 100-main.py
#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

guillaume@ubuntu:~/0x07$ ./100-main.py 
[[7, 10], [15, 22]]
[[13, 16]]
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/100-matrix_mul.txt | tail -2
6 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ 
```
</details>

<details>
<summary>

### 7. Lazy matrix multiplication
`#advanced`

File: [101-lazy_matrix_mul.py](), [tests/101-lazy_matrix_mul.txt]()
</summary>

Write a function that multiplies 2 matrices by using the module [NumPy](https://numpy.org/)

To install it: `pip3 install numpy==1.15.0`
- Prototype: `def lazy_matrix_mul(m_a, m_b):`
- Test cases should be the same as `100-matrix_mul` but with new exception type/message
```bash
guillaume@ubuntu:~/0x07$ cat 101-main.py
#!/usr/bin/python3
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

guillaume@ubuntu:~/0x07$ ./101-main.py 
[[ 7 10]
 [15 22]]
[[13 16]]
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/101-lazy_matrix_mul.txt 
guillaume@ubuntu:~/0x07$ 
```
</details>

<details>
<summary>

### 8. CPython #3: Python Strings
`#advanced`

File: [102-python.c]()
</summary>

Create a function that prints Python strings.
- Prototype: `void print_python_string(PyObject *p);`
- Format: see example
- If `p` is not a valid string, print an error message (see example)
- Read: [Unicode HOWTO](https://docs.python.org/3.4/howto/unicode.html)

About:
- Python version: 3.4
- You are allowed to use the C standard library
- Your shared library will be compiled with this command line: `gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c`

```bash
julien@ubuntu:~/0x07. Pyhton Strings$ cat 102-tests.py
import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_string.argtypes = [ctypes.py_object]
s = "The spoon does not exist"
lib.print_python_string(s)
s = "ложка не существует"
lib.print_python_string(s)
s = "La cuillère n'existe pas"
lib.print_python_string(s)
s = "勺子不存在"
lib.print_python_string(s)
s = "숟가락은 존재하지 않는다."
lib.print_python_string(s)
s = "スプーンは存在しない"
lib.print_python_string(s)
s = b"The spoon does not exist"
lib.print_python_string(s)
julien@ubuntu:~/0x07. Pyhton Strings$ gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c
julien@ubuntu:~/0x07. Pyhton Strings$ python3 ./102-tests.py
[.] string object info
  type: compact ascii
  length: 24
  value: The spoon does not exist
[.] string object info
  type: compact unicode object
  length: 19
  value: ложка не существует
[.] string object info
  type: compact unicode object
  length: 24
  value: La cuillère n'existe pas
[.] string object info
  type: compact unicode object
  length: 5
  value: 勺子不存在
[.] string object info
  type: compact unicode object
  length: 14
  value: 숟가락은 존재하지 않는다.
[.] string object info
  type: compact unicode object
  length: 10
  value: スプーンは存在しない
[.] string object info
  [ERROR] Invalid String Object
julien@ubuntu:~/0x07. Pyhton Strings$ 
```
</details>