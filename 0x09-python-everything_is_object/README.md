# **0x09. PYTHON - EVERYTHING IS OBJECT**
`Python` `OOP`

# Background Context
Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:
```py
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>> 
```
OK. But what about this?
```py
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>> 
```
This project is a little bit different than the usual projects. The first part is only questions about Python’s specificity like “What would be the result of…”. You should **read all documentation first (as usual :))**, then take the time to **think and brainstorm with your peers** about what you think and why. **Try to do this without coding anything for a few hours**.

Trying examples in the Python interpreter will give you most of the answers without having to think about it. **Don’t go this route**. First read, then think, then brainstorm together. Only then you can test in the interpreter.

It’s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types.

Note that during interviews for Python positions, **you will most likely have to answer to these type of questions**.

All your answers should be only one line in a file. No space before or after the answer.

# Resources
- [9.10. Objects and values](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values)
- [9.11. Aliasing](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing)
- [Immutable vs mutable types](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)
- [Mutation](https://www.composingprograms.com/pages/24-mutable-data.html) (*Only this chapter*)
- [9.12. Cloning lists](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists)
- [Python tuples: immutable but potentially changing](http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html)

<!-- man or help:
- `` -->

# Learning Objectives
<details>
<summary><h3>Why Python programming is awesome</h3></summary>
</details>

<details>
<summary><h3>What is an object</h3></summary>
</details>

<details>
<summary><h3>What is the difference between a class and an object or instance</h3></summary>
</details>

<details>
<summary><h3>What is the difference between immutable object and mutable object</h3></summary>
</details>

<details>
<summary><h3>What is a reference</h3></summary>
</details>

<details>
<summary><h3>What is an assignment</h3></summary>
</details>

<details>
<summary><h3>What is an alias</h3></summary>
</details>

<details>
<summary><h3>How to know if two variables are identical</h3></summary>
</details>

<details>
<summary><h3>How to know if two variables are linked to the same object</h3></summary>
</details>

<details>
<summary><h3>How to display the variable identifier (which is the memory address in the CPython implementation)</h3></summary>
</details>

<details>
<summary><h3>What is mutable and immutable</h3></summary>
</details>

<details>
<summary><h3>What are the built-in mutable types</h3></summary>
</details>

<details>
<summary><h3>What are the built-in immutable types</h3></summary>
</details>

<details>
<summary><h3>How does Python pass variables to functions</h3></summary>
</details>

# Requirements
<details>
<summary><h3>Python Scripts</h3></summary>

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a newline character
- The first line of all your script files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`
</details>

<details>
<summary><h3><code>.txt</code> Answer Files</h3></summary>

- Only one line
- No Shebang
- All your files should end with a new line
</details>

# Tasks
<details>
<summary>

### 0. Who am I?
`mandatory`

File: [0-answer.txt]()
</summary>

What function would you use to get the type of an object?

Write the name of the function in the file, without `()`.
</details>

<details>
<summary>

### 1. Where are you?
`mandatory`

File: [1-answer.txt]()
</summary>

How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without `()`.
</details>

<details>
<summary>

### 2. Right count
`mandatory`

File: [2-answer.txt]()
</summary>

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```py
>>> a = 89
>>> b = 100
```
</details>

<details>
<summary>

### 3. Right count =
`mandatory`

File: [3-answer.txt]()
</summary>

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```py
>>> a = 89
>>> b = 89
```

> In the provided code:<br>
   Both `a` and `b` are assigned the integer value `89`. In Python, integers are immutable objects. This means that every time you assign a variable to an integer, Python creates a new integer object in memory to represent that value.<br>
   So, in this case, both `a` and `b` are assigned to the same integer value `89`, but they are two separate objects in memory. They have the same value, but they are not pointing to the exact same object. However, they do refer to equivalent objects with the same value `89`.
</details>

<details>
<summary>

### 4. Right count =
`mandatory`

File: [4-answer.txt]()
</summary>

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```py
>>> a = 89
>>> b = a
```
</details>

<details>
<summary>

### 5. Right count =+
`mandatory`

File: [5-answer.txt]()
</summary>

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```py
>>> a = 89
>>> b = a + 1
```
</details>

<details>
<summary>

### 6. Is equal
`mandatory`

File: [6-answer.txt]()
</summary>

What do these 3 lines print?
```py
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```
</details>

<details>
<summary>

### 7. Is the same
`mandatory`

File: [7-answer.txt]()
</summary>

What do these 3 lines print?
```py
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```
</details>

<details>
<summary>

### 8. Is really equal
`mandatory`

File: [8-answer.txt]()
</summary>

What do these 3 lines print?
```py
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```
</details>

<details>
<summary>

### 9. Is really the same
`mandatory`

File: [9-answer.txt]()
</summary>

What do these 3 lines print?
```py
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```
</details>

<details>
<summary>

### 10. And with a list, is it equal
`mandatory`

File: [10-answer.txt]()
</summary>

What do these 3 lines print?
```py
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```
</details>

<details>
<summary>

### 11. And with a list, is it the same
`mandatory`

File: [11-answer.txt]()
</summary>

What do these 3 lines print?
```py
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```
</details>

<details>
<summary>

### 12. And with a list, is it really equal
`mandatory`

File: [12-answer.txt]()
</summary>

What do these 3 lines print?
```py
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```
</details>

<details>
<summary>

### 13. And with a list, is it really the same
`mandatory`

File: [13-answer.txt]()
</summary>

What do these 3 lines print?
```py
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```
</details>

<details>
<summary>

### 14. List append
`mandatory`

File: [14-answer.txt]()
</summary>

What does this script print?
```py
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```
</details>

<details>
<summary>

### 15. List add
`mandatory`

File: [15-answer.txt]()
</summary>

What does this script print?
```py
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```
</details>

<details>
<summary>

### 16. Integer incrementation
`mandatory`

File: [16-answer.txt]()
</summary>

What does this script print?
```py
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```
</details>

<details>
<summary>

### 17. List incrementation
`mandatory`

File: [17-answer.txt]()
</summary>

What does this script print?
```py
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```
</details>

<details>
<summary>

### 18. List assignation
`mandatory`

File: [18-answer.txt]()
</summary>

What does this script print?
```py
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```
</details>

<details>
<summary>

### 19. Copy a list object
`mandatory`

File: [19-copy_list.py]()
</summary>

Write a function `def copy_list(l):` that returns a **copy** of a list.

- The input list can contain any type of objects
- Your file should be maximum 3-line long (no documentation needed)
- You are not allowed to import any module
```py
guillaume@ubuntu:~/0x09$ cat 19-main.py
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

guillaume@ubuntu:~/0x09$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
guillaume@ubuntu:~/0x09$ wc -l 19-copy_list.py 
3 19-copy_list.py
guillaume@ubuntu:~/0x09$ 
```
**No test cases needed**
</details>

<details>
<summary>

### 20. Tuple or not?
`mandatory`

File: [20-answer.txt]()
</summary>

```py
a = ()
```
Is `a` a tuple? Answer with `Yes` or `No`.
</details>

<details>
<summary>

### 21. Tuple or not?
`mandatory`

File: [21-answer.txt]()
</summary>

```py
a = (1, 2)
```
Is `a` a tuple? Answer with `Yes` or `No`.
</details>

<details>
<summary>

### 22. Tuple or not?
`mandatory`

File: [22-answer.txt]()
</summary>

```py
a = (1)
```
Is `a` a tuple? Answer with `Yes` or `No`.
</details>

<details>
<summary>

### 23. Tuple or not?
`mandatory`

File: [23-answer.txt]()
</summary>

```py
a = (1, )
```
Is `a` a tuple? Answer with `Yes` or `No`.
</details>

<details>
<summary>

### 24. Who I am?
`mandatory`

File: [24-answer.txt]()
</summary>

What does this script print?
```py
a = (1)
b = (1)
a is b
```
</details>

<details>
<summary>

### 25. Tuple or not
`mandatory`

File: [25-answer.txt]()
</summary>

What does this script print?
```py
a = (1, 2)
b = (1, 2)
a is b
```
</details>

<details>
<summary>

### 26. Empty is not empty
`mandatory`

File: [26-answer.txt]()
</summary>

What does this script print?
```py
a = ()
b = ()
a is b
```
</details>

<details>
<summary>

### 27. Still the same?
`mandatory`

File: [27-answer.txt]()
</summary>

```py
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```
Will the last line of this script print `139926795932424`? Answer with `Yes` or `No`.
</details>

<details>
<summary>

### 28. Same or not?
`mandatory`

File: [28-answer.txt]()
</summary>

```py
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```
Will the last line of this script print `139926795932424`? Answer with `Yes` or `No`.
</details>

<details>
<summary>

### 29. #pythonic
`#advanced`

File: [100-magic_string.py]()
</summary>

Write a function `magic_string()` that returns a string “BestSchool” n times the number of the iteration (see code):
- Format: see example
- Your file should be maximum 4-line long (no documentation needed)
- You are not allowed to import any module
```py
guillaume@ubuntu:~/0x09$ cat 100-main.py
#!/usr/bin/python3
magic_string = __import__('100-magic_string').magic_string

for i in range(10):
    print(magic_string())

guillaume@ubuntu:~/0x09$ ./100-main.py | cat -e
BestSchool$
BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
guillaume@ubuntu:~/0x09$ wc -l 100-magic_string.py 
4 100-magic_string.py
guillaume@ubuntu:~/0x09$ 
```
**No test cases needed**
</details>

<details>
<summary>

### 30. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 31. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 32. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 33. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 34. 
`#advanced`

File: []()
</summary>


</details>

