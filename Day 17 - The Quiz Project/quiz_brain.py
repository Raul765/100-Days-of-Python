class QuizBrain:
    def __init__(self, question_bank):
        self.question_number=0
        self.question_list=question_bank
        self.correct_answers=0

    def next_question(self):
        self.question=self.question_list[self.question_number]
        self.question_number+=1
        self.answer=input(f"Q{self.question_number}: {self.question.text}. (True/False): ")
        
        if self.answer.lower()==self.question.answer.lower():
            self.correct_answers+=1
            print(f"You got it right!")
            print(f"The correct answer was {self.question.answer}.")
            print(f"Your current score is {self.correct_answers}/{self.question_number}")
        else:
            print(f"That's wrong.")
            print(f"The correct answer was {self.question.answer}.")
            print(f"Your current score is {self.correct_answers}/{self.question_number}")            
        print("")

    def has_questions_left(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            return False

    def end_of_quiz():
        print("You've completed the quiz")
        print(f"Your final score was: {self.correct_answers}/{self.question_number} ")