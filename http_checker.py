from flask import Flask, request, jsonify

app = Flask(__name__)

def get_headers():
    data = {}
    headers = request.headers
    for header in headers:
        key = header[0]
        value = header[1]
        data[key] = value
    return data


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def main_route():
    headers = get_headers()
    response = {
        "code": 200,
        "message": "Kau ni ape?, kau tinggal sini ke?",
        "data": {
            "method": request.method,
            "path": '/',
            "headers": headers,
            "remote_addr": request.remote_addr,
            "scheme": request.scheme,
            "server": request.server,
            "query_string": str(request.query_string)
        },

    }
    # print(request.query_string)
    # print(type(request.query_string))
    return jsonify(response), 200


@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def catch_all_path(path):
    headers = get_headers()
    response = {
        "message": "Not Found",
        "code": 404,
        "data": {
            "method": request.method,
            "path": '/' + path,
            "headers": headers,
            "remote_addr": request.remote_addr,
            "scheme": request.scheme,
            "server": request.server,
            "query_string": str(request.query_string)
        },
    }
    return jsonify(response), 404

# if __name__ == '__main__':
#     app.run()
