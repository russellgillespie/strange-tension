import sys
import os
import json
from discord_markdown.discord_markdown import convert_to_html

dupes = open(sys.argv[2]).read().splitlines()

f = open(sys.argv[1])
name = os.path.splitext(sys.argv[1])[0]
data = json.load(f)

# year = 2020
# month = 8
# strMonth = "09"
counter = 0
character_count = 0

container = []
messages = []
names = []

file = ""


#st = open('strange-tension' + str(year) + "_" + strMonth + '.html', 'w')
# file = open(name + str(year) + "_" + strMonth + '.txt', 'w')
file = open(name + 'start' + '.txt', 'w')
#file.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width">\n<link rel="stylesheet" href="./styles.css">\n</head>\n<body>\n<div class="content-wrapper">\n')
# file.write('<h1>' + name + '</h1>')

#Loop through all Messages in JSON file
for i in data['messages']:
	#cache message content
	c = i['content']
	n = i['author']['name']
	d = i['timestamp'][0:18]

	#Create per-name formatting
	if n in names:
		pass
	else:
		names.append(n)

	# color_class = 'class="character-' + str(names.index(n)) + '"'


	is_dupe = False

	#Check against list of duplicates from arg
	while is_dupe == False:
		for dupe in dupes:

			if str(c) == str(dupe) :
				print(i['content'] + " = " + dupe)
				print("***DUPE DETECTED***")
				print("***DUPE DETECTED***")
				print("***DUPE DETECTED***")
				is_dupe = True
				break
			elif (c.startswith("Alias ") or c.startswith("!") or c.startswith("(") and c.endswith(")")) or c.startswith('Error') or (c.startswith("(") and c.endswith(") ")) or (" !alias" in c or "!alias" in c or "Alias" in c or "msa" in c or ":"  in c):
				print(i['content'] + " : filtered")
				print("***FILTERED FORMATTING***")
				print("***FILTERED FORMATTING***")
				print("***FILTERED FORMATTING***")
				is_dupe = True
				break
			else:
				continue


		if is_dupe == False:
			messages = []
			container = []
			messages.append(i['content'])
			container.append(messages)

			#Datetime parsing helper
			# if month < 10:
			# 	strMonth = "0" + str(month)
			# else:
			# 	strMonth = str(month)

			# Check if characters will exceed 5000 limit for google TextToSpeechClient
			for message in messages:
				character_count += len(message) + 1
			if character_count > 5000:
				character_count = 0
			#Check if new month/year and close old /create new file if so
			# if i['timestamp'] and not i['timestamp'].startswith(str(year) + "-" + strMonth):
				# file.write("\n</div><!-- .content-wrapper -->\n" + "</body>" + "\n" + "</html>")
				file.close()

				#Datetime parsing helper
				# if month < 12:
				# 	month += 1
				# else:
				# 	month = 0
				# 	year += 1
				#
				# if month < 10:
				# 	strMonth = "0" + str(month)
				# else:
				# 	strMonth = str(month)

				#Create new file with year-month
				file = open(name + str(d) + '.txt', 'w')
				# file.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width">\n<link rel="stylesheet" href="./styles.css">\n</head>\n<body>\n<div class="content-wrapper">\n')
				file.write(name)

				for message in container:
					try:
						# file.write('<div ' + color_class + '>')
						file.write(message[0])
						# file.write('</div>')
						file.write("\n")
					except:
						# file.write('<div ' + color_class + '>')
						file.write(message[0])
						# file.write('</div>')
						file.write("\n")
					# else:
					# 	file.write(message[0])
					# 	file.write("\n")

				container = []
				messages = []
				is_dupe = True

			else:
				for message in container:
					try:
						# file.write('<div ' + color_class + '>')
						file.write(message[0])
						# file.write('</div>')
						file.write("\n")
					except:
						# file.write('<div ' + color_class + '>')
						file.write(message[0])
						# file.write('</div>')
						file.write("\n")
					# else:
					# 	file.write(message[0])
					# 	file.write("\n")
				container = []
				messages = []
				is_dupe = True
		else:
			is_dupe = True
