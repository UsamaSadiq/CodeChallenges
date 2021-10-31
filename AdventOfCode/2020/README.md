# Advent Of Code 2020

## Summary of the Events/Challenges:

### **Event 01**

   Given a list of numbers, find product of numbers whose sum is given.
   - part 1: Given a list of numbers, find product of two numbers whose sum matches the given number.
   - part 2: Given a list of numbers, find product of three numbers whose sum matches the given number.

### **Event 02** 

   Given a list of passwords, find no. of passwords which match its given criteria.
   - part 1: Given a critera `1-3 a: abcde`, The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid.
   - part 2: Given a critera `1-3 a: abcde`, The password policy indicates that Exactly one of these positions must contain the given letter.

### **Event 03** 

   Given a map of trees(#) & open squares(.) and a slop pattern e.g. (right 3, down 1), calculate all the trees(#) found in the path starting from top-left corner and reaching till the bottom line.
```
..##.......   ---->
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....   ---->
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#   ---->
```
   - Given the map, find number of trees encountered using path `(3,1)`.
   - Given the map, find the product of number of trees encountered using paths `(1,1), (3,1), (5,1), (7,1), (1,2)`.

### **Event 04** 

   Given a batch file of passports, find no. of passports which are valid according to the given criteria.
   - part 1: Given the btach of data, find the number of passports which have all the required fields or only one optional field missing.
   - part 2: Given the batch of data, find the number of pasports which have all the required fields or onyl one optional field missing. The valid passports also need to pass validations for each field.

### **Event 05** 

   Given a batch file of passports, find what the highest seat ID is on a boarding pass?
   Use following details for the passport fields: 
   The airline uses binary space partitioning to seat people. A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".
   The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.
   Every seat also has a unique seat ID: multiply the row by 8, then add the column.