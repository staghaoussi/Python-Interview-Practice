#Sylvain Taghaoussi
#Python modules refresher and practice

import requests
import re
 

def main():
	#	get html file from website
	html_file = requests.get('https://rooof.bamboohr.com/jobs/view.php?id=60')
	
	# create regex pattern so it can be reused if needed
	names_obj = re.compile(r'(\bXPath\b|\bRegular Expressions\b|\bRegEx\b|\bChrome\b)', re.IGNORECASE)
	
	# find all the matches in the html file and store them in a list
	match_list = re.findall(names_obj,html_file.text)
	
	#initializing dictionary to increment it while I loop through the match list
	dict = {'Xpath':0,'Regex':0,'Chrome':0}
	
	# loop that increments dictionary
	for match in match_list:
		if match[0].lower() == 'x':
			dict['Xpath'] += 1
		if match[0].lower() == 'r':
			dict['Regex'] += 1
		if match[0].lower() == 'c':
			dict['Chrome'] += 1
		else:
			continue
	
	#printing out number of occurences of Xpath, Regex and Chrome
	print("\nThe number of occurences of Xpath, Regex/Regular Expressions and Chrome are")
	for key in dict:
		print(key,":",dict[key])
	
	
if __name__ == "__main__":
    main()