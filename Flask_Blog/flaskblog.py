from flask import Flask, render_template

app = Flask(__name__)

posts = [{
    'author': 'Henry Eze',
    'title': 'Blog Post 1',
    'date_posted': 'April 21, 2018',
    'content': 'First post content'
},
    {
        'author': 'Chika Edeh',
        'title': 'Blog Post 2',
        'date_posted': 'April 21, 2019',
        'content': 'Second post content'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')
