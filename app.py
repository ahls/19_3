from flask import Flask, request, render_template, redirect, flash, session
from surveys import satisfaction_survey
app = Flask(__name__)
app.config["SECRET_KEY"] = 'asd'
responses = []

@app.route('/')
def rootRoute():
    return render_template('home.html',survey=satisfaction_survey)

@app.route('/questions')
def questionRoute():
    if 'responses' not in session or session['responses'] == None:
        session['responses'] = list()
    index = len(session['responses'])
    # elif len(responses) == 0 or len(responses[-1]) >= len(satisfaction_survey.questions):
    #     flash('Sent you to Question 0!')
    #     return redirect('/questions/0')
    # elif index != len(responses[-1]):
    #     flash('Sent you to the next question!')
    #     return redirect(f'/questions/{len(responses[-1])}')
    return render_template('question.html',survey=satisfaction_survey, questionIndex = index)


@app.route('/questions/<int:index>/submit', methods = ['POST'])
def nextQuestionRoute(index):
    
    sessionResponse = session['responses']
    print(f"current index in submit:{len(sessionResponse)}")
    sessionResponse.append(list(request.form.keys())[0])
    session['responses'] = sessionResponse
    if len(sessionResponse) >= len(satisfaction_survey.questions):
        responses.append(sessionResponse)
        session['responses'] = None
        return redirect('/thankyou')
    else:
        return redirect(f'/questions')

@app.route('/thankyou')
def thankyouRoute():
    return render_template("thankyou.html",survey=satisfaction_survey)
