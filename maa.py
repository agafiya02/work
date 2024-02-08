from flask import Flask, url_for
import requests

app = Flask(__name__)


@app.route('/')
def name():
    return "Миссия Колонизация Марса"


@app.route('/index')
def slogan():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    advertisement = ['Человечество вырастает из детства.',

                     'Человечеству мала одна планета.',

                     'Мы сделаем обитаемыми безжизненные пока планеты.',

                     'И начнем с Марса!',

                     'Присоединяйся!']
    return '</br>'.join(advertisement)


@app.route('/image_mars')
def image():
    return '''<html>
             <head>
                 <meta charset="utf-8">
                 <title>Привет, Марс!</title>
             </head>
             <body>
                <h1>Жди нас, Марс!</h1>
                <img width="350" height="350" src="https://media.istockphoto.com/id/1128060877/ru/%D1%84%D0%BE%D1%82%D0%BE/%D0%BF%D0%BB%D0%B0%D0%BD%D0%B5%D1%82%D0%B0-%D0%BC%D0%B0%D1%80%D1%81-%D1%81-%D0%BF%D0%BE%D0%BB%D1%8F%D1%80%D0%BD%D1%8B%D0%BC-%D0%BB%D1%8C%D0%B4%D0%BE%D0%BC-%D0%B8%D0%B7%D0%BE%D0%BB%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B0-%D0%BD%D0%B0-%D0%B1%D0%B5%D0%BB%D0%BE%D0%BC-%D1%84%D0%BE%D0%BD%D0%B5-%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B-%D1%8D%D1%82%D0%BE%D0%B3%D0%BE-%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F.
                jpg?s=612x612&w=0&k=20&c=HPstwzoXIKL8fItpdDg93spx1y-xvI0JvPGHGtHr6aE=" 
    alt="здесь должна была быть картинка, но не нашлась">
    
                 <p align="left">Вот она какая, красная планета. </p>
              </body>
            </html>
             '''


@app.route('/promotion_image')
def promotion_image():
    return f'''<html>
             <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet" 
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                crossorigin="anonymous">
                <title>Колонизация</title>
             </head>
             <body>
                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                <h1>Жди нас, Марс!</h1>
                <img width="300" height="300" src="https://media.istockphoto.com/id/1128060877/ru/%D1%84%D0%BE%D1%82%D0%BE/%D0%BF%D0%BB%D0%B0%D0%BD%D0%B5%D1%82%D0%B0-%D0%BC%D0%B0%D1%80%D1%81-%D1%81-%D0%BF%D0%BE%D0%BB%D1%8F%D1%80%D0%BD%D1%8B%D0%BC-%D0%BB%D1%8C%D0%B4%D0%BE%D0%BC-%D0%B8%D0%B7%D0%BE%D0%BB%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B0-%D0%BD%D0%B0-%D0%B1%D0%B5%D0%BB%D0%BE%D0%BC-%D1%84%D0%BE%D0%BD%D0%B5-%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B-%D1%8D%D1%82%D0%BE%D0%B3%D0%BE-%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F.jpg?s=612x612&w=0&k=20&c=HPstwzoXIKL8fItpdDg93spx1y-xvI0JvPGHGtHr6aE="
    alt="здесь должна была быть картинка, но не нашлась">
                <div class="alert alert-dark" role="alert">
                  <b>Человечество вырастает из детства.</b>
                </div>
                <div class="alert alert-success" role="alert">
                  <b>Человечеству мала одна планета.</b>
                </div>
                <div class="alert alert-dark" role="alert">
                  <b>Мы сделаем обитаемыми безжизненные пока планеты.</b>
                </div>
                <div class="alert alert-warning" role="alert">
                  <b>И начнем с Марса!</b>
                </div>
                <div class="alert alert-danger" role="alert">
                  <b>Присоединяйся!</b>
                </div>
              </body>
            </html>
             '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
