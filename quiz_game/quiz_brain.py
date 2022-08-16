class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        print(len(self.question_list))
    
    def still_has_question(self):
        return self.question_number < len(self.question_list)
        

    def next_question(self):
        print(self.question_number < len(self.question_list))
        print(f"{self.question_number} < {len(self.question_list)}")
        # print(self.question_number)
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:{current_question.text} (True/False):")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self , user_answer , currect_answer):
        if user_answer.lower() == currect_answer.lower():
            self.score += 1
            print("you got it right")
        else:
            print("thats wrong")
        print(f"the currect answer was: {currect_answer}.")
        print(f"your current score is : {self.score}/{self.question_number}\n")
