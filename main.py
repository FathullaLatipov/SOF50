from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Простейшая временная база данных для хранения вопросов и ответов
questions = [
    {'id': 1, 'title': 'Как использовать Flask?', 'text': 'Я новичок и я не знаю как работать на Flask'},
    {'id': 2, 'title': 'Как скачать Django?', 'text': 'Я новичок и я не знаю как работать на Django'}
]

answers = [
    {'id': 1, 'question_id': 1, 'answer': 'Просто скачай Flask через команду pip install flask'},
    {'id': 2, 'question_id': 2, 'answer': 'Просто скачай Django через команду pip install django'}
]


# endpoint or url (urls.py)
@app.route('/')
def home():
    return render_template('index.html', questions=questions)


# Страница с деталями вопроса и ответа
@app.route('/question/<int:question_id>')
def question(question_id):
    question = next((q for q in questions if q['id'] == question_id), None)
    if question:
        question_answers = (a for a in answers if a['question_id'] == question_id)
        return render_template('question.html', question=question, answers=question_answers)
    else:
        return 'Руслан не найден!'


# Страница для добавления нового вопроса
@app.route('/ask', methods=['POST', 'GET'])
def ask():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']

        new_question = {
            'id': len(questions) + 1,
            'title': title,
            'text': text
        }

        questions.append(new_question)
        # Если не будет работать то поставьте вместо home -> 'home'
        return redirect(url_for(home))
    else:
        return render_template('ask.html')


@app.route('/slave/<int:title>')
def buy(title):
    return f'This is product sd1212fsdf: {title}'


app.run(debug=True)
