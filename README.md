# Online-course-Selling-software
TAFE offers online courses to their students. The student can select any available course to enrol in 
it. If the student enrols in more than three courses, TAFE offers 5% discount to second course 
onward. TAFE allows its students to pay for their courses cost using credit or debit card. Write a 
program to store the available courses in a Dictionary collection, including the course ID as a key and 
the course name, course cost, and length as a value. 
The system allows a student to list the available courses, search for a course, enrol in a course, list 
his/her courses. The main program should first display a menu as follows. A user needs to select an 
option from the main menu. 
=======================================================
Welcome to TAFE Online Courses System
=======================================================
<1> List the available courses 
<2> Search for a course 
<3> Enrol in a course
<4> List my courses 
<5> Quit 
Please select an option from the above: 1
If a student selects the option <1> the program will list all available courses showing course ID and 
name. Then the user selects the course ID that he/she want to enrol or a negative number to exit. The 
program will display the course detail includes course ID, name, cost and length then the program will 
ask the student to confirm his/her enrolment. If the student selects Y then the program will check if 
the student eligible for the 5% discount as discuss above. If he/she eligible then the system will applythe discount and shows the new cost. After that the system asks for the student’s name and credit or 
debit card details. However, if the student selects N then the system will display the main menu again, 
otherwise it will ask the same question again.
The student's details and credit or debit card details are then added to the end of a text file 
(student.txt), including student name, course ID, name, course cost, and course length. Note that the 
newly added record should be consistent with that of existing records.
A typical example of the program display (once a student chooses the option <1>) can be as follows. 
Your program MUST follow the same display style.
The available courses are:
1- Java
2- Ruby
3- Database
4- Java advance
Please select the course code you want to enrol or a negative number
to exit: 3
Course detail:
Name: Database
Cost: $120
Total length: 10 hours
Do you want to enrol in this course (Y/N)? Y
Please enter your name and your credit or debit card details:
Name: Sally John
Card Number:1234567898
MM:02
YYYY: 2025
Thank You!
You have been added to the Database course
Do you want to enrol in another course (Y/N)? N
After the operation, the student.txt file will have the following content after Harry John's details 
entered.
Sally John,3,Database,120,10
=======================================================
Welcome to TAFE Online Courses System
=======================================================
<1> List the available courses 
<2> Search for a course 
<3> Enrol in a course
<4> List my courses 
<5> Quit 
Please select an option from the above: 2
If a student chooses the option <2> from the main menu then the system asks the student to enter the 
course name that want to see details. To facilitate the search option, you need to read from the courses 
dictionary and list all matched courses as below. If the course is not in the courses list, then the system 
must print a message to the student saying this curse is not available. 
After displaying the courses' list, the system prompts the student with the following message, 'Do you 
want to search for another course (Y/N)?' If a student enters 'Y', the system asks the student to enter 
the course name, else if the user enters 'N', the program displays the main menu. Otherwise, the 
program prompts the same message again. 
Please enter the course name you want to search or a negative number
to exit: Java
Thank You!
One course has been found:
Course ID: 1
Name: Java
Cost: $180
Total length: 20 hours
Do you want to search for another course (Y/N)? N
=======================================================
Welcome to TAFE Online Courses System
=======================================================
<1> List the available courses 
<2> Search for a course 
<3> Enrol in a course
<4> List my courses 
<5> Quit 
Please select an option from the above: 3
If a student chooses the option <3> the program, then will list all available courses showing course ID 
and name. Then the user selects the course ID that he/she want to enrol or a negative number to exit. 
The program will display the course detail includes course ID, name, cost and length then the program 
will ask the user to confirm his/her enrolment. If the student selects Y then the program will check if 
the student eligible for the 5% as discuss above. If he/she eligible then the system will apply the 
discount and shows the new cost. After that the system asks for student name and credit or debit card 
details. However, if the student selects N then the system will display the main menu again, otherwise 
it will ask the same question again.
The student's details are then added to the end of the text file (student.txt), including student name, 
course ID, name, course cost, and course length. Note that the newly added record should be 
consistent with that of existing recordsA typical example of the program display (once a user chooses the option <3>) can be as follows. 
Your program MUST follow the same display style.
The available courses are:
1- Java
2- Ruby
3- Database
4- Java advance
Please select the course code you want to enrol or 0 to exit: 1
Course detail:
Couse ID:1
Name: Java
Cost: $180
Total length: 20 hours
Do you want to enrol in this course (Y/N)? Y
Congratulation you received a 5% discount. You need to pay only 
$171.
Please enter your credit or debit card details:
Name on Card: Sally John
Card Number: 1234567898
MM:02
YYYY:2025
Thank You!
You have been added to the Java course.
Do you want to enrol in another course (Y/N)? N
After the operation, the student.txt file will have the following content after Harry John's details 
entered.
Sally John,3,Database,120,10
Sally John,1,Java,171,20
=======================================================
Welcome to TAFE Online Courses System
=======================================================
<1> List the available courses 
<2> Search for a course 
<3> Enrol in a course
<4> List my courses
<5> Quit 
Please select an option from the above: 4
If a student chooses the option <4> from the main menu, the system asks the student to enter his/her 
name. The system then collects the user details from the student.txt file. It displays it as follows 
(assuming the following student was searched for). If the name cannot find the system must show an 
error message to the user. To facilitate the search option, you need to use an appropriate data structure 
such as List.
Enter your name: Sally John
Hello Sally, you are enrolled in the following courses:
1- Database, 10 hours
2- Java, 20 hours
Finally, the program quits if the student chooses the option <5>. 
=======================================================
Welcome to TAFE Online Courses System
=======================================================
<1> List the available courses 
<2> Search for a course 
<3> Enrol in a course
<4> List my courses 
<5> Quit 
Please select an option from the above: 5
Goodbye 
Note: 
• You must use multiple functions, instead of using a single function to do everything.
• You must handle exceptions appropriately such as the student.txt file is not existing, string 
values instead of numbers etc. 
• You must use appropriate data structure such as Lists, Dictionaries etc.
• Your program should be able to handle some exceptions such as invalid inputs, undefined 
inputs with error messages, e.g.: 
o The Credit or Debit Card number must be 10 digits.
o The Credit or Debit Card MM must be 2 digits.
o The Credit or Debit Card YYYY must be 4 digits.
