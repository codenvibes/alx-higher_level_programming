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

</summary>

What function would you use to get the type of an object?

Write the name of the function in the file, without `()`.
</details>

<details>
<summary>

### 1. Where are you?
`mandatory`

</summary>

How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without `()`.
</details>

<details>
<summary>

### 2. Right count
`mandatory`

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

### 7. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 8. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 9. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 10. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 11. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 12. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 13. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 14. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 15. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 16. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 17. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 18. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 19. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 20. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 21. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 22. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 23. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 24. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 25. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 26. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 27. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 28. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 29. 
`#advanced`

File: []()
</summary>


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

