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


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What are the map, reduce and filter functions</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<br>

## Requirements
<!-- Add your requirements here -->

<!-- <br>

## More Info -->

<br>

## Quiz questions
<details>
<summary><b>Question 0</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 1</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 2</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 3</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 4</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 5</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 6</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 7</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 8</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 9</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 10</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 11</b></summary><br>


<br>
</details>

<br>

## Tasks
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

<details>
<summary>

### 6. 
`mandatory`

File: []()
</summary>


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
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 14. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 15. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 16. 
`#advanced`

File: []()
</summary>


</details>

