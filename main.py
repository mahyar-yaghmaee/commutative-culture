from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/artwork")
def artwork():
    return render_template('artwork.html', title='ArtWork')


@app.route("/news")
def news():
    return render_template('news.html', title='News')


@app.route("/publications")
def publications():
    return render_template('publications.html', title='Publications')


@app.route("/services")
def services():
    return render_template('services.html', title='Services')


@app.route("/forum")
def forum():
    return render_template('forum.html', title='Forum')


@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')


if __name__ == '__main__':
    app.run(debug=True)