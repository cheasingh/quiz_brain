from tkinter import Tk, Button, Label, Canvas, PhotoImage
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizeInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # label estate
        self.label_score = Label(text="score = 0", bg=THEME_COLOR,
                                 fg="white", font=("Arial", 14))
        self.label_score.grid(row=0, column=1)

        # canvas estate
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.board = self.canvas.create_text(
            150,
            125,
            text="This is joe",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
            width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # btn estate
        img_true = PhotoImage(file="./images/true.png")
        img_false = PhotoImage(file="./images/false.png")
        self.btn_true = Button(image=img_true,
                               width=80, height=80, highlightthickness=0, command=self.click_true)
        self.btn_true.grid(row=2, column=0)
        self.btn_false = Button(image=img_false,
                                width=80, height=80, highlightthickness=0, command=self.click_false)
        self.btn_false.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

        # end ui design

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.board, text=q_text)
        else:
            self.canvas.itemconfig(
                self.board, text=f"Your Final Score: {self.quiz.score}/{len(self.quiz.question_list)}")
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")

    def click_true(self):

        self.give_feedback(self.quiz.check_answer("True"))

    def click_false(self):

        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
