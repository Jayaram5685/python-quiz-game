import tkinter as tk
import random

# List of 50 Python-related questions (including errors and trivia)
python_questions = [
    {"question": "Who is known as the father of Python?", "options": ["Guido van Rossum", "Elon Musk", "Mark Zuckerberg", "Bill Gates"], "answer": "Guido van Rossum"},
    {"question": "What is the output of the following code:\n\nprint(5 + 2 * 3)\n", "options": ["11", "21", "17", "15"], "answer": "11"},
    {"question": "Identify the error in the following code:\n\nx = 5\ny = 'hello'\nprint(x + y)\n", "options": ["TypeError", "SyntaxError", "NameError", "ValueError"], "answer": "TypeError"},
    {"question": "Which keyword is used to define a function in Python?", "options": ["def", "function", "func", "create"], "answer": "def"},
    {"question": "What is the output of the following code:\n\nprint('Hello'[1])\n", "options": ["H", "e", "l", "o"], "answer": "e"},
    {"question": "Which method is used to add an element at the end of a list?", "options": ["append()", "insert()", "add()", "push()"], "answer": "append()"},
    {"question": "What does the 'self' keyword represent in a class?", "options": ["Instance of the class", "Class itself", "Function parameter", "Method return value"], "answer": "Instance of the class"},
    {"question": "Which function is used to get the type of an object in Python?", "options": ["type()", "id()", "class()", "object()"], "answer": "type()"},
    {"question": "What does the 'break' statement do in a loop?", "options": ["Exits the loop", "Skips the current iteration", "Pauses the loop", "Restarts the loop"], "answer": "Exits the loop"},
    {"question": "Which of the following is not a valid Python data type?", "options": ["integer", "float", "list", "character"], "answer": "character"},
    {"question": "What does the 'continue' statement do in a loop?", "options": ["Exits the loop", "Skips the current iteration", "Pauses the loop", "Restarts the loop"], "answer": "Skips the current iteration"},
    {"question": "Which operator is used to get the remainder of a division?", "options": ["%", "//", "/", "*"], "answer": "%"},
    {"question": "Which of the following is used to import a module in Python?", "options": ["import module", "include module", "require module", "use module"], "answer": "import module"},
    {"question": "What does the 'is' operator do in Python?", "options": ["Compares values", "Checks for object identity", "Checks if the value is None", "Checks if two values are equal"], "answer": "Checks for object identity"},
    {"question": "How do you declare a dictionary in Python?", "options": ["{}", "[]", "()", "dict()"], "answer": "{}"},
    {"question": "Which Python function is used to read input from the user?", "options": ["input()", "get_input()", "scan()", "read()"], "answer": "input()"},
    {"question": "Which operator is used to assign a value to a variable?", "options": ["=", "==", "=>", ":="], "answer": "="},
    {"question": "Which of the following is the correct way to create a string in Python?", "options": ["'Hello'", '"Hello"', "Hello", "'H' + 'ello'"], "answer": "'Hello'"},
    {"question": "Which function returns the number of characters in a string?", "options": ["len()", "count()", "size()", "length()"], "answer": "len()"},
    {"question": "What does the 'lambda' keyword define in Python?", "options": ["Anonymous function", "Named function", "Class", "Variable"], "answer": "Anonymous function"},
    {"question": "What is the default value of a function argument in Python?", "options": ["None", "0", "False", "Empty string"], "answer": "None"},
    {"question": "What type of error occurs when a non-existent method is called on an object?", "options": ["AttributeError", "TypeError", "IndexError", "ValueError"], "answer": "AttributeError"},
    {"question": "What function is used to create a file in Python?", "options": ["open()", "create()", "file()", "write()"], "answer": "open()"},
    {"question": "How do you handle exceptions in Python?", "options": ["try-except", "catch-except", "error-catch", "try-catch"], "answer": "try-except"},
    {"question": "What function is used to convert a string to lowercase?", "options": ["lower()", "tolower()", "convert()", "str.lower()"], "answer": "lower()"},
    {"question": "Which function is used to round off a number in Python?", "options": ["round()", "ceil()", "floor()", "round-off()"], "answer": "round()"},
    {"question": "How do you declare a tuple in Python?", "options": ["()", "[]", "{}", "tuple()"], "answer": "()"},
    {"question": "Which of the following is used to access an element from a list in Python?", "options": ["index", "key", "position", "element"], "answer": "index"},
    {"question": "What is the output of the following code: print(3 == 3)?", "options": ["True", "False", "3", "Error"], "answer": "True"},
    {"question": "Which operator checks if two values are equal in Python?", "options": ["==", "=", ">", "<"], "answer": "=="},
    {"question": "Which function is used to sort a list in Python?", "options": ["sort()", "order()", "arrange()", "sorted()"], "answer": "sort()"},
    {"question": "Which function is used to get the current working directory in Python?", "options": ["os.getcwd()", "os.path()", "sys.getcwd()", "sys.path()"], "answer": "os.getcwd()"},
    {"question": "What is the purpose of the 'del' keyword in Python?", "options": ["To delete an object", "To define a function", "To add an element", "To print a statement"], "answer": "To delete an object"},
    {"question": "What does the 'with' keyword do in Python?", "options": ["Manages resources", "Defines a function", "Creates a new module", "Declares a variable"], "answer": "Manages resources"},
    {"question": "Which Python module is used for regular expressions?", "options": ["re", "regex", "regexp", "expression"], "answer": "re"},
    {"question": "Which of the following is used to start a comment in Python?", "options": ["#", "//", "/*", "'''"], "answer": "#"},
    {"question": "Which of the following will check if an object is an instance of a class in Python?", "options": ["isinstance()", "type()", "instanceof()", "typecheck()"], "answer": "isinstance()"},
    {"question": "What is the output of the following code: print(bool(0))?", "options": ["False", "True", "None", "0"], "answer": "False"},
    {"question": "What is the method used to remove whitespace from the start and end of a string?", "options": ["strip()", "trim()", "clean()", "remove()"], "answer": "strip()"},
    {"question": "What is the output of the following code:\n\nprint([1, 2, 3] * 2)", "options": ["[1, 2, 3, 1, 2, 3]", "[1, 2, 3, 6]", "[2, 4, 6]", "[1, 2, 3, 2, 4, 6]"], "answer": "[1, 2, 3, 1, 2, 3]"},
    {"question": "Which function in Python is used to read the entire content of a file?", "options": ["read()", "readlines()", "content()", "get()"], "answer": "read()"},
    {"question": "How can you check the length of a list in Python?", "options": ["len(list)", "size(list)", "count(list)", "list.length()"], "answer": "len(list)"},
    {"question": "What does the 'pass' keyword do in Python?", "options": ["Does nothing", "Exits the loop", "Prints a message", "Breaks the program"], "answer": "Does nothing"},
    {"question": "What does the 'not' keyword do in Python?", "options": ["Negates a boolean", "Checks if a value is None", "Compares two objects", "Assigns a value"], "answer": "Negates a boolean"},
    {"question": "Which of the following is used to define a class in Python?", "options": ["class", "def", "function", "module"], "answer": "class"},
    {"question": "Which function is used to remove an element from a list in Python?", "options": ["remove()", "del", "pop()", "delete()"], "answer": "remove()"},
    {"question": "What is the output of the following code:\n\nx = 10\nprint(x > 5 and x < 20)", "options": ["True", "False", "Error", "None"], "answer": "True"},
    {"question": "Which operator is used for floor division in Python?", "options": ["//", "/", "%", "div"], "answer": "//"},
    {"question": "Which module is used to generate random numbers in Python?", "options": ["random", "math", "statistics", "randomgen"], "answer": "random"},
    {"question": "What is the output of the following code:\n\nx = 'Python'\nprint(x[::-1])", "options": ["Python", "nohtyP", "Pyt", "Error"], "answer": "nohtyP"},
]

# Shuffle the list of questions
random.shuffle(python_questions)

# Select 10 random questions from the shuffled list
questions = python_questions[:10]

# Index to track current question
current_question_index = 0
score = 0

# Function to check the answer
def check_answer(selected_option, button):
    global score
    correct_answer = questions[current_question_index]["answer"]
    for btn in option_buttons:
        btn.config(state="disabled")

    if selected_option == correct_answer:
        score += 1
        button.config(bg="#4CAF50", activebackground="#45a049")  # Correct answer button turns green
    else:
        button.config(bg="#F44336", activebackground="#e53935")  # Incorrect answer button turns red
        for btn in option_buttons:
            if btn.cget("text") == correct_answer:
                btn.config(bg="#4CAF50", activebackground="#45a049")

    next_button.config(state="normal")  # Enable Next button

# Function to show the final score with conditions
def show_final_score():
    points = score * 10  # Total score
    total_points = len(questions) * 10  # Maximum points possible

    # Define the performance category and background color
    if points < 40:
        performance = "Fail"
        bg_color = "#F44336"  # Red for fail
    elif points >= 40 and points < 70:
        performance = "Pass"
        bg_color = "#FFC107"  # Yellow for pass
    elif points >= 70 and points < 90:
        performance = "Good"
        bg_color = "#4CAF50"  # Green for good
    else:
        performance = "Excellent"
        bg_color = "#388E3C"  # Dark green for excellent

    # Set the main window background color based on performance
    root.config(bg=bg_color)

    # Hide the question and options
    frame.pack_forget()

    # Create and display score and performance in full screen
    final_score_label.config(text=f"Your score: {points} / {total_points}\nYour performance: {performance}")
    final_score_label.place(relx=0.5, rely=0.4, anchor="center")  # Center the label in the middle of the screen

    # Display the "Play Again" button after the game is completed
    play_again_button.pack(pady=20)

# Function to load the next question
def next_question():
    global current_question_index
    current_question_index += 1
    if current_question_index < len(questions):
        load_question(current_question_index)
    else:
        show_final_score()

# Function to load a question
def load_question(index):
    question_data = questions[index]
    question_label.config(text=f"{index + 1}. {question_data['question']}")  # Display number and question text

    # Randomize options
    random.shuffle(question_data["options"])
    
    for i, option in enumerate(question_data["options"]):
        option_buttons[i].config(
            text=option,
            bg="#ffffff",  # Set background color for buttons
            state="normal",  # Enable buttons for the next question
            command=lambda opt=option, btn=option_buttons[i]: check_answer(opt, btn)
        )
    
    next_button.config(state="disabled")  # Disable Next button until answer is selected

# Function to restart the game
def restart_game():
    global current_question_index, score
    current_question_index = 0
    score = 0
    final_score_label.place_forget()  # Remove the final score label
    play_again_button.pack_forget()  # Hide the Play Again button
    frame.pack(fill="both", expand=True, padx=20, pady=20)  # Show the frame again
    load_question(current_question_index)  # Reload the first question
    root.config(bg="#f0f0f0")  # Reset background color to default

# Set up the main window
root = tk.Tk()
root.title("Python Quiz Game")
root.geometry("800x600")  # Increased window size for better visibility
root.config(bg="#f0f0f0")  # Light grey background for the main window

# Create a frame for the quiz
frame = tk.Frame(root, bg="#F06292", bd=5, relief="ridge")  # Soft pink color for the frame
frame.pack(fill="both", expand=True, padx=20, pady=20)

# Question label with a clean and readable background color
question_label = tk.Label(frame, text="", font=("Arial", 18), wraplength=600, bg="#F06292", fg="#ffffff")
question_label.pack(pady=20)

# Buttons for options with clean background
option_buttons = []
for i in range(4):
    btn = tk.Button(frame, text="", font=("Arial", 14), width=25, height=2, bg="#ffffff", fg="#000000", relief="solid", activebackground="#c1c1c1")
    btn.pack(pady=10)
    option_buttons.append(btn)

# Next button with distinct color
next_button = tk.Button(frame, text="Next", font=("Arial", 14), width=10, state="disabled", command=next_question, bg="#0288D1", fg="#ffffff", relief="solid")
next_button.pack(pady=20)

# Play Again button after completing the quiz
play_again_button = tk.Button(root, text="Play Again", font=("Arial", 16), width=20, command=restart_game, bg="#FF5722", fg="#ffffff", relief="solid")
play_again_button.pack_forget()  # Initially hidden

# Score and performance label
final_score_label = tk.Label(root, text="", font=("Arial", 40, "bold"), bg="#F06292", fg="#ffffff", anchor="center", justify="center")

# Load the first question
load_question(current_question_index)

# Start the Tkinter event loop
root.mainloop()
