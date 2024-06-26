from flask import Flask, render_template, request
import random

app = Flask(__name__)

proff = ['инженер-исследователь',
         'пилот',
         'строитель',
         'экзобиолог',
         'врач',
         'инженер по терраформированию',
         'климатолог',
         'специалист по радиационной защите',
         'астрогеолог',
         'гляциолог',
         'инженер жизнеобеспечения',
         'метеоролог',
         'оператор марсохода',
         'киберинженер',
         'штурман',
         'пилот дронов']

name = [
    {
        "name": "Энди",
        "surname": "Уир",
        "photo": "static/img/pers1.png",
        "specialties": "астрогеолог, специалист по радиационной защите"
    },
    {
        "name": "Марк",
        "surname": "Уаер",
        "photo": "static/img/pers2.png",
        "specialties": "пилот, специалист в своей сфере"
    },
    {
        "name": "Джейсон",
        "surname": "Браер",
        "photo": "static/img/pers3.png",
        "specialties": "врач, отличный врач!"
    }
]


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list1>')
def list_prof(list1):
    return render_template('list_prof.html', list1=list1, proff=proff)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    return render_template('auto_answer.html')


@app.route('/astronaut_selection')
def astronaut_selection():
    return render_template('astronaut.html', proff=proff)


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return render_template('choice.html', planet_name=planet_name)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return render_template('results.html', nickname=nickname, level=level, rating=rating)


@app.route('/load_photo', methods=['POST', 'GET'])
def photo():
    if request.method == 'GET':
        return render_template('photo.html')
    elif request.method == 'POST':
        f = request.files['file']
        print(f.read())
        return "Форма отправлена"


@app.route('/carousel')
def carousel():
    return render_template('carousel.html')


@app.route('/login')
def login():
    return render_template('login_form.html')


@app.route('/member')
def member():
    number = random.randint(0, 2)
    return render_template('member.html', name=name, number=number)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
