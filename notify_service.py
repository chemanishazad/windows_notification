from flask import Flask, request
from plyer import notification

app = Flask(__name__)

@app.route('/')
def index():
    return 'Notification service is running. Use POST /notify to send notifications.'

@app.route('/notify', methods=['POST'])
def notify():
    data = request.get_json()
    title = data.get('title', 'Notification')
    message = data.get('message', 'You have a new notification')

    notification.notify(
        title=title,
        message=message,
        app_name='Your App',
        timeout=10
    )
    return 'Notification sent', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
