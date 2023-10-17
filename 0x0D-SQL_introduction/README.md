<h1 align="center"><b>0x0D. SQL - INTRODUCTION</b></h1>
<div align="center"><code>SQL</code> <code>MySQL</code></div>

<!-- # Background Context -->

# Resources
<details>
<summary><b><a href="https://intranet.alxswe.com/concepts/37">Databases</a></b></summary>


</details>

<details>
<summary><b><a href="https://intranet.alxswe.com/concepts/556">Databases</a></b></summary>


</details>

<details>
<summary><b><a href="https://www.youtube.com/watch?v=FR4QIeZaPeM">What is Database & SQL?</a></b></summary>


</details>

<details>
<summary><b><a href="https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04">A Basic MySQL Tutorial</a></b></summary>


</details>

<details>
<summary><b><a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php">Basic SQL statements: DDL and DML</a> (no need to read the chapter “Privileges”)</b></summary>


</details>

<details>
<summary><b><a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php">Basic queries: SQL and RA</a></b></summary>


</details>

<details>
<summary><b><a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php">SQL technique: functions</a></b></summary>


</details>


<details>
<summary><b><a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php">SQL technique: subqueries</a></b></summary>


</details>

<details>
<summary><b><a href="https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458">What makes the big difference between a backtick and an apostrophe?</a></b></summary>


</details>

<details>
<summary><b><a href="https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US">MySQL Cheat Sheet</a></b></summary>


</details>

<details>
<summary><b><a href="https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html">MySQL 8.0 SQL Statement Syntax</a></b></summary>


</details>

<details>
<summary><b><a href="https://phoenixnap.com/kb/install-mysql-ubuntu-20-04">installing MySQL in Ubuntu 20.04</a></b></summary>


</details>

<!-- **man or help:**
- `` -->

# Learning Objectives
<details>
<summary><b><a href=" "></a>What’s a database</b></summary>


</details>

<details>
<summary><b><a href=" "></a>What’s a relational database</b></summary>


</details>

<details>
<summary><b><a href=" "></a>What does SQL stand for</b></summary>


</details>

<details>
<summary><b><a href=" "></a>What’s MySQL</b></summary>


</details>

<details>
<summary><b><a href=" "></a>How to create a database in MySQL</b></summary>


</details>

<details>
<summary><b><a href=" "></a>What does <code>DDL</code> and <code>DML</code> stand for</b></summary>


</details>

<details>
<summary><b><a href=" "></a>How to <code>CREATE</code> or <code>ALTER</code> a table</b></summary>


</details>

<details>
<summary><b><a href=" "></a>How to <code>SELECT</code> data from a table</b></summary>


</details>

<details>
<summary><b><a href=" "></a>How to <code>INSERT</code>, <code>UPDATE</code> or <code>DELETE</code> data</b></summary>


</details>

<details>
<summary><b><a href=" "></a>What are <code>subqueries</code></b></summary>


</details>

<details>
<summary><b><a href=" "></a>How to use MySQL functions</b></summary>


</details>

# Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0` (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

# More Info

<details>
<summary><b>Comments for your SQL file:</b></summary><br>

```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```
</details>

<details>
<summary><b>Install MySQL 8.0 on Ubuntu 20.04 LTS</b></summary><br>

```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```
Connect to your MySQL server:
```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```
</details>

<details>
<summary><b>Use “container-on-demand” to run MySQL</b></summary><br>

**In the container, credentials are `root/root`**

- Ask for container `Ubuntu 20.04`
- Connect via SSH
- OR connect via the Web terminal
- In the container, you should start MySQL before playing with it:
```
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
```
**In the container, credentials are `root/root`**
</details>

# Quiz questions
<details>
<summary><h3>Question 0</h3></summary>

How to you add a new record in the table `users`?
```
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
```
- [x] INSERT INTO users (id, name, age) VALUES (2, “Betty”, 30);
- [ ] INSERT INTO users (id, name, age) VALUES (2, “Betty”);
- [ ] INSERT INTO users (id, name) VALUES (2, “Betty”, 30);
- [ ] INSERT users (id, name, age) VALUES (2, “Betty”, 30);
</details>

<details>
<summary><h3>Question 1</h3></summary>

What does DDL stand for?
- [ ] Data Document Language
- [ ] Document Data Language
- [ ] Database Definition Language
- [x] Data Definition Language
</details>

<details>
<summary><h3>Question 2</h3></summary>

What is a relational database? (please select all correct answers)
- [x] a collection of data
- [x] a table containing only one object representation
- [x] data are organized by tables, records and columns
- [ ] data are organized by tables and indexes
- [ ] married databases
- [ ] a table containing multiple object representation
- [x] a database
</details>

<details>
<summary><h3>Question 3</h3></summary>

What does DML stand for?
- [x] Data Manipulation Language
- [ ] Document Model Language
- [ ] Document Manipulation Language
- [ ] Database Manipulation Language
</details>

<details>
<summary><h3>Question 4</h3></summary>

How do you list all `users` records with `age > 21` in this table?
```
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
```
- [x] SELECT * FROM users WHERE age > 21;
- [ ] SELECT * FROM users WHERE age BETWEEN 21 AND 89;
- [ ] SELECT * FROM users WHERE age IS UP TO 21;
- [ ] SELECT * FROM users WHERE age < 21;
</details>

<details>
<summary><h3>Question 5</h3></summary>

How do you delete the `users` record with `id = 89` in this table?
```
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
```
- [ ] DELETE FROM users;
- [ ] DELETE FROM users WHERE id IS EQUAL TO 89;
- [x] DELETE FROM users WHERE id = 89;
- [ ] DELETE users WHERE id = 89;
</details>

<details>
<summary><h3>Question 6</h3></summary>

How do you change the name of the `users` record with `id = 89` to `Holberton`?
```
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
```
- [ ] UPDATE users SET name = “Holberton”;
- [ ] CHANGE users SET name = “Holberton” WHERE id = 89;
- [x] UPDATE users SET name = “Holberton” WHERE id = 89;
</details>

<details>
<summary><h3>Question 7</h3></summary>

How do you list all `users` in this table?
```
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
```
- [ ] SELECT ALL users;
- [x] SELECT * FROM users;
- [ ] DELETE * FROM users;
</details>

<details>
<summary><h3>Question 8</h3></summary>

What does SQL stand for?
- [ ] Solid Query Language
- [ ] Structured Question Language
- [x] Structured Query Language
- [ ] Sequences of Query Logic
</details>

# Tasks
<details>
<summary>

### 0. List databases
`mandatory`

File: [0-list_databases.sql]()
</summary>

Write a script that lists all databases of your MySQL server.
```
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                     
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ 
```
</details>

<details>
<summary>

### 1. Create a database
`mandatory`

File: [1-create_database_if_missing.sql]()
</summary>


</details>

<details>
<summary>

### 2. Delete a database
`mandatory`

File: [2-remove_database.sql]()
</summary>


</details>

<details>
<summary>

### 3. List tables
`mandatory`

File: [3-list_tables.sql]()
</summary>


</details>

<details>
<summary>

### 4. First table
`mandatory`

File: [4-first_table.sql]()
</summary>


</details>

<details>
<summary>

### 5. Full description
`mandatory`

File: [5-full_table.sql]()
</summary>


</details>

<details>
<summary>

### 6. List all in table
`mandatory`

File: [6-list_values.sql]()
</summary>


</details>

<details>
<summary>

### 7. First add
`mandatory`

File: [7-insert_value.sql]()
</summary>


</details>

<details>
<summary>

### 8. Count 89
`mandatory`

File: [8-count_89.sql]()
</summary>


</details>

<details>
<summary>

### 9. Full creation
`mandatory`

File: [9-full_creation.sql]()
</summary>


</details>

<details>
<summary>

### 10. List by best
`mandatory`

File: [10-top_score.sql]()
</summary>


</details>

<details>
<summary>

### 11. Select the best
`mandatory`

File: [11-best_score.sql]()
</summary>


</details>

<details>
<summary>

### 12. Cheating is bad
`mandatory`

File: [12-no_cheating.sql]()
</summary>


</details>

<details>
<summary>

### 13. Score too low
`mandatory`

File: [13-change_class.sql]()
</summary>


</details>

<details>
<summary>

### 14. Average
`mandatory`

File: [14-average.sql]()
</summary>


</details>

<details>
<summary>

### 15. Number by score
`mandatory`

File: [15-groups.sql]()
</summary>


</details>

<details>
<summary>

### 16. Say my name
`mandatory`

File: [16-no_link.sql]()
</summary>


</details>

<details>
<summary>

### 17. Go to UTF8
`#advanced`

File: [100-move_to_utf8.sql]()
</summary>


</details>

<details>
<summary>

### 18. Temperatures #0
`#advanced`

File: [101-avg_temperatures.sql]()
</summary>


</details>

<details>
<summary>

### 19. Temperatures #1
`#advanced`

File: [102-top_city.sql]()
</summary>


</details>

<details>
<summary>

### 20. Temperatures #2
`#advanced`

File: [103-max_state.sql]()
</summary>


</details>

