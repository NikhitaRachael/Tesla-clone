from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cybertruck")
def cybertruck():
    return render_template("cybertruck.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # use Render's assigned port or fallback to 5000 locally
    app.run(host="0.0.0.0", port=port, debug=True)
