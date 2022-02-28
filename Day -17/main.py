from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = [] # ceate empty list to store data

for q in question_data: # access every item in list
    q_text = q['text'] # get items 'text' key as it is a dictionary
    q_answer = q['answer'] # get items 'answer' key as it is a dictionary
    new_q = Question(q_text, q_answer) # creates instance of an object and passes text and answer to it

    question_bank.append(new_q) # adds object to list

current_question = QuizBrain(question_bank) # creates instance of QuizBrain

current_question.next_question() # uses next question Method




    