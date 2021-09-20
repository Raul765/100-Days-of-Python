from tkinter import*
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.minsize(height=700)
        
        self.canvas = Canvas(height=250, width= 300)
        self.question = self.canvas.create_text(150, 125, text="a", font=("Arial",20,"italic"))

        image_true = PhotoImage(file=r"Day34 - Trivia App\images\true.png")
        self.button_true = Button(image=image_true, command=self.true_pressed)

        image_false = PhotoImage(file=r"Day34 - Trivia App\images\false.png")
        self.button_false = Button(image=image_false, command=self.false_pressed)

        self.label_score = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")

        #grid
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.button_true.grid(row=2, column=1)
        self.button_false.grid(row=2, column=0)
        self.label_score.grid(row=0, column=1, sticky="e")

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text, width=280)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz", width=280)
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")
        
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("True")      
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
            self.label_score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_question)
            