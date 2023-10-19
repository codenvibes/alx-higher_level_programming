-- A MYSQL script that computes the score average of all records in 'second_table' 

-- Calculate the average score.
SELECT AVG(score) AS average_score FROM second_table;

-- Add a new column to the table to store the average score.
ALTER TABLE second_table ADD COLUMN average DECIMAL;
