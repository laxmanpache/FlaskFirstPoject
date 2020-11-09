from flask import Flask, render_template

app = Flask(__name__)
post = [

    {
        'title': "first post",
        'author': 'laxman',
        'date_of_posted': '8 nov',
        'content': 'MY content'
    },

    {
        'title': "second post",
        'author': 'ram',
        'date_of_posted': '9 nov',
        'content': 'MY second post content'
    }
]


@app.route('/')
@app.route('/home')
def hi():
    return render_template('home.html', post=post)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


app.run(debug=True)
