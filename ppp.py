from flask import Flask, render_template, request, url_for

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


@app.route('/carousel')
def carousel():
    return render_template('carousel.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
