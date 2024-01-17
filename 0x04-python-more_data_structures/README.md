<h1 align="center"><b>0x04. PYTHON-MORE_DATA_STRUCTURES</b></h1>
<div align="center"><code>Python</code></div>

<!-- <br>

## Background Context -->


<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->

<br>

## Resources
<details>
<summary><b><a href="https://docs.python.org/3/tutorial/datastructures.html">Data structures</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://python-course.eu/advanced-python/lambda-filter-reduce-map.php">Lambda, filter, reduce and map</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://www.youtube.com/watch?v=1GAC6KQUPeg">Learn to Program 12 Lambda Map Filter Reduce</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<br>

**man or help:**
- `python3`

<br>

## Learning Objectives
<details>
<summary><b><a href=" "></a>Why Python programming is awesome</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What are sets and how to use them</b></summary><br>

In Python, a set is a built-in data type that represents an unordered collection of unique elements. Sets are used to store multiple items, but unlike lists or tuples, sets do not allow duplicate values. They are implemented using a hash table, which enables efficient membership testing, insertion, and deletion of elements.

Here's how you can define and use sets in Python:

### Creating a Set

You can create a set by enclosing a comma-separated sequence of values in curly braces `{}`.

```python
# Creating a set
my_set = {1, 2, 3, 4, 5}
```

### Adding Elements to a Set

You can add elements to a set using the `add()` method.

```python
my_set.add(6)
```

### Removing Elements from a Set

You can remove elements from a set using the `remove()` method. If the element is not present, it will raise a `KeyError`. To avoid this, you can use the `discard()` method.

```python
my_set.remove(3)  # Raises an error if 3 is not in the set
my_set.discard(3)  # Removes 3 if it exists, otherwise does nothing
```

### Membership Testing

You can test if an element is present in a set using the `in` keyword.

```python
if 2 in my_set:
    print("2 is in the set")
```

### Set Comprehensions

You can also use set comprehensions to create sets in a concise way.

```python
squared_set = {x ** 2 for x in range(1, 6)}  # {1, 4, 9, 16, 25}
```

Sets are particularly useful when you want to store a collection of unique elements and perform operations like checking membership, finding intersections, and more, efficiently. Just keep in mind that sets are unordered, so their elements are not stored in any particular order.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What are the most common methods of set and how to use them</b></summary><br>

Sets in Python come with a variety of useful methods for performing operations on sets. Here are some of the most common set methods and how to use them:

1. **add()**: Adds an element to the set.

   ```python
   my_set = {1, 2, 3}
   my_set.add(4)
   # Resulting set: {1, 2, 3, 4}
   ```

2. **remove()**: Removes a specified element from the set. Raises an error if the element is not found.

   ```python
   my_set = {1, 2, 3}
   my_set.remove(2)
   # Resulting set: {1, 3}
   ```

3. **discard()**: Removes a specified element from the set. Does nothing if the element is not found.

   ```python
   my_set = {1, 2, 3}
   my_set.discard(2)
   # Resulting set: {1, 3}
   ```

4. **pop()**: Removes and returns an arbitrary element from the set. Useful if you want to remove an element without knowing its value.

   ```python
   my_set = {1, 2, 3}
   popped_value = my_set.pop()
   # Resulting set: {2, 3}
   ```

5. **clear()**: Removes all elements from the set, making it empty.

   ```python
   my_set = {1, 2, 3}
   my_set.clear()
   # Resulting set: {}
   ```

6. **union()**: Returns a new set containing all elements from the set and one or more other sets.

   ```python
   set1 = {1, 2, 3}
   set2 = {3, 4, 5}
   union_set = set1.union(set2)
   # Resulting set: {1, 2, 3, 4, 5}
   ```

7. **intersection()**: Returns a new set containing elements that are common to the set and one or more other sets.

   ```python
   set1 = {1, 2, 3}
   set2 = {3, 4, 5}
   intersection_set = set1.intersection(set2)
   # Resulting set: {3}
   ```

8. **difference()**: Returns a new set containing elements that are in the set but not in one or more other sets.

   ```python
   set1 = {1, 2, 3}
   set2 = {3, 4, 5}
   difference_set = set1.difference(set2)
   # Resulting set: {1, 2}
   ```

9. **symmetric_difference()**: Returns a new set containing elements that are in either of the sets, but not in both.

   ```python
   set1 = {1, 2, 3}
   set2 = {3, 4, 5}
   symmetric_diff_set = set1.symmetric_difference(set2)
   # Resulting set: {1, 2, 4, 5}
   ```

10. **issubset()** and **issuperset()**: Checks if one set is a subset or superset of another set.

    ```python
    set1 = {1, 2}
    set2 = {1, 2, 3, 4}
    is_subset = set1.issubset(set2)  # True
    is_superset = set2.issuperset(set1)  # True
    ```

These are just some of the most common methods available for sets in Python. Sets are very versatile data structures and can be combined with other set operations to perform more complex tasks efficiently.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>When to use sets versus lists</b></summary><br>

Choosing between sets and lists depends on the specific requirements of your program and the characteristics of the data you are working with. Here are some guidelines to help you decide when to use sets versus lists:

Use Sets When:

1. **Uniqueness Matters**: If you need to store a collection of elements where duplicates are not allowed, sets are the way to go. Sets automatically eliminate duplicate values, making them suitable for scenarios where uniqueness matters.
    > when checking membership using a set, the time it takes to determine whether an element is present doesn't significantly depend on the size of the set. This is because sets use hash tables to internally store and organize their elements, allowing for quick retrieval based on the hash of the element.

    > On the other hand, when checking membership using a list, the time it takes grows linearly with the number of elements in the list. This is because lists need to iterate through each element to determine if the element is present.

    > So, sets are much faster for membership testing, especially as the size of the data increases, making them a preferred choice when frequent membership checks are required.

2. **Membership Testing**: If you need to frequently check whether an element is present in a collection, sets are more efficient than lists. Sets use hash tables for fast membership testing, while lists require linear searching.

3. **Set Operations**: If you need to perform operations like union, intersection, difference, or symmetric difference between collections, sets provide built-in methods for these operations, making your code more concise and efficient.

4. **Mathematical Modeling**: If your program involves modeling mathematical sets, where the order of elements doesn't matter, and you need to perform set-based operations, sets are a natural choice.

5. **Removing Duplicates**: When you have a list with duplicate values and you want to remove duplicates while maintaining the order of the remaining elements, you can convert the list to a set, then back to a list.

Use Lists When:

1. **Order Matters**: If the order of elements is significant and you need to maintain the order of insertion, lists are the appropriate choice. Sets do not guarantee any specific order.

2. **Duplicates Are Allowed**: If your data can contain duplicate values and you want to preserve all occurrences, lists are the way to go. Sets automatically remove duplicates.

3. **Indexing and Slicing**: If you need to access elements by index or perform slicing operations, lists support these operations, whereas sets do not provide direct indexing.

4. **Data Retrieval and Manipulation**: If you frequently need to modify the content of your collection, like inserting, deleting, or replacing elements, lists offer more flexibility.

5. **Stable Iteration Order**: If you want to iterate through elements in a specific order (insertion order), lists are preferable, as sets do not guarantee any particular order during iteration.

In summary, use sets when you need to work with unique elements, perform efficient membership testing, and apply set-specific operations. Use lists when you require ordered elements, need to maintain duplicates, and want more flexibility in terms of element manipulation and access. Often, the choice between sets and lists depends on the nature of your data and the operations you'll perform on it.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to iterate into a set</b></summary><br>

You can iterate over the elements of a set using a `for` loop.

```python
for item in my_set:
    print(item)
```

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What are dictionaries and how to use them</b></summary><br>

In Python, a dictionary is a built-in data structure that allows you to store and manage data in key-value pairs. Each key in a dictionary maps to a corresponding value, similar to how words and their definitions are organized in a real-world dictionary. 

> Dictionaries are also sometimes referred to as "associative arrays" or "hash maps" in other programming languages.

Dictionaries are very useful when you want to store and retrieve data based on some unique identifier (the key). The keys in a dictionary must be unique and immutable (such as strings, numbers, or tuples), and the values can be of any data type (including other dictionaries or complex objects).

Here's how you create and use dictionaries in Python:

```python
# Creating a dictionary
student = {
    "name": "John",
    "age": 20,
    "major": "Computer Science"
}

# Accessing values using keys
print(student["name"])  # Output: John
print(student["age"])   # Output: 20

# Adding a new key-value pair
student["gpa"] = 3.8

# Modifying a value
student["age"] = 21

# Removing a key-value pair
del student["major"]

# Checking if a key exists
if "gpa" in student:
    print("GPA:", student["gpa"])
```

Dictionaries provide a flexible way to organize and manage data, especially when you need to quickly look up values based on keys. They are commonly used in various programming tasks, including configuration management, data processing, and more. Keep in mind that starting from Python 3.7, dictionary order is guaranteed to be insertion order, which means the order of key-value pairs is preserved.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>When to use dictionaries versus lists or sets</b></summary><br>

Dictionaries:
- Use dictionaries when you have data that needs to be stored and retrieved based on unique keys.
- Ideal for situations where you need fast lookups and associations between keys and values.
- Use cases: Storing configuration settings, mapping IDs to objects, managing data relationships, creating data structures for efficient searching, etc.

Here are some more specific scenarios to help guide your choice:
- If you need to associate values with keys, use a dictionary.
- If you need an ordered collection and will access elements by index, use a list.
- If you need to check for membership and ensure uniqueness, use a set.
- If you need both fast lookups and uniqueness, a dictionary or a set might be suitable depending on whether you need to associate values or not.

In many cases, you might find yourself using a combination of these data structures to build more complex data processing and storage solutions. Always consider the requirements of your specific problem and choose the data structure that best fits those requirements.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is a key in a dictionary</b></summary><br>

In a dictionary, a key is a unique identifier that is used to access and retrieve a corresponding value. Each key is associated with a specific value, forming a key-value pair within the dictionary. Keys must be unique and immutable, meaning they cannot be changed after they are created, and they cannot be duplicated within the same dictionary.

Here's a simple example of a dictionary with key-value pairs:

```python
student = {
    "name": "John",
    "age": 20,
    "major": "Computer Science"
}
```

In this example, `"name"`, `"age"`, and `"major"` are the keys, and `"John"`, `20`, and `"Computer Science"` are the corresponding values. You can use these keys to access the associated values within the dictionary:

```python
print(student["name"])  # Output: John
print(student["age"])   # Output: 20
```

Keys provide a way to uniquely identify and access data within a dictionary, making dictionaries highly efficient for fast lookups and retrieval of information based on specific identifiers.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to iterate over a dictionary</b></summary><br>

1. **Iterating Through Keys:**
   
   You can iterate through the keys of a dictionary using a `for` loop. By default, iterating through a dictionary iterates over its keys.

   ```python
   student = {
       "name": "John",
       "age": 20,
       "major": "Computer Science"
   }

   for key in student:
       print(key)
   ```
   output:
   ```
   name : John
   age : 23
   GPA : 3.5
   ```

2. **Iterating Through Keys and Values:**

   You can use the `.items()` method to iterate through both the keys and their corresponding values.

   ```python
   student = {
       "name": "John",
       "age": 20,
       "major": "Computer Science"
   }

   for key, value in student.items():
       print(key, ":", value)
   ```
   output:
   ```
   name : John
   age : 23
   GPA : 3.5
   ```

3. **Iterating Through Values:**

   While less common, you can also directly iterate through the values of a dictionary using the `.values()` method.

   ```python
   student = {
       "name": "John",
       "age": 20,
       "major": "Computer Science"
   }

   for value in student.values():
       print(value)
   ```
   output:
   ```
   John
   23
   3.5
   ```

4. **Iterating Through Items Using `enumerate()`:**

   If you want to access both the keys and values along with their indexes, you can use the `enumerate()` function.

   ```python
   student = {
       "name": "John",
       "age": 20,
       "major": "Computer Science"
   }

   for index, (key, value) in enumerate(student.items()):
       print(f"Item {index}: {key} - {value}")
   ```
   output:
   ```
   Item 0: name - John
   Item 1: age - 23
   Item 2: GPA - 3.5
   ```

Remember that dictionaries in Python 3.7 and later maintain insertion order, meaning the order of key-value pairs is preserved during iteration. However, in earlier versions of Python, dictionaries were not guaranteed to maintain this order.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is a lambda function</b></summary><br>

A lambda function in Python is a small, anonymous (unnamed) function that can have any number of arguments, but can only have one expression. Lambda functions are often used for simple operations where defining a full named function using the `def` keyword would be overkill.

Lambda functions are created using the `lambda` keyword, followed by the function's parameters and the expression that is evaluated and returned as the result of the function. The syntax is as follows:

```python
lambda arguments: expression
```

Here's a simple example of a lambda function that adds two numbers:

```python
add = lambda x, y: x + y
result = add(5, 3)
print(result)  # Output: 8
```

Lambda functions are commonly used in scenarios where you need a short, throwaway function for a specific purpose, such as in sorting operations, filtering data, or passing a function as an argument to another function like in the `map()` and `filter()` functions.

However, keep in mind that while lambda functions can be convenient for very simple tasks, using named functions with the `def` keyword is generally preferred for more complex or reusable code, as they provide better readability and can be more expressive.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What are the map, reduce and filter functions</b></summary><br>

`map()`, `filter()`, and `reduce()` are three built-in higher-order functions in Python that operate on sequences (lists, tuples, etc.) and are often used to perform operations on elements within these sequences. They are part of the `functools` module in Python 3.

1. **`map()` Function:**
   The `map()` function applies a given function to all items in a sequence (list, tuple, etc.) and returns an iterator with the results. The syntax is:
   
   ```python
   map(function, iterable)
   ```

   Example:
   
   ```python
   numbers = [1, 2, 3, 4]
   squared = map(lambda x: x ** 2, numbers)
   squared_list = list(squared)  # Convert iterator to list
   # squared_list: [1, 4, 9, 16]
   ```

2. **`filter()` Function:**
   The `filter()` function constructs a new sequence by filtering out items from an iterable based on a given function's boolean return value. It returns an iterator containing the elements for which the function returns `True`.
   
   ```python
   filter(function, iterable)
   ```

   Example:
   
   ```python
   numbers = [1, 2, 3, 4, 5, 6]
   even_numbers = filter(lambda x: x % 2 == 0, numbers)
   even_list = list(even_numbers)  # Convert iterator to list
   # even_list: [2, 4, 6]
   ```

3. **`reduce()` Function:**
   The `reduce()` function was originally a built-in function in Python 2, but it was moved to the `functools` module in Python 3. It applies a given function to the elements of an iterable in a cumulative way, reducing the sequence to a single value. To use `reduce()`, you need to import it separately:
   
   ```python
   from functools import reduce
   reduce(function, iterable, initializer)
   ```

   Example:
   
   ```python
   from functools import reduce
   numbers = [1, 2, 3, 4]
   product = reduce(lambda x, y: x * y, numbers)
   # product: 24
   ```

While these functions are useful, keep in mind that list comprehensions and generator expressions can often provide similar functionality in a more readable and concise way, especially for simple operations.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<br>

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`

<!-- <br>

## More Info -->

<br>

## Quiz questions
<details>
<summary><b>Question 0</b></summary><br>

What do these lines print?
```py
>>> for i in [1, 2, 3, 4]:
>>>     print(i, end=" ")
```
- [ ] 1 2 3
- [x] 1 2 3 4
- [ ] 0 1 2 3 5
- [ ] 0 1 2 3
<br>
</details>

<details>
<summary><b>Question 1</b></summary><br>

What do these lines print?
```py
>>> for i in [1, 3, 4, 2]:
>>>     print(i, end=" ")
```
- [x] 1 3 4 2
- [ ] 1 3 4 2 0
- [ ] 1 2 3 4
- [ ] 0 1 2 3
<br>
</details>

<details>
<summary><b>Question 2</b></summary><br>

What do these lines print?
```py
>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
>>> a.get('projects')[3]
```
- [ ] 3
- [ ] [3]
- [ ] [1, 2, 3, 4]
- [ ] [4]
- [x] 4
<br>
</details>

<details>
<summary><b>Question 3</b></summary><br>

What do these lines print?
```py
>>> a = { 'id': 89, 'name': "John" }
>>> a.get('age')
```
- [ ] 12
- [x] Nothing
- [ ] 89
- [ ] Not found
- [ ] ‘age’
<br>
</details>

<details>
<summary><b>Question 4</b></summary><br>

What do these lines print?
```py
>>> a = { 'id': 89, 'name': "John" }
>>> a.get('id')
```
- [x] 89
- [ ] John
- [ ] a[‘id’]
- [ ] ‘id’
- [ ] id
<br>
</details>

<details>
<summary><b>Question 5</b></summary><br>

What do these lines print?
```py
>>> for i in ["Hello", "Holberton", "School", 98]:
>>>     print(i, end=" ")
```
- [x] Hello Holberton School 98
- [ ] 1 2 3 4
- [ ] 0 1 2 3
<br>
</details>

<details>
<summary><b>Question 6</b></summary><br>

What do these lines print?
```py
>>> a = { 'id': 89, 'name': "John" }
>>> a.get('age', 0)
```
- [x] 0
- [ ] 89
- [ ] Nothing
- [ ] ‘age’
<details><summary>Explanation:</summary>

```python
a.get('age', 0)
```

This line uses the `get()` method of the dictionary `a`. The `get()` method retrieves the value associated with the specified key. If the key is not found in the dictionary, it returns the provided default value (which is the second argument to `get()`). In this case, the key `'age'` is not present in the dictionary `a`, so the method returns the default value `0`.
</details>
<br>
</details>

<details>
<summary><b>Question 7</b></summary><br>

What do these lines print?
```py
>>> for i in range(1, 4):
>>>     print(i, end=" ")
```
- [ ] 1 2 3 4
- [ ] 0 1 2 3
- [x] 1 2 3
<br>
</details>

<details>
<summary><b>Question 8</b></summary><br>

What do these lines print?
```py
>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4], 'friends': [ { 'id': 82, 'name': "Bob" }, { 'id': 83, 'name': "Amy" } ] }
>>> a.get('friends')[-1].get("name")
```
- [ ] Bob
- [ ] Nothing
- [x] Amy
- [ ] [ { ‘id’: 82, ‘name’: “Bob” }, { ‘id’: 83, ‘name’: “Amy” } ]
- [ ] 89
<br>
</details>

<details>
<summary><b>Question 9</b></summary><br>

What do these lines print?
```py
>>> for i in range(0, 3):
>>>     print(i, end=" ")
```
- [x] 0 1 2
- [ ] 0 1 2 3
- [ ] 1 2 3
<br>
</details>

<details>
<summary><b>Question 10</b></summary><br>

What do these lines print?
```py
>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
>>> a.get('projects')
```
- [ ] list
- [ ] Nothing
- [ ] [1]
- [x] [1, 2, 3, 4]
- [ ] ‘projects’
<br>
</details>

<details>
<summary><b>Question 11</b></summary><br>

What do these lines print?
```py
>>> a = { 'id': 89, 'name': "John" }
>>> a['id']
```
- [x] 89
- [ ] John
- [ ] a[‘id’]
- [ ] ‘id’
- [ ] id
<br>
</details>

<br>

## Tasks
<details>
<summary>

### 0. Squared simple
`mandatory`

File: [0-square_matrix_simple.py]()
</summary>

Write a function that computes the square value of all integers of a matrix.
- Prototype: `def square_matrix_simple(matrix=[])`:
- `matrix` is a 2 dimensional array
- Returns a new matrix:
    - Same size as `matrix`
    - Each value should be the square of the value of the input
- Initial matrix should not be modified
- You are not allowed to import any module
- You are allowed to use regular loops, `map`, etc.
```bash
guillaume@ubuntu:~/0x04$ cat 0-main.py
#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

guillaume@ubuntu:~/0x04$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
guillaume@ubuntu:~/0x04$
``` 
</details>

<details>
<summary>

### 1. Search and replace
`mandatory`

File: [1-search_replace.py]()
</summary>

Write a function that replaces all occurrences of an element by another in a new list.
- Prototype: `def search_replace(my_list, search, replace):`
- `my_list` is the initial list
- `search` is the element to replace in the list
- `replace` is the new element
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x04$ cat 1-main.py
#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x04$ ./1-main.py
[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
guillaume@ubuntu:~/0x04$ 
```
</details>

<details>
<summary>

### 2. Unique addition
`mandatory`

File: [2-uniq_add.py]()
</summary>

Write a function that adds all unique integers in a list (only once for each integer).
- Prototype: `def uniq_add(my_list=[]):`
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x04$ cat 2-main.py
#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))

guillaume@ubuntu:~/0x04$ ./2-main.py
Result: 15
guillaume@ubuntu:~/0x04$
```
</details>


<details>
<summary>

### 3. Present in both
`mandatory`

File: [3-common_elements.py]()
</summary>

Write a function that returns a set of common elements in two sets.
- Prototype: `def common_elements(set_1, set_2):`
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x04$ cat 3-main.py
#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

guillaume@ubuntu:~/0x04$ ./3-main.py
['C']
guillaume@ubuntu:~/0x04$ 
```
</details>

<details>
<summary>

### 4. Only differents
`mandatory`

File: [4-only_diff_elements.py]()
</summary>

Write a function that returns a set of all elements present in only one set.
- Prototype: `def only_diff_elements(set_1, set_2):`
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x04$ cat 4-main.py
#!/usr/bin/python3
only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))

guillaume@ubuntu:~/0x04$ ./4-main.py
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
guillaume@ubuntu:~/0x04$ 
```
</details>

<details>
<summary>

### 5. Number of keys
`mandatory`

File: [5-number_keys.py]()
</summary>

Write a function that returns the number of keys in a dictionary.
- Prototype: `def number_keys(a_dictionary):`
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x04$ cat 5-main.py
#!/usr/bin/python3
number_keys = __import__('5-number_keys').number_keys

a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))

guillaume@ubuntu:~/0x04$ ./5-main.py
Number of keys: 3
guillaume@ubuntu:~/0x04$ 
```
</details>

<details>
<summary>

### 6. Print sorted dictionary
`mandatory`

File: [6-print_sorted_dictionary.py]()
</summary>

Write a function that prints a dictionary by ordered keys.
- Prototype: `def print_sorted_dictionary(a_dictionary):`
- You can assume that all keys are strings
- Keys should be sorted by alphabetic order
- Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
- Dictionary values can have any type
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x04$ cat 6-main.py
#!/usr/bin/python3
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)

guillaume@ubuntu:~/0x04$ ./6-main.py
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
guillaume@ubuntu:~/0x04$ 
```
</details>

<details>
<summary>

### 7. Update dictionary
`mandatory`

File: [7-update_dictionary.py]()
</summary>

Write a function that replaces or adds key/value in a dictionary.
- Prototype: `def update_dictionary(a_dictionary, key, value):`
- `key` argument will be always a string
- `value` argument will be any type
- If a key exists in the dictionary, the value will be replaced
- If a key doesn’t exist in the dictionary, it will be created
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x04$ cat 7-main.py
#!/usr/bin/python3
update_dictionary = __import__('7-update_dictionary').update_dictionary
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

guillaume@ubuntu:~/0x04$ ./7-main.py
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level
--
--
city: San Francisco
language: Python
number: 89
track: Low level
--
city: San Francisco
language: Python
number: 89
track: Low level
guillaume@ubuntu:~/0x04$ 
```
</details>

<details>
<summary>

### 8. Simple delete by key
`mandatory`

File: [8-simple_delete.py]()
</summary>

Write a function that deletes a key in a dictionary.
- Prototype: `def simple_delete(a_dictionary, key=""):`
- `key` argument will be always a string
- If a key doesn’t exist, the dictionary won’t change
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x04$ cat 8-main.py
#!/usr/bin/python3
simple_delete = __import__('8-simple_delete').simple_delete
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
new_dict = simple_delete(a_dictionary, 'track')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = simple_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

guillaume@ubuntu:~/0x04$ ./8-main.py
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
--
--
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
guillaume@ubuntu:~/0x04$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x04-python-more_data_structures
File: 8-simple_delete.py
```
</details>

<details>
<summary>

### 9. Multiply by 2
`mandatory`

File: [9-multiply_by_2.py]()
</summary>

Write a function that returns a new dictionary with all values multiplied by 2
- Prototype: `def multiply_by_2(a_dictionary):`
- You can assume that all values are only integers
- Returns a new dictionary
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x04$ cat 9-main.py
#!/usr/bin/python3
multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

guillaume@ubuntu:~/0x04$ ./9-main.py
Alex: 8
Bob: 14
John: 12
Mike: 14
Molly: 16
--
Alex: 16
Bob: 28
John: 24
Mike: 28
Molly: 32
guillaume@ubuntu:~/0x04$ 
```
</details>

<details>
<summary>

### 10. Best score
`mandatory`

File: [10-best_score.py]()
</summary>

Write a function that returns a key with the biggest integer value.
- Prototype: `def best_score(a_dictionary):`
- You can assume that all values are only integers
- If no score found, return `None`
- You can assume all students have a different score
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x04$ cat 10-main.py
#!/usr/bin/python3
best_score = __import__('10-best_score').best_score

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))

guillaume@ubuntu:~/0x04$ ./10-main.py
Best score: Molly
Best score: None
guillaume@ubuntu:~/0x04$ 
```
</details>

<details>
<summary>

### 11. Multiply by using map
`mandatory`

File: [11-multiply_list_map.py]()
</summary>

Write a function that returns a list with all values multiplied by a number without using any loops.
- Prototype: `def multiply_list_map(my_list=[], number=0):`
- Returns a new list:
    - Same length as `my_list`
    - Each value should be multiplied by `number`
- Initial list should not be modified
- You are not allowed to import any module
- You have to use `map`
- Your file should be max 3 lines
```bash
guillaume@ubuntu:~/0x04$ cat 11-main.py
#!/usr/bin/python3
multiply_list_map = __import__('11-multiply_list_map').multiply_list_map

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)

guillaume@ubuntu:~/0x04$ ./11-main.py
[4, 8, 12, 16, 24]
[1, 2, 3, 4, 6]
guillaume@ubuntu:~/0x04$ 
```
</details>

<details>
<summary>

### 12. Roman to Integer
`mandatory`

File: [12-roman_to_int.py]()
</summary>

**Technical interview preparation:**
- You are not allowed to google anything
- Whiteboard first
Create a function `def roman_to_int(roman_string):` that converts a R[oman numeral](https://en.wikipedia.org/wiki/Roman_numerals) to an integer.
- You can assume the number will be between 1 to 3999.
- `def roman_to_int(roman_string)` must return an integer
- If the `roman_string` is not a string or `None`, return 0
```bash
guillaume@ubuntu:~/0x04$ cat 12-main.py
#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

guillaume@ubuntu:~/0x04$ ./12-main.py
X = 10
VII = 7
IX = 9
LXXXVII = 87
DCCVII = 707
guillaume@ubuntu:~/0x04$ 
```
</details>

<details>
<summary>

### 13. Weighted average!
`#advanced`

File: [100-weight_average.py]()
</summary>

Write a function that returns the weighted average of all integers tuple `(<score>, <weight>)`
- Prototype: `def weight_average(my_list=[]):`
- Returns `0` if the list is empty
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x04$ cat 100-main.py
#!/usr/bin/python3
weight_average = __import__('100-weight_average').weight_average

my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))

guillaume@ubuntu:~/0x04$ ./100-main.py
Average: 2.80
guillaume@ubuntu:~/0x04$ 
```
</details>

<details>
<summary>

### 14. Squared by using map
`#advanced`

File: [101-square_matrix_map.py]()
</summary>

Write a function that computes the square value of all integers of a matrix using `map`
- Prototype: `def square_matrix_map(matrix=[]):`
- `matrix` is a 2 dimensional array
- Returns a new matrix:
    - Same size as `matrix`
    - Each value should be the square of the value of the input
- Initial matrix should not be modified
- You are not allowed to import any module
- You have to use `map`
- You are not allowed to use `for` or `while`
- Your file should be max 3 lines
```bash
guillaume@ubuntu:~/0x04$ cat 101-main.py
#!/usr/bin/python3
square_matrix_map = \
    __import__('101-square_matrix_map').square_matrix_map

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_map(matrix)
print(new_matrix)
print(matrix)

guillaume@ubuntu:~/0x04$ ./101-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
guillaume@ubuntu:~/0x04$ 
```
</details>

<details>
<summary>

### 15. Delete by value
`#advanced`

File: [102-complex_delete.py]()
</summary>

Write a function that deletes keys with a specific value in a dictionary.
- Prototype: `def complex_delete(a_dictionary, value):`
- If the value doesn’t exist, the dictionary won’t change
- All keys having the searched value have to be deleted
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x04$ cat 102-main.py
#!/usr/bin/python3
complex_delete = __import__('102-complex_delete').complex_delete
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
new_dict = complex_delete(a_dictionary, 'C')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = complex_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

guillaume@ubuntu:~/0x04$ ./102-main.py
ids: [1, 2, 3]
track: Low
--
ids: [1, 2, 3]
track: Low
--
--
ids: [1, 2, 3]
track: Low
--
ids: [1, 2, 3]
track: Low
guillaume@ubuntu:~/0x04$ 
```
</details>

<details>
<summary>

### 16. CPython #1: PyBytesObject
`#advanced`

File: [103-python.c]()
</summary>

Create two C functions that print some basic info about Python lists and Python bytes objects.

Python lists:
- Prototype: `void print_python_list(PyObject *p);`
- Format: see example

Python bytes:
- Prototype: `void print_python_bytes(PyObject *p);`
- Format: see example
- Line “first X bytes”: print a maximum of 10 bytes
- If p is not a valid `PyBytesObject`, print an error message (see example)
- Read `/usr/include/python3.4/bytesobject.h`

About:
- Python version: 3.4
- Your shared library will be compiled with this command line: `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c`
- You are not allowed to use the following macros/functions:
    - `Py_SIZE`
    - `Py_TYPE`
    - `PyList_GetItem`
    - `PyBytes_AS_STRING`
    - `PyBytes_GET_SIZE`
```bash
julien@ubuntu:~/CPython$ python3 --version
Python 3.4.3
julien@ubuntu:~/CPython$ gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c
julien@ubuntu:~/CPython$ cat 103-tests.py 
import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
s = b"Hello"
lib.print_python_bytes(s);
b = b'\xff\xf8\x00\x00\x00\x00\x00\x00';
lib.print_python_bytes(b);
b = b'What does the \'b\' character do in front of a string literal?';
lib.print_python_bytes(b);
l = [b'Hello', b'World']
lib.print_python_list(l)
del l[1]
lib.print_python_list(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], b"Holberton", "Betty"]
lib.print_python_list(l)
l = []
lib.print_python_list(l)
l.append(0)
lib.print_python_list(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list(l)
l.pop()
lib.print_python_list(l)
l = ["Holberton"]
lib.print_python_list(l)
lib.print_python_bytes(l);
julien@ubuntu:~/CPython$ python3 103-tests.py 
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[.] bytes object info
  size: 8
  trying string: �
  first 9 bytes: ff f8 00 00 00 00 00 00 00
[.] bytes object info
  size: 60
  trying string: What does the 'b' character do in front of a string literal?
  first 10 bytes: 57 68 61 74 20 64 6f 65 73 20
[*] Python list info
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
Element 1: bytes
[.] bytes object info
  size: 5
  trying string: World
  first 6 bytes: 57 6f 72 6c 64 00
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 2
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[*] Python list info
[*] Size of the Python List = 8
[*] Allocated = 8
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
Element 1: int
Element 2: int
Element 3: float
Element 4: tuple
Element 5: list
Element 6: bytes
[.] bytes object info
  size: 9
  trying string: Holberton
  first 10 bytes: 48 6f 6c 62 65 72 74 6f 6e 00
Element 7: str
[*] Python list info
[*] Size of the Python List = 0
[*] Allocated = 0
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 4
Element 0: int
[*] Python list info
[*] Size of the Python List = 5
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
Element 4: int
[*] Python list info
[*] Size of the Python List = 4
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 1
Element 0: str
[.] bytes object info
  [ERROR] Invalid Bytes Object
julien@ubuntu:~/CPython$ 
```
</details>
