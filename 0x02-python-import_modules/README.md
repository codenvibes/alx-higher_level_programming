# **0x02-PYTHON-IMPORT_MODULES**
`Python`

# Resources
- [Modules](https://docs.python.org/3/tutorial/modules.html)
- [Command line arguments](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)
- [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

man or help:
- `python3`

# Learning Objectives
- Why Python programming is awesome
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function `dir()`
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs

# Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`

# Quiz questions
<details>
<summary>

### Question #0
</summary>

What do these lines print?
```py
>>> def my_function(counter=89):
>>>     return counter + 1
>>> 
>>> print(my_function())
```
- [x] 90
- [ ] 891
- [ ] 89
- [ ] 1
</details>

<details>
<summary>

### Question #1
</summary>

What do these lines print?
```py
>>> def my_function(counter):
>>>     print("Counter: {}".format(counter))
>>> 
>>> my_function(12)
```
- [x] Counter: 12
- [ ] Counter: c
- [ ] Counter: counter
</details>

<details>
<summary>

### Question #2
</summary>

What do these lines print?
```py
>>> def my_function():
>>>     print("In my function")
>>> 
>>> my_function
```
- [x] function my_function at …
- [ ] Nothing
- [ ] In my function
- [ ] “In my function”

<details>
<summary>Description:</summary>

In Python, when you reference a function without parentheses `()`, you're referring to the function object itself, not invoking the function. So, the output of the provided code will be:
```bash
<function my_function at 0x...>
```
The exact memory address (0x...) will vary depending on the system you're running the code on.
</details>
</details>

<details>
<summary>

### Question #3
</summary>

What do these lines print?
```py
>>> def my_function(counter=89):
>>>     print("Counter: {}".format(counter))
>>> 
>>> my_function(12)
```
- [ ] Counter: 101
- [ ] Counter: 89
- [x] Counter: 12
<details>
<summary>Description:</summary>

The provided code defines a function `my_function `with a default parameter `counter` set to `89`. When the function is called with an argument, the argument value overrides the default value of the parameter. Then, it calls the function with an argument `12`.
</details>
</details>

<details>
<summary>

### 
</summary>


</details>

<details>
<summary>

### 
</summary>


</details>
