class QuizBrain :
    def __init__(self, question_list) :
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self) :
        q_no = self.question_number
        self.question_number += 1;
        current_question = self.question_list[q_no]
        correct_ans = current_question.answer
        user_ans = input(f"Q.{q_no + 1} : {current_question.question} (True or False) ")
        self.check_answer(user_ans,correct_ans)

    def still_has_questions(self) :
        if self.question_number < len(self.question_list) :
            return True
        else :
            return False

    def check_answer(self,user_ans,correct_ans) :
        if  user_ans.lower() == correct_ans.lower() :
            self.score += 1
            print("Hurray that's absolutely correct ")
        else:
            print("Sorry , that was incorrect answer !!")

        print(f"Your Current Score is {self.score}/{self.question_number}")
        print("\n")