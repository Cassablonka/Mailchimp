from flask import Flask, render_template, request
from mailchimp3 import MailChimp
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form['fullname']
        email = request.form['email']
        marks_10 = request.form['10th']
        marks_12 = request.form['12th']
        key = os.environ.get('API_KEY')
        list_id = os.environ.get('LIST_ID')
        client = MailChimp(key, '{}-{}'.format('Cassa2006', 'us5'))
        if client.lists.members.create(list_id, {'email_address': email, 'status': 'subscribed', 'merge_fields': {'FNAME': name, '10TH': marks_10, '12TH': marks_12,}}):
            return render_template('success.html')
    return render_template('index.html')


if __name__ == '__main__':
    app.run()