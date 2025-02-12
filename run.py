from flask import Flask, send_from_directory
from api import api_bp
from web import web_bp
from utils import _GENERATE_FLAG, _NORMALIZING

app = Flask(__name__)

_GENERATE_FLAG()

app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(web_bp, url_prefix='/')

@app.route("/robots.txt")
def robots():
     return send_from_directory(app.static_folder, 'robots.txt')
     
@app.route("/sitemap.xml")
def sitemap_xml():
     return send_from_directory(app.static_folder, 'sitemap.xml')
     
if __name__=="__main__":
     _GENERATE_FLAG()
     app.run("0.0.0.0",debug=True)
     _NORMALIZING()