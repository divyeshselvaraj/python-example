import flask
import model.keywordextractor as KEModel
from flask import request

from urllib.request import urlopen
from bs4 import BeautifulSoup

import discord_code.example_bot as DiscordBot

app = flask.Flask(__name__, template_folder='templates')

#background process happening without any refreshing
@app.route('/runKeywordExtractionModel', methods=['GET', 'POST'])
def runKeywordExtractionModel():
	#url = request.args.get('url')
	#text = getTextFromURL(url)
	#print ("Running Keyword Extraction Model")
	#KEModel.runModel(text)
	DiscordBot.performSearch()
	return flask.render_template('application.html', flash_message="True")

@app.route('/show_linker')
def show():
    return flask.render_template('linker2.html')

@app.route('/')

def main():
    return(flask.render_template('application.html'))


def getTextFromURL(url):
	html = urlopen(url).read()
	soup = BeautifulSoup(html, features="html.parser")
	
	# kill all script and style elements
	for script in soup(["script", "style"]):
	    script.extract()    # rip it out
	
	# get text
	text = soup.get_text()
	
	# break into lines and remove leading and trailing space on each
	lines = (line.strip() for line in text.splitlines())
	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	# drop blank lines
	text = '\n'.join(chunk for chunk in chunks if chunk)

	return text


if __name__ == '__main__':
    app.run()