from flask import Flask, request, render_template, redirect, flash
from surveys import satisfaction_survey
app = Flask(__name__)
app.secret_key = 'asd'
responses = []

@app.route('/')
def rootRoute():
    return render_template('home.html',survey=satisfaction_survey)

@app.route('/questions/<int:index>')
def questionRoute(index):
    if index==0:
        responses.append(list())
    elif len(responses) == 0 or len(responses[-1]) >= len(satisfaction_survey.questions):
        flash('Sent you to Question 0!')
        return redirect('/questions/0')
    elif index != len(responses[-1]):
        print(f'/questions/{len(responses[-1])} $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        flash('Sent you to the next question!')
        return redirect(f'/questions/{len(responses[-1])}')
    return render_template('question.html',survey=satisfaction_survey, questionIndex = index)


@app.route('/questions/<int:index>/submit', methods = ['POST'])
def nextQuestionRoute(index):
    responses[-1].append(list(request.form.keys())[0])
    if index >= len(satisfaction_survey.questions):
        return redirect('/thankyou')
    else:
        return redirect(f'/questions/{index}')

@app.route('/thankyou')
def thankyouRoute():
    return render_template("thankyou.html",survey=satisfaction_survey)
