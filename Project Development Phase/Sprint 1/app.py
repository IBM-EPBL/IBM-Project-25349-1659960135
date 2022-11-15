from flask import Flask, render_template, redirect
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_sqlalchemy import SQLAlchemy   
from flask import request, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRETKEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False, default=0.0)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Expense('{self.title}', '{self.category}', {self.amount}, {self.date})"
# we create a fake database here since we haven't had a database yet
all_expenses = [
    {
        "id":1,
        "title":"Headphones",
        "category":"Electronics",
        "amount":100,
        "date": datetime.strptime("22-02-2019", '%d-%m-%Y')
    },
    {
        "id":2,
        "title":"BBQ and Bacons",
        "category":"Food",
        "amount":200,
        "date":datetime.strptime("12-09-2019", '%d-%m-%Y')
    },
    {
        "id":3,
        "title":"Spotify",
        "category":"Sevices",
        "amount":15,
        "date":datetime.strptime("23-08-2019", '%d-%m-%Y')
    },
    {
        "id":4,
        "title":"Netflix",
        "category":"Sevices",
        "amount":30,
        "date":datetime.strptime("23-12-2019", '%d-%m-%Y')
    }

]

class ExpenseForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    amount = DecimalField('Amount', validators=[DataRequired()])
    date = DateField('Date')
    submit = SubmitField('Submit')

    def __repr__(self):
        return f"ExpenseForm('{self.title}', '{self.category}', {self.amount}, {s.date})"

@app.route("/delete/<int:expense_id>", methods=['POST'])
def delete(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/update/<int:expense_id>", methods=['GET', 'POST'])
def update(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    form = ExpenseForm()
        # if the form is validated and submited, update the data of the item
        # with the data from the field
    if form.validate_on_submit():
        expense.title = form.title.data
        expense.category = form.category.data
        expense.amount = form.amount.data
        expense.date = form.date.data
        db.session.commit()
        return redirect(url_for('home'))
        # populate the field with data of the chosen expense 
    elif request.method == 'GET':
        form.title.data = expense.title
        form.category.data = expense.category
        form.amount.data = expense.amount
        form.date.data = expense.date
    return render_template('add.html', form=form, title='Edit Expense')

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = ExpenseForm()
    #if form successfully validated
    if form.validate_on_submit():
    
        # we create an expense object
        expense = Expense(title=form.title.data, category=form.category.data, 
                            amount=form.amount.data, date=form.date.data)
                            
        # add it to the database                     
        db.session.add(expense)
        db.session.commit()
        return redirect('/home')

    form.date.data = datetime.utcnow()
    return render_template('add.html', form=form)

@app.route('/home')
@app.route('/')
def home():
    all_expenses = Expense.query.all()
    return render_template('home.html', expenses=all_expenses)

if __name__ == '__main__':
    app.run(debug=True)