from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "UP"}), 200


@app.route('/sum', methods=['POST'])
def get_sum():
    data = request.get_json() or {}

    a = data.get('a', 0)
    b = data.get('b', 0)

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return jsonify({"error": "Inputs must be numbers"}), 400

    return jsonify({"result": a + b})

@app.route('/reverse-string', methods=['POST'])
def reverse_string():
    data = request.get_json() or {}

    text = data.get('text', "")

    if not isinstance(text, str):
        return jsonify({"error": "Text must be a string"}), 400

    return jsonify({"result": text[::-1]})


if __name__ == '__main__':
    app.run()
