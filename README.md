# Messenger
Back-end : flask

Front-end : QtCreator
# Инструкция по разворачиванию приложения
* Активируем виртуальную среду:
```python
pip install virtualenv
virtualenv venv
source venv/bin/activate
```
* Скачиваем фреймворки
```python
pip install flask
pip install requests
pip install PyQt5
```
* Запускаем сервер и само приложение
```python
python3 server.py
python3 Messenger.py
```
* Переходим по ссылке
Running on http://127.0.0.1:5000/
# Конструкция сервера
### Статус
1. URL : http://127.0.0.1:5000/status
2. request : GET
3. Body: 
```
{
  "Count of messages", # Количество сообщений на сервере, int
  "Time on server", # Время на сервере, YYYY-MM-DD HH:MM:SS
  "server_name", # Имя сервера, строка
  "status" # Работает ли сервер, boolean
}
```
### Посланные сообщения
1. URL : http://127.0.0.1:5000/send_message
2. request : GET, POST
3. Body: 
```
{
    "wait for you": "please, send a message"
}
```
Необходим для занесения сообщений в базу данных, поэтому на самой странице нет ничего информативного

### Полученные сообщения
1. URL : http://127.0.0.1:5000/get_messages
2. request : GET
3. Body : 
```
{
  messages: [
    {
      author, # Имя автора, строка
      text, # Текст сообщения, строка   
      time # Время отправки сообщения, YYYY-MM-DD HH:MM:SS
    },    
    ...
  ]
}
```
### Случайный пользователь 
1. URL : http://127.0.0.1:5000/user/59565/
2. request : GET
3. Body : 
```
Profile page of user #[user_id]
```
