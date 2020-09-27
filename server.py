from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
print(app)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/works')
def works():
    return render_template('works.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/work')
def work():
    return render_template('work.html')


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou')
    else:
        return 'someting went wrong. try again'
