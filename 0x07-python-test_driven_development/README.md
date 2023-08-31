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
- [ ] No
- [ ] Yes
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

