from flask import Flask, render_template, request

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Shimla',
        'salary': 'Rs. 12,00,000'
    },
    {
        'id': 2,
        'title': 'Full-Stack web developer',
        'location': 'Mohali',
        'salary': 'Rs. 9,00,000'
    },
    {
        'id': 3,
        'title': 'Web designer',
        'location': 'Delhi',
        'salary': 'Rs. 8,00,000'
    },
    {
        'id': 4,
        'title': 'Programmer',
        'location': 'Germany',
        'salary': 'Rs. 11,00,000'
    }
]


@app.route("/")
def index():

    return render_template("index.html", jobs=JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
