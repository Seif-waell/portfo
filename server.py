# django and flask, learn those 2 for building servers

# flask uses ginga a templeting language


from flask import Flask ,render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/<string:page_name>')
def html_dynamic(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('F:\Python Training\Training\Server\database.csv', mode = 'a', newline = '') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n {email}, {subject}, {message}")
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
        print("message written")


@app.route('/submit_form', methods = ['POST', 'GET' ])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong try again later'