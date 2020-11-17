from flask import Flask ,render_template,url_for,request,redirect
import csv
app = Flask(__name__)



# @app.route('/')
# def hello_world():
#     return 'Hello, Saikiran Lets Start Take Some time'

# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_pages(page_name):
    return render_template(page_name)

def write_to_data(data):
    with open('Database.txt',mode='a') as database:
        email=data['email']
        subject=data['subject']
        message=data['message']
        file=database.write(f'\n{email} ,{subject},{message}')

def write_to_csv(data):
    with open('Database.csv',newline='',mode='a') as database1:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer=csv.writer(database1 ,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method ==  'POST':
        data= request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        print('Something went wrong ,Try Again')




    # error = None
    # if request.method == 'POST':
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    #return render_template('login.html', error=error)




if __name__ == '__main__':
    app.run(debug=True)

