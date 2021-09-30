import flask
import threading

app = flask.Flask(__name__)

_bad_request = "Bad request.  Add requires x and y in the querystring - .../add?x=1&y=2"

@app.route('/add/', methods=['GET'])
def add():
    addend1 = flask.request.args.get('x', None, type=float)
    if addend1 is None or _is_number(addend1) == False:
        return _bad_request, 400

    addend2 = flask.request.args.get('y', None, type=float)
    if addend2 is None or _is_number(addend1) == False:
        return _bad_request, 400

    return str(addend1 + addend2)

def _is_number(var):
    return type(var) == int or type(var) == float

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)