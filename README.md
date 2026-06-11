#  **Fizlet** - Flashcard App For Learning and Practicing

## A. Background Information
* This program is designed to help those who are learning and getting ready for each lession or test in class, by:
    -  having UIs similar to Quizlet, but not completely
    - creating a set of card, which includes term and definition by themselves
    - then using it and practicing it by flipping between two sides

* **PURPOSE:** It can help user improve their memory of classroom content, vocabulary from a language they are learning, questions they are preparing for an upcoming exam, and even trivia to challenge their friends. By using the learning method implemented in this app and practicing consistently, user can gradually strengthen their retention, turning short-term memories into long-term knowledge.

## B. How To Use?
* As being mentioned earlier, FIzlet has the interface similar to Quizlet. So that, it has some certain mechanisms, such as:
    - Creating a set of flashcard
    - Saving these set in main screen
    - Selecting set to practice and learn

* For Creating A Set:
    1. First, when you open app, you will be in welcoming screen and can enter main screen by clicking the **Start Button**
    2. Then, you have two decision to make, which is to create or select a set as you are in **Main Screen**
    3. In order to create a set, you may need to click on the **Plus Button** which is the circle button with the plus symbol at the bottom of the screen
    4. After that, you are asked to enter these following inputs: name, term, and definition
        - Name input, which is the large line near the top of screen, is asked only one time
        - Term & Definition input, which are the two small lines on the right and left of the screen, can be entered multiple times if you want
            - clicking the **Add Button** to add more spaces
    5. When you are satisfied with entering  inputs, you can click the **Done Button** in the corner of top right of the screen in order to go back to **Main Screen** and save these datas
    
* For Practicing A Set
    1. As you is in the **Main Screen**, you may chose a set by clicking to the box above the name to select the onr you want to practice
    2. After that, you will be directed to **Practicing Screen** where they can start to enhance their memory
        - Specifically, the card will automatically displays the front side which is the term. To reveal the definition, you can flip it by clicking that box
        - To move on to the next card, you can click the button which has <i>the arrow towards the right</i>
        - In contrast, to move back to previous card, you can click the button which has <i>the arrow towards the left</i>
    3. Then, if you reach to the end of the set, which means there is no more card, you would be congratulated and moved back to **Main Screen**
## C. Keep In Mind
Fizlet
To improve the user experience with the **Daily Planner Assistant**, user should pay attention to the following points: 
* **For the task's input**:
    - user can enter a long string (e.g., help student to complete the project) or a single word (e.g., help, complete, organize).
    - Itan be considered as invalid data and prompt the user to re-enter if the it includes special characters (!, @, #,  $, %,...) or numbers. 
* **For the estimated time's input**:

     The information will be invalid when:  
    - It includes letters (a-z), special characters such as !, @, #, $, %, ^, &,... and includes spaces.  
    - Negative numbers or numbers greater than 24 hours (24 hours for time entered in hours and 1440 for time entered in minutes).  

* **For Yes/No questions** (*"Do you want to continue?"* and *"Do you want to enter time input in hour?"*)
    - The answer is only valid if it is **y** (indicates Yes) and **n** (indicates No), otherwise an error will be displayed and the user will be prompted to re-enter. 
    - ***Especially:***
        - **For "Do you want to continue?"**, if the user uses any characters other than “y”, the program will treat all of them as “n” and will start processing the data to generate a schedule.  
        - **For "Do you want to enter time input in hours?"**, it will be asked again whenever the user has entered invalid information while being asked for the estimated time.

# 

 ***Thank Your For Using Fizlet***




ADD:
may add a notification when they are waiting to be directed (Done)
adding notification when the name input is empty 
issue with dot in name 
