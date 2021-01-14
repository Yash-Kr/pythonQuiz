from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    # create new object
    new_que = Question(item["question"], item["answer"])
    question_bank.append(new_que)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have Completed the Quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")