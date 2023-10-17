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
<summary><b>Install MySQL 8.0 on Ubuntu 20.04 LTS</b></summary>

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
<summary><b>Use “container-on-demand” to run MySQL</b></summary>

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


</details>

<details>
<summary><h3>Question 1</h3></summary>


</details>

<details>
<summary><h3>Question 2</h3></summary>


</details>

<details>
<summary><h3>Question 3</h3></summary>


</details>

<details>
<summary><h3>Question 4</h3></summary>


</details>

<details>
<summary><h3>Question 5</h3></summary>


</details>

<details>
<summary><h3>Question 6</h3></summary>


</details>

<details>
<summary><h3>Question 7</h3></summary>


</details>

<details>
<summary><h3>Question 8</h3></summary>


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
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 18. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 19. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 20. 
`#advanced`

File: []()
</summary>


</details>

