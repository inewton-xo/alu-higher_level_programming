-- LISTS THE RECORDS THAT HAVE A NAME.
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
