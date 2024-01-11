@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        url = request.form['url']
        index = get_max_index()
        token = base62_encode(index)
        add_url(url, token)
        short_url = 'http://127.0.0.1:8002/{token}'.format(token=token)
        return jsonify({'short_url': short_url})
