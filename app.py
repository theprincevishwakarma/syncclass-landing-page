from flask import Flask, render_template, Response, send_from_directory
from pathlib import Path

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sitemap.xml')
def sitemap():
    sitemap_path = Path(__file__).parent / 'sitemap.xml'

    xml_content = sitemap_path.read_text(
        encoding='utf-8-sig'
    ).lstrip()

    return Response(xml_content, mimetype='application/xml')

@app.route('/robots.txt')
def robots():
    return send_from_directory('.', 'robots.txt')



if __name__ == '__main__':
    app.run(debug=True, port=5002)