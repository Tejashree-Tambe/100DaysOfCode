from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import Quiz_UI


# extracting questions from data.py
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


# to check scores
quiz = QuizBrain(question_bank)
ui = Quiz_UI(quiz)

while quiz.still_has_questions():
    quiz.next_question()

