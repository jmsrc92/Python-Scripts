class QuizBrain:
    def __init__(self, q_list):
     
        self.question_number = 0 # attribute starting at 0
        self.question_list = q_list # passes in a list

    def next_question(self):
        self.question_number += 1
        question_text = self.question_list[self.question_number].text #.text is attribute of the question bank
        user_input = input(f"Q.{self.question_number}: {question_text} (True/False)?: ")
        print(user_input)














        
        