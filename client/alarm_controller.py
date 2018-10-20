import datetime

from flask import Flask
from flask_ask import Ask, statement
import logging

app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.intent('AddAlarm', mapping={'time': 'time'})
def gpio_control(time):
    try:
        date_time = datetime.datetime(time)
    except Exception as e:
        return statement('Could not translate the date.')

    print('alarm set to {}'.format(date_time))

    return statement('Setting alarm for {}'.format(time))

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5000)
