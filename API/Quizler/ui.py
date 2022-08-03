from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Quiz_UI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score:0", bg=THEME_COLOR, fg="white", highlightthickness=0)
        self.score.grid(column=1, row=0)

        self.question_canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.question_canvas.create_text(
            150,
            125,
            text="Some Question Here",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            width=280)
        self.question_canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, padx=20, pady=20, command=self.true_clicked)
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, padx=20, pady=20, command=self.false_clicked)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score.config(text=f"Score : {self.quiz.score}")
            question = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=question)

        else:
            self.question_canvas.itemconfig(self.question_text, text="You have reached the end of quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def give_output_of_answer(self, is_correct):
        if is_correct:
            self.question_canvas.config(bg="green")

        else:
            self.question_canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

    def true_clicked(self):
        is_correct = self.quiz.check_answer("True")
        self.give_output_of_answer(is_correct)

    def false_clicked(self):
        is_correct = self.quiz.check_answer("False")
        self.give_output_of_answer(is_correct)
