class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_no].text
        current_answer = self.question_list[self.question_no].answer
        self.question_no += 1
        user_ans = input(f"Q.{self.question_no}: {current_question} (True/False)? ")

        self.check_answer(user_ans, current_answer)

    def still_has_questions(self):
        no_of_questions = len(self.question_list)
        return self.question_no < no_of_questions

    def check_answer(self, user_ans, correct_answer):
        if user_ans.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1

        else:
            print("You got it wrong")

        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_no}\n")

    def get_score(self):
        return self.score


