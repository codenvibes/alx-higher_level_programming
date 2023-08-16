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
<summary><h3>What are sets and how to use them</h3></summary>

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
</details>

<details>
<summary><h3>What are the most common methods of set and how to use them</h3></summary>

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
</details>

<details>
<summary><h3>When to use sets versus lists</h3></summary>

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
</details>

<details>
<summary><h3>How to iterate into a set</h3></summary>

You can iterate over the elements of a set using a `for` loop.

```python
for item in my_set:
    print(item)
```
</details>

<details>
<summary><h3>What are dictionaries and how to use them</h3></summary>
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
</details>

<details>
<summary><h3>When to use dictionaries versus lists or sets</h3></summary>

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
</details>

<details>
<summary><h3>What is a key in a dictionary</h3></summary>

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
</details>

<details>
<summary><h3>How to iterate over a dictionary</h3></summary>

1. **Iterating Through Keys:**
   
   You can iterate through the keys of a dictionary using a `for` loop. By default, iterating through a dictionary iterates over its keys.

   ```python
   student = {
       "name": "John",
       "age": 20,
       "major": "Computer Science"
   }

   for key in student:
       print(key, ":", student[key])
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
</details>

<details>
<summary><h3>What is a lambda function</h3></summary>
</details>

<details>
<summary><h3>What are the map, reduce and filter functions</h3></summary>
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
