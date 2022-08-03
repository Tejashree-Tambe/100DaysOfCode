from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

no_of_questions = len(question_data)
for question in question_data:
    q_text = question['text']
    q_ans = question['answer']

    new_question = Question(q_text, q_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz!")
score = quiz.get_score()
print(f"Your score is {score}/{len(question_bank)}")
