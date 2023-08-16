# **0x04-PYTHON-MORE_DATA_STRUCTURES**
`Python`

# Resources
- [Data structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Lambda, filter, reduce and map](https://python-course.eu/advanced-python/lambda-filter-reduce-map.php)
- [Learn to Program 12 Lambda Map Filter Reduce](https://www.youtube.com/watch?v=1GAC6KQUPeg)

man or help:
- `python3`

# Learning Objectives
<details>
<summary>What are sets and how to use them</summary><br>
</details>

<details>
<summary>What are the most common methods of set and how to use them</summary><br>
</details>

<details>
<summary>When to use sets versus lists</summary><br>
</details>

<details>
<summary>How to iterate into a set</summary><br>
</details>

<details>
<summary>What are dictionaries and how to use them</summary><br>
</details>

<details>
<summary>When to use dictionaries versus lists or sets</summary><br>
</details>

<details>
<summary>What is a key in a dictionary</summary><br>
</details>

<details>
<summary>How to iterate over a dictionary</summary><br>
</details>

<details>
<summary>What is a lambda function</summary><br>
</details>

<details>
<summary>What are the map, reduce and filter functions</summary><br>
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

# Quiz questions
<details>
<summary><h3>Question #0</h3></summary>

What do these lines print?
```py
>>> for i in [1, 2, 3, 4]:
>>>     print(i, end=" ")
```
- [ ] 1 2 3
- [ ] 1 2 3 4
- [ ] 0 1 2 3 5
- [ ] 0 1 2 3
</details>

<details>
<summary><h3>Question #1</h3></summary>

What do these lines print?
```py
>>> for i in [1, 3, 4, 2]:
>>>     print(i, end=" ")
```
- [ ] 1 3 4 2
- [ ] 1 3 4 2 0
- [ ] 1 2 3 4
- [ ] 0 1 2 3
</details>

<details>
<summary><h3>Question #2</h3></summary>

What do these lines print?
```py
>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
>>> a.get('projects')[3]
```
- [ ] 3
- [ ] [3]
- [ ] [1, 2, 3, 4]
- [ ] [4]
- [ ] 4
</details>

<details>
<summary><h3>Question #3</h3></summary>

What do these lines print?
```py
>>> a = { 'id': 89, 'name': "John" }
>>> a.get('age')
```
- [ ] 12
- [ ] Nothing
- [ ] 89
- [ ] Not found
- [ ] ‘age’
</details>

<details>
<summary><h3>Question #4</h3></summary>

What do these lines print?
```py
>>> a = { 'id': 89, 'name': "John" }
>>> a.get('id')
```
- [ ] 89
- [ ] John
- [ ] a[‘id’]
- [ ] ‘id’
- [ ] id
</details>

<details>
<summary><h3>Question #5</h3></summary>

What do these lines print?
```py
>>> for i in ["Hello", "Holberton", "School", 98]:
>>>     print(i, end=" ")
```
- [ ] Hello Holberton School 98
- [ ] 1 2 3 4
- [ ] 0 1 2 3
</details>

<details>
<summary><h3>Question #6</h3></summary>

What do these lines print?
```py
>>> a = { 'id': 89, 'name': "John" }
>>> a.get('age', 0)
```
- [ ] 0
- [ ] 89
- [ ] Nothing
- [ ] ‘age’
</details>

<details>
<summary><h3>Question #7</h3></summary>

What do these lines print?
```py
>>> for i in range(1, 4):
>>>     print(i, end=" ")
```
- [ ] 1 2 3 4
- [ ] 0 1 2 3
- [ ] 1 2 3
</details>

<details>
<summary><h3>Question #8</h3></summary>

What do these lines print?
```py
>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4], 'friends': [ { 'id': 82, 'name': "Bob" }, { 'id': 83, 'name': "Amy" } ] }
>>> a.get('friends')[-1].get("name")
```
- [ ] Bob
- [ ] Nothing
- [ ] Amy
- [ ] [ { ‘id’: 82, ‘name’: “Bob” }, { ‘id’: 83, ‘name’: “Amy” } ]
- [ ] 89
</details>

<details>
<summary><h3>Question #9</h3></summary>

What do these lines print?
```py
>>> for i in range(0, 3):
>>>     print(i, end=" ")
```
- [ ] 0 1 2
- [ ] 0 1 2 3
- [ ] 1 2 3
</details>

<details>
<summary><h3>Question #10</h3></summary>

What do these lines print?
```py
>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
>>> a.get('projects')
```
- [ ] list
- [ ] Nothing
- [ ] [1]
- [ ] [1, 2, 3, 4]
- [ ] ‘projects’
</details>

<details>
<summary><h3>Question #11</h3></summary>

What do these lines print?
```py
>>> a = { 'id': 89, 'name': "John" }
>>> a['id']
```
- [ ] 89
- [ ] John
- [ ] a[‘id’]
- [ ] ‘id’
- [ ] id
</details>

# Tasks
<details>
<summary>

### 
`mandatory`

File: []()
</summary>


</details>
