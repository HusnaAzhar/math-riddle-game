import tkinter as tk
from tkinter import tkk
import random

# Multiple Choice Questions with explanations
math_mcq_riddles = [
    {
        "question": "Which quadratic equation represents the area of a square with side length x, if the area is 289 m²?",
        "choices": ["x² - 17x = 289", "x² + 17² = 0", "(x + 17)² = 0", "x² - 289 = 0"],
        "answer": "x² - 289 = 0",
        "hint": "Area of square is x². Rearranged to standard form.",
        "explanation": "Area = x² → x² = 289 → x² - 289 = 0 is the correct form."
    },
    {
        "question": "Solve the quadratic: (x + 1)(x + 2) = -2x(x + 2)",
        "choices": ["x = 1, x = -2/3", "x = -1, x = -2/3", "x = -1, x = 2/3", "x = 1, x = 2/3"],
        "answer": "x = 1, x = -2/3",
        "hint": "Expand both sides and simplify before solving.",
        "explanation": "Simplifying both sides gives a quadratic: x² + 3x + 2 = -2x² - 4x → solve it to get x = 1 and -2/3."
    },
    {
        "question": "Convert binary number 1101₂ to base 10.",
        "choices": ["14", "11", "13", "15"],
        "answer": "13",
        "hint": "Use place values: 1×8 + 1×4 + 0×2 + 1×1.",
        "explanation": "1×8 + 1×4 + 0×2 + 1×1 = 13."
    },
    {
        "question": "Given P = {1,3,5,7,9} and R = {1,4,9}, what is P ∩ R?",
        "choices": ["1, 4", "3, 7", "1, 9", "4, 9"],
        "answer": "1, 9",
        "hint": "Intersection = common elements.",
        "explanation": "Elements in both sets: {1, 9}."
    },
    {
        "question": "In a graph, a vertex has a loop. What is the degree of that vertex?",
        "choices": ["1", "2", "3", "0"],
        "answer": "2",
        "hint": "A loop adds 2 to the degree.",
        "explanation": "In graph theory, a loop contributes two to the degree of a vertex."
    },
    {
        "question": "What is the range of this data set: 10, 5, 8, 18, 22, 12?",
        "choices": ["15", "17", "13", "12"],
        "answer": "17",
        "hint": "Range = Max - Min.",
        "explanation": "Range = 22 - 5 = 17."
    },
    {
        "question": "A fair coin and a die are tossed. How many total outcomes are there?",
        "choices": ["6", "10", "12", "14"],
        "answer": "12",
        "hint": "2 outcomes × 6 outcomes.",
        "explanation": "2 outcomes from coin × 6 outcomes from die = 12 total outcomes."
    },
    {
        "question": "Find the roots of the equation x² + x - 6 = 0",
        "choices": ["x = 3, x = -2", "x = 2, x = -3", "x = -3, x = -2", "x = 1, x = -6"],
        "answer": "x = 2, x = -3",
        "hint": "Factor: (x + 3)(x - 2).",
        "explanation": "x² + x - 6 factors into (x + 3)(x - 2), so x = -3 or x = 2."
    },
    {
        "question": "Express 2(64) + 24 + 6 in base 7.",
        "choices": ["10423", "7044", "5066", "3524"],
        "answer": "5066",
        "hint": "Convert total from base 10 to base 7.",
        "explanation": "2×64 + 24 + 6 = 158 in base 10 → 5066 in base 7."
    },
    {
        "question": "The arrow follows a quadratic path: f(x) = -13/200 x² + 39/20 x. What is its maximum height?",
        "choices": ["1.6", "2.1", "1.95", "2.5"],
        "answer": "1.95",
        "hint": "Find vertex: x = -b/2a, then compute f(x).",
        "explanation": "x = -b/2a = 1.5 → f(1.5) = 1.95 (max height)."
    }
]

class MathMCQBot:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Riddle Bot")
        self.root.configure(bg="#e0f7fa")

        self.questions = random.sample(math_mcq_riddles, len(math_mcq_riddles))
        self.score = 0
        self.index = 0
        self.hints_used = 0
        self.max_hints = 3
        self.used_hint_this_question = False
        self.correct_streak = 0

        # --- MAIN PAGE ---
        self.main_frame = tk.Frame(root, bg="#e0f7fa")
        self.main_frame.pack(fill="both", expand=True)

        tk.Label(self.main_frame, text="🧠 Welcome to Math Riddle Bot! 🎓", font=("Verdana", 20, "bold"), bg="#e0f7fa", fg="#004d40").pack(pady=30)
        tk.Label(self.main_frame, text="Test your mind with fun math challenges.\nCan you beat your high score?", font=("Verdana", 14), bg="#e0f7fa").pack(pady=10)
        tk.Button(self.main_frame, text="Start Quiz", font=("Verdana", 14), bg="#4CAF50", fg="white", width=15, command=self.start_quiz).pack(pady=20)

        # --- QUIZ FRAME ---
        self.quiz_frame = tk.Frame(root, bg="#e0f7fa")

        self.progress = ttk.Progressbar(self.quiz_frame, length=300, mode='determinate')
        self.progress.pack(pady=10)

        self.percentage_label = tk.Label(self.quiz_frame, text="Progress: 0%", font=("Verdana", 10),
                                         bg="#e0f7fa", fg="#004d40")
        self.percentage_label.pack()
        
        self.quiz_title = tk.Label(
            self.quiz_frame,
            text="📘 Math Riddle Challenge",
            font=("Verdana", 18, "bold"),
            bg="#e0f7fa",
            fg="#00796B"
        )
        self.quiz_title.pack(pady=(10, 5))


        self.question_label = tk.Label(
            self.quiz_frame,
            text="",
            font=("Verdana", 16, "bold"),
            wraplength=600,
            justify="center",
            bg="white",  # White background for contrast
            fg="#004d40",
            relief="groove",
            bd=3,
            padx=10,
            pady=10
        )

        self.question_label.pack(pady=(10, 10), fill="both", expand=True)

        self.option_frame = tk.Frame(self.quiz_frame, bg="#e0f7fa")
        self.option_frame.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(
                self.option_frame,
                text="",
                width=30,
                font=("Verdana", 12),
                bg="#ffffff",
                fg="#000000",
                relief="raised",
                bd=2,
                activebackground="#e0f7fa",
                cursor="hand2",
                command=lambda i=i: self.check_answer(i)
            )

            btn.pack(pady=5)
            self.option_buttons.append(btn)

        self.feedback_label = tk.Label(self.quiz_frame, text="", font=("Verdana", 12), bg="#e0f7fa", fg="blue")
        self.feedback_label.pack(pady=5)

        self.button_frame = tk.Frame(self.quiz_frame, bg="#e0f7fa")
        self.button_frame.pack(pady=10)

        self.hint_button = tk.Button(self.button_frame, text="Hint", command=self.show_hint,
                                     bg="#2196F3", fg="white", width=12, font=("Verdana", 11))
        self.hint_button.grid(row=0, column=0, padx=10)

        self.next_button = tk.Button(self.button_frame, text="Next", command=self.next_question,
                                     bg="#4CAF50", fg="white", width=12, font=("Verdana", 11))
        self.next_button.grid(row=0, column=1, padx=10)

        self.end_button = tk.Button(self.button_frame, text="End", command=self.end_game,
                                    bg="#F44336", fg="white", width=12, font=("Verdana", 11))
        self.end_button.grid(row=0, column=2, padx=10)

        self.score_label = tk.Label(self.quiz_frame, text="Score: 0", font=("Verdana", 12, "bold"),
                                    bg="#e0f7fa", fg="#00695c")
        self.score_label.pack(pady=5)

        # --- FEEDBACK SECTION ---
        self.feedback_prompt = tk.Label(
            self.quiz_frame,
            text="",
            font=("Verdana", 14, "bold"),
            bg="#e0f7fa",
            fg="#004d40",
            justify="center"
        )

        self.feedback_buttons_frame = tk.Frame(self.quiz_frame, bg="#e0f7fa")

        self.feedback_buttons = []
        feedback_options = [
            ("Good", "😊", "#4CAF50"),     # Green
            ("Neutral", "😐", "#FFC107"),  # Yellow
            ("Bad", "😞", "#F44336")       # Red
        ]
        for label, emoji, color in feedback_options:
            btn = tk.Button(
                self.feedback_buttons_frame,
                text=f"{emoji} {label}",
                font=("Verdana", 12, "bold"),
                width=12,
                bg=color,
                fg="white",
                command=lambda t=label: self.collect_feedback(t)
            )
            btn.pack(side="left", padx=15, pady=10)
            self.feedback_buttons.append(btn)
            
        self.restart_button = tk.Button(
            self.quiz_frame,
            text="🔁 Restart Quiz",
            font=("Verdana", 12, "bold"),
            bg="#9C27B0",  # Purple
            fg="white",
            width=20,
            command=self.restart_quiz
        )


    def start_quiz(self):
        self.main_frame.pack_forget()
        self.quiz_frame.pack(fill="both", expand=True)
        self.next_question()

    def next_question(self):
        if self.index >= len(self.questions):
            self.end_game()
            return

        self.progress["maximum"] = len(self.questions)
        self.progress["value"] = self.index
        percent = int((self.index / len(self.questions)) * 100)
        self.percentage_label.config(text=f"Progress: {percent}%")

        self.used_hint_this_question = False
        self.feedback_label.config(text="")

        q = self.questions[self.index]
        self.question_label.config(text=f"Q{self.index + 1}: {q['question']}")

        for i, choice in enumerate(q["choices"]):
            self.option_buttons[i].config(text=choice, state="normal", bg="#ffffff")

    def check_answer(self, choice_index):
        selected = self.option_buttons[choice_index].cget("text")
        q = self.questions[self.index]
        correct = q["answer"]
        explanation = q.get("explanation", "")

        if selected == correct:
            points = 5 if self.used_hint_this_question else 10
            self.correct_streak += 1
            if self.correct_streak == 3:
                points += 5
                self.correct_streak = 0
                self.feedback_label.config(text=f"🔥 Streak! +{points} points (+5 bonus)", fg="green")
            else:
                self.feedback_label.config(text=f"✅ Correct! +{points} points", fg="green")
            self.score += points
        else:
            self.feedback_label.config(text=f"❌ Wrong! Correct: {correct}\n📘 {explanation}", fg="red")
            self.correct_streak = 0

        for btn in self.option_buttons:
            btn.config(state="disabled")

        self.score_label.config(text=f"Score: {self.score}")
        self.index += 1

    def show_hint(self):
        if self.hints_used < self.max_hints:
            hint = self.questions[self.index]["hint"]
            self.feedback_label.config(text=f"💡 Hint: {hint}", fg="blue")
            self.hints_used += 1
            self.used_hint_this_question = True
        else:
            self.feedback_label.config(text="⚠️ No more hints!", fg="orange")

    def end_game(self):
        self.question_label.config(text=f"🎉 Game Over! Your total score is: {self.score}")
        self.feedback_label.config(text="")
        for btn in self.option_buttons:
            btn.pack_forget()
        self.hint_button.config(state="disabled")
        self.next_button.config(state="disabled")
        self.end_button.config(state="disabled")
        self.progress["value"] = len(self.questions)
        self.percentage_label.config(text="Progress: 100%")

        # Show feedback section
        self.feedback_prompt.config(text="How was your experience with Math Riddle Bot?")
        self.feedback_prompt.pack(pady=(20, 5))
        self.feedback_buttons_frame.pack(pady=(0, 20))
        
        self.restart_button.pack(pady=(5, 20))


    def collect_feedback(self, rating):
        self.feedback_prompt.config(text=f"✅ Thanks for your feedback: {rating}!", fg="#2E7D32")
        for btn in self.feedback_buttons:
            btn.config(state="disabled")
            
    def restart_quiz(self):
        self.quiz_frame.pack_forget()
        self.main_frame.pack(fill="both", expand=True)

        # Reset all variables
        self.questions = random.sample(math_mcq_riddles, len(math_mcq_riddles))
        self.score = 0
        self.index = 0
        self.hints_used = 0
        self.used_hint_this_question = False
        self.correct_streak = 0

        # Reset interface
        self.score_label.config(text="Score: 0")
        self.percentage_label.config(text="Progress: 0%")
        self.feedback_label.config(text="")
        self.feedback_prompt.config(text="")
        for btn in self.feedback_buttons:
            btn.config(state="normal")
        self.feedback_buttons_frame.pack_forget()
        self.feedback_prompt.pack_forget()
        self.restart_button.pack_forget()

        for btn in self.option_buttons:
            btn.config(state="normal")
            btn.pack()

        self.hint_button.config(state="normal")
        self.next_button.config(state="normal")
        self.end_button.config(state="normal")


        
# Run the GUI
root = tk.Tk()
app = MathMCQBot(root)
root.mainloop()
