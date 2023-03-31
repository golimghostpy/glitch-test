from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def a(title='None'):
    return render_template('base.html', title=title)


@app.route('/list_prof/<list>')
def b(list):
    prof = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
            'климатолог', 'специалист по радиационной защите', 'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения',
            'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов']
    return render_template('index.html', list=list, prof=prof)


@app.route('/answer')
@app.route('/auto_answer')
def c():
    params = {}
    params['title'] = 'Анкета'
    params['surname'] = 'Сычук'
    params['name'] = 'Алексей'
    params['education'] = 'Детский сад'
    params['profession'] = 'Профессиональный профессионал'
    params['sex'] = 'Ламинат'
    params['motivation'] = 'Очень хочу'
    params['ready'] = 'Да'
    return render_template('auto_answer.html', **params)



if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1', debug=True)
