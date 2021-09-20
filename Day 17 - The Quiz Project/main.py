from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]

for i in question_data:
    new_question=Question(i["text"], i["answer"])
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.has_questions_left():
    quiz.next_question()

quiz.end_of_quiz()
