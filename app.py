import tmdbsimple as tmdb
from flask import Flask
from flask import request

tmdb.API_KEY = '5429c3585c7d9845b4cb42cf3879d7be'

app = Flask(__name__)
app.debug = True


@app.route("/")
def searchPage():
    html = ""
    html += "<html>\n"
    html += "<body>\n"
    html += '<form method = "POST" action="form_input">\n'
    html += 'Enter name of movie: <input type="text" name="userInput" />\n'
    html += '<input type="submit" value="submit" />\n'
    html += "</form>\n"
    html += "</body>\n"
    html += "</html>\n"
    return html

@app.route('/form_input', methods=['POST'])
def form_input():

    userInput = request.form['userInput']
    search = tmdb.Search()
    response = search.movie(query= userInput)


    html = ""
    html += "<html>\n"
    html += "<body>\n"
    html += "<table><tr><th>Movie Name</th>" \
            "<th>Popularity</th>" \
            "<th>Release Date</th>" \
            "<th>ID</th></tr>"
    for s in search.results:
        html += "<tr><td>" + \
                s['title'] + "</td><td>" + \
                str(s['popularity']) + "</td><td>" + \
                s['release_date'] + "</td><td>" + \
                str(s['id']) + "</td></tr>\n"
    html += "</table>\n"
    html += '<a href="/">Back</a>\n'
    html += "</form>\n"
    html += "</body>\n"
    html += "</html>\n"

    return html



if __name__ =="__main__":
    app.run()
