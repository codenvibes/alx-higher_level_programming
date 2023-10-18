<h1 align="center"><b>0x0E. SQL - MORE QUERIES</b></h1>
<div align="center"><code>SQL</code> <code>MySQL</code></div>

<br>
<div align="center">
<img width="300px" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/66988091.jpg">
</div>
<br>

<!-- # Background Context -->

# Resources
<details>
<summary><b><a href="https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql">How To Create a New User and Grant Permissions in MySQL</a></b></summary>


</details>

<details>
<summary><b><a href="https://www.mysqltutorial.org/mysql-grant.aspx">How To Use MySQL GRANT Statement To Grant Privileges To a User</a></b></summary>


</details>

<details>
<summary><b><a href="https://zetcode.com/mysql/constraints/">MySQL constraints</a></b></summary>


</details>

<details>
<summary><b><a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php">SQL technique: subqueries</a></b></summary>


</details>

<details>
<summary><b><a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/join.php">Basic query operation: the join</a></b></summary>


</details>

<details>
<summary><b><a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/multijoin.php">SQL technique: multiple joins and the distinct keyword</a></b></summary>


</details>

<details>
<summary><b><a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/jointypes.php">SQL technique: join types</a></b></summary>


</details>

<details>
<summary><b><a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/setops.php">SQL technique: union and minus</a></b></summary>


</details>

<details>
<summary><b><a href="https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US">MySQL Cheat Sheet</a></b></summary>


</details>

<details>
<summary><b><a href="https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html">The Seven Types of SQL Joins</a></b></summary>


</details>

<details>
<summary><b><a href="https://www.youtube.com/watch?v=yPu6qV5byu4">MySQL Tutorial</a></b></summary>


</details>

<details>
<summary><b><a href="https://www.sqlstyle.guide/">SQL Style Guide</a></b></summary>


</details>

<details>
<summary><b><a href="https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html">MySQL 8.0 SQL Statement Syntax</a></b></summary>


</details>

<br>
<b>Extra resources around relational database model design:</b>


<br>
<br>
<details>
<summary><b><a href="https://www.guru99.com/database-design.html">Design</a></b></summary>


</details>

<details>
<summary><b><a href="https://www.guru99.com/database-normalization.html">Normalization</a></b></summary>


</details>

<details>
<summary><b><a href="https://www.guru99.com/er-modeling.html">ER Modeling</a></b></summary>


</details>

<!-- **man or help:**
- `` -->

# Learning Objectives
<details>
<summary><b><a href=" "> </a>How to create a new MySQL user</b></summary>


</details>

<details>
<summary><b><a href=" "> </a>How to manage privileges for a user to a database or table</b></summary>


</details>

<details>
<summary><b><a href=" "> </a>What’s a <code>PRIMARY KEY</code></b></summary>


</details>

<details>
<summary><b><a href=" "> </a>What’s a <code>FOREIGN KEY</code></b></summary>


</details>

<details>
<summary><b><a href=" "> </a>How to use <code>NOT NULL</code> and <code>UNIQUE</code> constraints</b></summary>


</details>

<details>
<summary><b><a href=" "> </a>How to retrieve datas from multiple tables in one request</b></summary>


</details>

<details>
<summary><b><a href=" "> </a>What are subqueries</b></summary>


</details>

<details>
<summary><b><a href=" "> </a>What are <code>JOIN</code> and <code>UNION</code></b></summary>


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

<details>
<summary><b>How to import a SQL dump</b></summary><br>

```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

<br>
<img src="https://github.com/codenvibes/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/pics/bc2575fee3303b731031.png">

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

