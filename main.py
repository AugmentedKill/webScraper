import requests
import bs4

url = "https://xkcd.com/"
next_url = "https://xkcd.com"

while next_url.endswith("#") == False:
	#Do Everything

	# Request the page & Soupify Request
	response = requests.get(next_url)
	soup = bs4.BeautifulSoup(response.text, 'html.parser')
	
	#Step 1 - Starting page, download image
	#	Find an isolate the img tag
	img_elem_list = soup.select("#comic img")
	img_elem = img_elem_list[0]
	img_src = img_elem["src"]
	img_src = "https:" + img_src
	# print(img_src)
	
	#	Find the name of the image
	split_img_src = img_src.split("/")
	img_name = split_img_src[-1]
	
	# Download and save the img
	print("Downloading: " + img_name)
	requested_img = requests.get(img_src)
	with open("comics/" + img_name, "wb") as image:
		image.write(requested_img.content)
		
	#Step 2 - Click back button
		prev_anchor = soup.findAll("a", {"rel": "prev"})[0]
		prev_num = prev_anchor["href"]
		next_url = url + prev_num
	
	#Step 3 - Repeat until the end