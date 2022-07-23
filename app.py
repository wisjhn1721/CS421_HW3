from flask import Flask, render_template, send_from_directory, url_for, redirect
from forms import StudentGradeForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'securityKey'


@app.route('/', methods=['GET', 'POST'])
def home():
    form = StudentGradeForm()
    if form.validate_on_submit():
        print('Form was valid, we can save it now!')

    return render_template('home.html', form=form)


@app.route('/grades')
def grades(request):
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
