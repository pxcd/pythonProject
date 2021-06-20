from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank)

# print(question_bank[2])

quiz = QuizBrain(question_bank)
# print(quiz.question_list)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"You're final score was: {quiz.score}/{len(question_bank)}")