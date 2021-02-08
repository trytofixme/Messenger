import time
from datetime import datetime
from flask import Flask, Response, request, make_response, redirect
import random


app = Flask(__name__)
db = [{'text': 'Hello', 'author': 'Администратор', 'time': time.time()}]


@app.route("/")
def main_page():
    return "Да, это мой первый мессенджер и что?" \
           "<br><a href='/status'>Статус</a>" \
           "<br><a href='/send_message'>Посланные сообщения</a>" \
           "<br><a href='/get_messages'>Полученные сообщения</a>" \
           "<br><a href='/user/{}'>Случайный пользователь </a>".format(random.randint(1, 100000))\



@app.route('/set-cookie')
def set_cookie():
    res = make_response("Cookie setter")
    res.set_cookie("favorite-color", "skyblue", 60*60*24*15)
    res.set_cookie("favorite-font", "sans-serif", 60*60*24*15)
    return res


@app.route('/transfer')
def transfer():
    return redirect("https://localhost:5000/login", code=301)


@app.route('/user/<user_id>/')
def user_profile(user_id):
    user_id = random.randint(1, 10000)
    return "Profile page of user #{}".format(user_id)


@app.route("/status")
def status():
    dn = datetime.now()
    stats = {'status': True, 'server_name': 'Messenger',
             'Count of messages': len(db), 'Time on server': dn.strftime('%Y-%m-%d %H:%M:%S')}
    return stats


@app.route("/send_message", methods=['GET', 'POST'])
def send_message():
    if request.json is not None:
        data = request.json
        if not isinstance(data, dict):
            return Response('not json', 400)

        text = data.get('text')
        author = data.get('author')

        if isinstance(text, str) and isinstance(author, str):
            db.append({
                'text': text,
                'author': author,
                'time': time.time()
            })
            return Response('ok')
        else:
            return Response('wrong format', 400)
    return {
        'wait for you': 'please, send a message'
    }


@app.route("/get_messages")
def get_message():
    after = request.args.get('after', '0')
    try:
        after = float(after)
    except:
        return Response('wrong format', 400)

    new_messages = [message for message in db if message['time'] > after]

    return {'messages': new_messages}


if __name__ == "__main__":
    app.run(debug=True)
