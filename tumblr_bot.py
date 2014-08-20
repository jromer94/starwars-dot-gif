import random
import os
import ConfigParser
import time
import subprocess

from tumblpy import Tumblpy
from makeGifs import makeGif

config = ConfigParser.ConfigParser()
config.read("config.cfg")
config.sections()

CONSUMER_KEY = config.get("tumblr", "consumer_key")
CONSUMER_SECRET = config.get("tumblr", "consumer_secret")
OAUTH_TOKEN = config.get("tumblr", "oauth_token")
OAUTH_TOKEN_SECRET = config.get("tumblr", "oauth_token_secret")


t = Tumblpy(
	CONSUMER_KEY,
	CONSUMER_SECRET,
	OAUTH_TOKEN,
	OAUTH_TOKEN_SECRET,
)

while True:
	quote = makeGif(random.randint(1,3), 0, rand=True, frames=20)
	quote = ' '.join(quote)

	# reduce amount of colors, because tumblr sucks
	subprocess.call(['convert',
					'star_wars.gif',
					'-layers',
					'Optimize',
					'-colors',
					'64',
					'star_wars.gif'])
	while(os.path.getsize('star_wars.gif') > 1048576):
		subprocess.call(['convert',
						'star_wars.gif',
						'-resize',
						'90%',
						'-coalesce',
						'-layers',
						'Optimize',
						'star_wars.gif'])

	photo = open('star_wars.gif', 'rb')

	post = t.post('post', blog_url='http://starwarsgifsasaservice.tumblr.com', params={'type':'photo', 'caption': quote, 'data': photo, 'tags': 'star wars, gif'})

	print "sleeping..."
	# sleep 12 hours
	time.sleep(43200)
