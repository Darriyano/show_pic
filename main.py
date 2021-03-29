from flask import Flask, url_for, request, redirect

import os

app = Flask(__name__)


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        path = ""
        if os.path.exists('static/img/prof_pic.jpg'):
            path = f'''<img src="{url_for('static', filename='img/prof_pic.jpg')}" 
                                           width=400>'''
            print(path)
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/styles.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align='center'>Загрузка файла</h1>
                            <h2 align='center'>Для участия в миссии</h2>
                            <br>
                            <form method="post" enctype="multipart/form-data">
                               <div class="form">
                                    <label for="photo">Выберите файл</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                    {path}
                                    <br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </div>
                                
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        fil = f.read()
        with open('static/img/prof_pic.jpg', 'wb') as file_pic:
            file_pic.write(fil)
        return redirect('/load_photo')


def main():
    app.run(host='localhost', port=8080)


if __name__ == '__main__':
    main()
