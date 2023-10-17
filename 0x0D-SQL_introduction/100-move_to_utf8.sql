-- Step 1: Convert the table "first_table" and the "name" field to UTF8MB4
USE hbtn_0c_0;
ALTER TABLE first_table
    CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table
    MODIFY COLUMN name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Step 2: Convert the database "hbtn_0c_0" to UTF8MB4
ALTER DATABASE hbtn_0c_0
    CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
