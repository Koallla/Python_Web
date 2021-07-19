from flask import Flask, flash, render_template, redirect, request
from time import sleep

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

from main import AddressBook, Name, Surname, Adress, Tag, Note, Birthday, Email, Phone, Record
from forms import AddRecordForm
from helpers import check_double


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add',  methods=['GET', 'POST'])
def add():
    form = AddRecordForm()
    if form.validate_on_submit():
        name = Name(form.name.data)
        surname = Surname(form.surname.data)
        adress_cls = Adress(form.adress.data)
        note = Note(form.note.data)
        tag = Tag(form.tag.data)

        birthday = form.birthday.data
        birthday_cls = Birthday(birthday)
        if not birthday_cls.flag:
            flash('Data birthday not correct!')
            

        email = form.email.data
        email_cls = Email(email)
        if email_cls.flag:
            data = AddressBook.get_data(AddressBook)
            if not check_double(data, 'email', email):
                flash(f'Email {email} used already!')
        else:
            flash(f'Email "{email}" not valid!')


        phone = form.phone.data
        phone_cls = Phone(phone)
        if phone_cls.flag:
            data = AddressBook.get_data(AddressBook)
            if check_double(data, 'phone', phone):
                record = Record(name, surname, adress_cls, note, tag, email_cls, phone_cls, birthday_cls)
                AddressBook.add_record(AddressBook, record)
                return redirect('/')
            else:    
                flash(f'Phone {phone} used already!')
            
        else:
            flash(f'Number {phone} is not valid! Please, enter number in format 380_________')

    return render_template('add_rec.html', form=form)
    



@app.route('/records')
def records():
    records = AddressBook.show_all_records(AddressBook)
    return render_template('records.html', records=records)





@app.route('/find', methods=['GET', 'POST'])
def find():
    if request.method == 'POST':
        query = request.form.get('query')
        data = request.form.get('data')
        record = AddressBook.show_records_for_query(AddressBook, query, data)
        return render_template('find_post.html', record=record)

    
    # record = AddressBook.show_records_for_query(AddressBook, query, data)
    return render_template('find_get.html')







if __name__ == '__main__':
    app.run(debug=True)