### 1. Started project off with local repository and git creation
### 2. Created docs/work-log.md and README.md
### 3. Created files for modules and for program execution
    - inputs.py - for functions responsible of taking data inputted by user
    - calculations.py - for calculating operation chosen by user on numbers chosen by him
    - main.py - for importing modules and whole program execution
### 4. Created input() functions for choosing numbers and operations 
### 5. Created calculating function for calculating operation on chosen numbers
### 6. Imported inputs.py and calculations.py modules to main.py and created program executing function inside
### 7. Created prints UX prints for main.py
### 8. Did tests after which I found out about not handled ZeroDivisionError
    - Operation input
        - "" - Operation cannot be empty
        - Other then in allowed operations - Operation not in allowed operations
    - Number input
        - -101 and 101 - Chosen number not in range <-100, 100>
        - If operation "/" - second number == 0 - You can't divide by 0
### 9. Repaired code by adding while loop with if instruction inside main function.
### 10. Sent my calculator for check to ChatGPT 
