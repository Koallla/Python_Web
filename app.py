from flask import Flask, render_template, request


app = Flask(__name__)


from main import AddressBook

@app.route('/')
def index():
    return render_template('index.html')



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
    app.run()