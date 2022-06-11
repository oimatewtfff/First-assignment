from flask import Flask, render_template, request
from quadratic_equation import solve_quadratic_equation

app = Flask(__name__)


@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html')


@app.route('/result', methods=['POST'])
def result_page():
    first = float(request.form['first'])
    second = float(request.form['second'])
    third = float(request.form['third'])
    title = 'Results'
    results = solve_quadratic_equation(first, second, third)
    return render_template('result.html',
                           the_title=title,
                           the_first=first,
                           the_second=second,
                           the_third=third,
                           the_results=results)


if __name__ == '__main__':
    app.run(debug=True)
