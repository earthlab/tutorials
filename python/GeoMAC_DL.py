#Acquiring fire data from the GeoMAC API
#
#Author: Matt Oakley
#Date: 07/25/2016

# Imports #
from bs4 import BeautifulSoup
import urllib2
import wget
import sys
import codecs

# Usage #
# ./python GeoMAC_API_Fire_Data.py <server> <file_name> <layer_numbers> <layer_option>
#Note: layer_numbers must be separated by periods '.' and contain no spaces
#Example: python ./GeoMAC_API_Fire_Data.py 1 firedata 1.3.10 1
#This will create a file named "firedata" with a composite image consisting of  layers 1, 3, 10 from the first server


#========================================================================================
#Function: get_servers																
#    																					
#input:		lidar_raster - None
#																						
#desc: 		Create a list of the available servers on GeoMAC's website				
#========================================================================================
def get_servers():
	#Open the homepage and extract links
	URL = "http://www.geomac.gov/services.shtml"
	page = urllib2.urlopen(URL)
	soup = BeautifulSoup(page, "lxml")
	content = soup.find('div', class_ = 'content')
	servers = content.findAll('a')

	#Create list of server links
	server_list = []
	for i in range(0, len(servers)):

		#Disregard service capability files
		if "WMSServer?" in str(servers[i]):
			continue
		else:
			link = servers[i].text
			link = link.encode('utf8')
			server_list.append(link)
	return server_list

#========================================================================================
#Function: choose_server															
#    																					
#input:		server_list - List of servers available on the GeoMAC website
#			cmd_arg - 0: Run interactively
#					  Otherwise, represents which number server to download from
#																						
#desc: 		Generate the URL corresponding the requested server				
#========================================================================================
def choose_server(server_list, cmd_arg):
	#If no arugments provided, let user choose which server they want to DL from
	if cmd_arg == 0:
		print "--------------------------------------------"
		for i in range(0, len(server_list)):
			print str(i + 1) + ": " + server_list[i]
		server_choice = int(raw_input("Number of server you'd like to download data from: ")) - 1
		if server_choice > len(server_list):
			print "Invalid server entry"
			exit()
		URL = server_list[server_choice]
		return URL

	#Otherwise, generate URL from argument
	else:
		server_choice = cmd_arg - 1
		if server_choice > len(server_list):
			print "Invalid server entry"
			exit()
		URL = server_list[server_choice]
		return URL

#========================================================================================
#Function: get_filename																
#    																					
#input:		lidar_raster - None
#																						
#desc: 		If running interactively, get the filename that the user wants to name
#			their downloaded KMZ file				
#========================================================================================
def get_filename():
	print "------------------------------------------------"
	filename = raw_input("Enter what you'd like to name the downloaded KMZ file: ")
	return filename

#========================================================================================
#Function: choose_layers																
#    																					
#input:		URL - URL to server hosting data
#			cmd_arg - 0: Run interatively
#					  Otherwise, represents which layers to download
#																						
#desc: 		Get the available layers from the GeoMAC server and have the user
#			choose which layers they want downloaded				
#========================================================================================
def choose_layers(URL, cmd_arg):
	#Get the layer names from the server
	layers = []
	page = urllib2.urlopen(URL)
	soup = BeautifulSoup(page, "lxml")
	layer_list = soup.findAll('li')
	for i in range(0, len(layer_list)):
		layer = layer_list[i]
		layer_name = layer.find('a')
		layer_name = layer_name.text
		layer_name = layer_name.encode('utf8')
		layers.append(layer_name)
	
	#Run interactively, user inputs which layer numbers they want
	if cmd_arg == 0:
		print "------------------------------------------------"
		for i in range(0, len(layers)):
			print str(i) + ": " + layers[i]
		print "\n"
		print "Example: '1,3,7'"
		layer_choice = raw_input("Enter the numbers of layers you wish to download: ")

		#Ensure valid layer options
		layer_list = layer_choice.split(',')
		for i in range(0, len(layer_list)):
			if int(layer_list[i]) > len(layers) - 1:
				print "Invalid layer choice: " + str(layer_list[i])
				exit()
		return layer_choice

	#Otherwise, generate list of layers from argument
	else:
		layer_arg = cmd_arg.split('.')
		layer_choice = ""
		
		#Ensure valid layer options
		for i in range(0, len(layer_arg)):
			if int(layer_arg[i]) > len(layers) - 1:
				print "Invalid layer choice: " + str(layer_arg[i])
				exit()
			else:
				continue

		#Generate comma separated list of layers
		for i in range(0, len(layer_arg)):
			if i != len(layer_arg) - 1:
				layer_choice = layer_choice + layer_arg[i] + ","
			else:
				layer_choice = layer_choice + layer_arg[i]

		return layer_choice

#========================================================================================
#Function: choose_layer_options														
#    																					
#input:		cmd_arg - 0: Run interactively
#					  Otherwise, represents which layer option to use
#																						
#desc: 		Specify how the downloaded data should be represented				
#========================================================================================
def choose_layer_options(cmd_arg):

	#Run interactively, user inputs which layer option they want
	if cmd_arg == 0:
		print "------------------------------------------------"
		print "1. Composite (All layers as a single composite image)"
		print "2. Separate Image (Each layer as a separate image)"
		print "3. Non-Composite (Vector layers as vectors and raster layers as images)"
		print "\n"
		option_choice = raw_input("Enter which layer option you want: ")
	else:
		option_choice = cmd_arg

	#Generate option in string format to be used in final URL
	if option_choice == "1":
		option = "composite"
	elif option_choice == "2":
		option = "separateImage"
	elif option_choice == "3":
		option = "nonComposite"
	else:
		print "Invalid layer option: " + option_choice
		exit()
	
	return option

#========================================================================================
#Function: DL_KML															
#    																					
#input:		base_URL - URL to server
#			filename - Name to be used for downloaded KMZ file
#			layers - Comma separated list of layers to be downloaded
#			layer_option - How to represent downloaded data/layers
#																						
#desc: 		Download the KMZ file corresponding to user input				
#========================================================================================
def DL_KMZ(base_URL, filename, layers, layer_option):
	URL = base_URL + "/generatekml?docName=" + filename + "&layers=" + layers + "&layerOptions=" + layer_option
	wget.download(URL)


def main(argv):
	servers = get_servers()
	if len(argv) > 1:
		server = int(argv[1])
		filename = argv[2]
		server_URL = choose_server(servers, server)
		layers = choose_layers(server_URL, argv[3])
		layer_option = choose_layer_options(argv[4])
		DL_KMZ(server_URL, filename, layers, layer_option)
	
	else:
		filename = get_filename()
		server_URL = choose_server(servers, 0)
		layers = choose_layers(server_URL, 0)
		layer_option = choose_layer_options(0)
		DL_KMZ(server_URL, filename, layers, layer_option)

if __name__ == "__main__":
	main(sys.argv)