from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizeInterface
import requests


param = {
    "amount": 10,
    "category": 18,
    "difficulty": "easy",
    "type": "boolean"
}
endpoint = "https://opentdb.com/api.php"

question_data = requests.get(endpoint, param).json()['results']
# question_data.raise_for_status()

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
window = QuizeInterface(quiz)
