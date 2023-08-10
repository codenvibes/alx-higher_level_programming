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

### Question #4
</summary>

What do these lines print?
```py
>>> def my_function(counter=89):
>>>     print("Counter: {}".format(counter))
>>> 
>>> my_function()
```
- [ ] Counter: 101
- [x] Counter: 89
- [ ] Counter: 12
</details>

<details>
<summary>

### Question #5
</summary>

What do these lines print?
```py
>>> def my_function():
>>>     print("In my function")
>>> 
>>> my_function()
```
- [ ] function my_function at …
- [ ] Nothing
- [x] In my function
- [ ] “In my function”
</details>

# Tasks
<details>
<summary>

### 0. Import a simple function from a simple file
`mandatory`

File: [0-add.py]()
</summary>

Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`

-   You have to use `print` function with string format to display integers
-   You have to assign:
    -   the value `1` to a variable called `a`
    -   the value `2` to a variable called `b`
    -   and use those two variables as arguments when calling the functions `add` and `print`
-   `a` and `b` must be defined in 2 different lines: `a = 1` and another `b = 2`
-   Your program should print: `<a value> + <b value> = <add(a, b) value>` followed with a new line
-   You can only use the word `add_0` once in your code
-   You are not allowed to use `*` for importing or `__import__`
-   Your code should not be executed when imported - by using `__import__`, like the example below

```bash
guillaume@ubuntu:~/0x02$ cat add_0.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

guillaume@ubuntu:~/0x02$ ./0-add.py
1 + 2 = 3
guillaume@ubuntu:~/0x02$ cat 0-import_add.py
__import__("0-add")
guillaume@ubuntu:~/0x02$ python3 0-import_add.py
guillaume@ubuntu:~/0x02$

```
</details>

<details>
<summary>

### 1. My first toolbox!
`mandatory`

File: [1-calculation.py]()
</summary>

Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result.

-   Do not use the function `print` (with string format to display integers) more than 4 times
-   You have to define:
    -   the value `10` to a variable `a`
    -   the value `5` to a variable `b`
    -   and use those two variables only, as arguments when calling functions (including `print`)
-   `a` and `b` must be defined in 2 different lines: `a = 10` and another `b = 5`
-   Your program should call each of the imported functions. See example below for format
-   the word `calculator_1` should be used only once in your file
-   You are not allowed to use `*` for importing or `__import__`
-   Your code should not be executed when imported

```bash
guillaume@ubuntu:~/0x02$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)

def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)

def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

guillaume@ubuntu:~/0x02$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
guillaume@ubuntu:~/0x02$

```
</details>

<details>
<summary>

### 2. How to make a script dynamic!
`mandatory`

File: [2-args.py]()
</summary>

Write a program that prints the number of and the list of its arguments.

-   The output should be:
    -   Number of argument(s) followed by `argument` (if number is one) or `arguments` (otherwise), followed by
    -   `:` (or `.` if no arguments were passed) followed by
    -   a new line, followed by (if at least one argument),
    -   one line per argument:
        -   the position of the argument (starting at `1`) followed by `:`, followed by the argument value and a new line
-   Your code should not be executed when imported
-   The number of elements of `argv` can be retrieved by using: `len(argv)`
-   You do not have to fully understand lists yet, but imagine that `argv` can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.

```bash
guillaume@ubuntu:~/0x02$ ./2-args.py
0 arguments.
guillaume@ubuntu:~/0x02$ ./2-args.py Hello
1 argument:
1: Hello
guillaume@ubuntu:~/0x02$ ./2-args.py Hello Welcome To The Best School
6 arguments:
1: Hello
2: Welcome
3: To
4: The
5: Best
6: School
guillaume@ubuntu:~/0x02$

```
</details>

<details>
<summary>

### 3. Infinite addition
`mandatory`

File: [3-infinite_add.py]()
</summary>

Write a program that prints the result of the addition of all arguments

-   The output should be the result of the addition of all arguments, followed by a new line
-   You can cast arguments into integers by using `int()` (you can assume that all arguments can be casted into integers)
-   Your code should not be executed when imported

```bash
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py
0
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10
89
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10 -40 -300 89
-162
guillaume@ubuntu:~/0x02$

```

Last but not least, your program should also handle big numbers. And the good news is: if your program works for the above example, it will work for the following example:

```bash
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 1111111111111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999990000000000000000000 11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334567788888899999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334568900000011111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999989999999999999999999
guillaume@ubuntu:~/0x02$

```

Remember how you did (or did not) do it in C? `#pythoniscool`
</details>

<details>
<summary>

### 4. Who are you?
`mandatory`

File: [4-hidden_discovery.py]()
</summary>

Write a program that prints all the names defined by the compiled module [hidden_4.pyc](https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc "hidden_4.pyc") (please download it locally).

-   You should print one name per line, in alpha order
-   You should print only names that do **not** start with `__`
-   Your code should not be executed when imported
-   Make sure you are running your code in Python3.8.x (`hidden_4.pyc` has been compiled with this version)

```bash
guillaume@ubuntu:~/0x02$ curl -Lso "hidden_4.pyc" "https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc"
guillaume@ubuntu:~/0x02$ ./4-hidden_discovery.py | sort
my_secret_santa
print_hidden
print_school
guillaume@ubuntu:~/0x02$

```
</details>

<details>
<summary>

### 5. Everything can be imported
`mandatory`

File: [5-variable_load.py]()
</summary>

Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value.

- You are not allowed to use `*` for importing or `__import__`
- Your code should not be executed when imported

```bash
guillaume@ubuntu:~/0x02$ cat variable_load_5.py
#!/usr/bin/python3
a = 98
"""Simple variable
"""

guillaume@ubuntu:~/0x02$ ./5-variable_load.py
98
guillaume@ubuntu:~/0x02$

```
</details>

<details>
<summary>

### 
``

File: []()
</summary>


</details>

<details>
<summary>

### 
``

File: []()
</summary>


</details>

<details>
<summary>

### 
``

File: []()
</summary>


</details>

<details>
<summary>

### 
``

File: []()
</summary>


</details>