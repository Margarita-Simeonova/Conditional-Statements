## Conditional Statements

# Logical expressions and checks. Conditional construction if - else.

## Conditional Statements - Lab

### Tasks:

1. Excellent result:
   
Write a console program that reads a grade (a real number) entered by the user and prints "Excellent!" if the grade is 5.50 or higher.

########

2. The largest number:
   
To write a program that reads two integers entered by the user and prints the larger of the two.

########

3. Even or odd:
   
To write a program that reads an integer entered by the user and prints whether it is even or odd. 
If even print "even", if odd print "odd".

########

4. Guess the password:
   
To write a program that reads a password (text) entered by the user and checks whether the entered password matches the phrase "s3cr3t!P@ssw0rd". If there is a match, display "Welcome". In case of mismatch, display "Wrong password!".

########

5. A number from 100 to 200:
   
Write a program that reads an integer entered by the user and checks whether it is less than 100, between 100 and 200, or greater than 200.

 If the number is:
 
 • under 100 print: "Less than 100"
 
 • between 100 and 200 print: "Between 100 and 200"
 
 • greater than 200 print: "Greater than 200"

########

6. Speed ​​information:
   
To write a program that reads a speed (real number) entered by the user and prints the speed information.

 • For speed up to 10 (inclusive) print "slow"
 
 • For speed above 10 and up to 50 (inclusive) print "average"
 
 • For speed over 50 and up to 150 (inclusive) print "fast"
 
 • For speed over 150 and up to 1000 (inclusive) print "ultra fast"
 
 • For higher speed, print "extremely fast"

########

7. Faces of figures:
   
To write a program in which the user enters the type and dimensions of a geometric figure and calculates its face. There are four types of figures: square, rectangle, circle and triangle. The first line of the input reads the type of figure (text with the following options: square, rectangle, circle or triangle).
 • If the figure is a square: a fractional number is read on the next line - the length of its side
 
 • If the figure is a rectangle: on the next two lines read two fractional numbers - the lengths of its sides
 
 • If the figure is a circle: on the next line read a fractional number - the radius of the circle
 
 • If the figure is a triangle: on the next two lines read two fractional numbers - the length of its side and the length of the height to it
Round the result to 3 decimal places.


# Conditional Statements - Exercise

1. Addition of seconds:
   
Three sports competitors finish in some number of seconds (between 1 and 50). To write a program that reads the times of the competitors in seconds entered by the user and calculates their total time in "minutes:seconds" format. Display seconds with a leading zero (2 -> "02", 7 -> "07", 35 -> "35").

########

2. Bonus points:
   
Given an integer - initial number of points. Bonus points are accrued on it according to the rules described below. To write a program that calculates the bonus points that the number receives and the total number of points (the number + the bonus).

 • If the number is up to and including 100, the bonus points are 5;
 
 • If the number is greater than 100, the bonus points are 20% of the number;
 
 • If the number is greater than 1000, the bonus points are 10% of the number.

Additional bonus points (charged separately from the previous ones):
 
 ◦ For an even number -> + 1 pt.
 
 ◦ For a number that ends in 5 -> + 2 pts.

########

3. Time + 15 minutes:
   
To write a program that reads the hour and minutes of a 24-hour day entered by the user and calculates what the time will be in 15 minutes. Print the result in hours:minutes format. Hours are always between 0 and 23 and minutes are always between 0 and 59. Hours are written as one or two digits. Minutes are always written as two digits, with a leading zero when necessary.

########

5. Children's toy store:
   
Petya has a children's toy shop. She gets a big order to fulfill. With the money he will earn, he wants to go on an excursion.

Toy prices:

 • Puzzle - BGN 2.60
 
 • Talking doll - BGN 3
 
 • Teddy bear - BGN 4.10
 
 • Mignon - BGN 8.20
 
 • Truck - BGN 2
 
 If the ordered toys are 50 or more, the store makes a discount of 25% of the total price. From the money earned, Petya must give 10% for the rent of the shop. To calculate whether the money will be enough for her to go on an excursion.

Input:

6 lines are read from the console:
 1. Excursion price - a real number
 2. Number of puzzles - an integer
 3. Number of talking dolls - an integer
 4. Number of teddy bears - an integer
 5. Number of minions - an integer
 6. Number of trucks - an integer
    
Output:

The console prints:

 • If the money is sufficient, the following is printed:
 ◦ "Yes! {remaining money} lv left."
 • If the money is NOT enough, the following is printed:
 ◦ "Not enough money! lv needed."

The result must be formatted to the second decimal place.

########

6. World record in swimming:
   
Ivan decides to improve the World Record in long distance swimming. Enter the record in seconds that Ivan has to beat, the distance in meters that he has to swim, and the time in seconds that he swims 1 m on the console. Write a program that calculates whether he has completed the task by it is meant that: water resistance slows it down every 15 m by 12.5 seconds. When calculating how many times Ivancho will slow down due to water resistance, the result should be rounded down to the nearest whole number.
To calculate the time in seconds that Ivancho will take to swim the distance and the difference to the World Record.

Input:

3 lines are read from the console:
 1. The record in seconds – a real number;
 2. The distance in meters – a real number;
 3. The time in seconds for which he swims a distance of 1 m. - a real number.
Exit
Printing to the console depends on the result:

 • If Ivan has improved the World Record (his time is less than the record) we print:

      "Yes, he succeeded! The new world record is {Ivan's time} seconds."
    
 • If he did NOT beat the record (his time is greater than or equal to the record) we print:
 
      "No, he failed! He was {missing seconds} seconds slower."
      
The result must be formatted to the second decimal place.

########

7. Shopping:
   
Peter wants to buy N video cards, M processors and P number of RAM. If the number of video cards is greater than the number of processors, you get a 15% discount on the final bill. The following prices apply:

 • Video card – BGN 250/pc.
 
 • Processor – 35% of the price of purchased video cards/pcs.
 
 • RAM memory – 10% of the price of purchased video cards/pcs.
 
To calculate the amount needed to purchase the materials and to calculate whether the budget will be enough.

Input:

The input consists of four lines:

 1. Peter's budget - a real
 2. The number of video cards - an integer
 4. The number of processors - an integer
 5. The number of RAM memory - an integer
    

1 line is printed to the console, which should look like this:

 • If the budget is sufficient:
 
"You have {remaining budget} leva left!"

 • If the amount exceeds the budget:
 
"Not enough money! You need leva more!"

Format the result to the second decimal place.

########

8. Lunch break:
   
During your lunch break, you want to watch an episode of your favorite series. Your task is to write a program that will tell if you have enough time to watch the episode. During the break, you have time for lunch and time for relaxation. Lunch time will be 1/8 of break time and recess time will be 1/4 of break time.

Input:

3 lines are read from the console:

 1. Name of series - text
 2. Episode duration - an integer
 3. Rest duration - an integer
    
Output:

Write one line to the console:

 • If there is enough time to watch the episode:
 
"You have enough time to watch {series name} and left with {remaining time} minutes free time."

 • If you don't have enough time:
 
"You don't have enough time to watch {series name}, you need {necessary time} more minutes."

Time to round up to the nearest whole number.
