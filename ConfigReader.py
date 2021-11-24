import json

def read_config_file():
	with open("config.json", "r") as file:
		jsonString = file.read()
	return jsonString
	
def get_configuration():
	jsonString = read_config_file()
	#convert json string to a Python object
	jsonObject = json.loads(jsonString)
	config = jsonObject
	return jsonObject
		
def get_base_url():
	conf = get_configuration()
	return conf["api"]["baseUrl"]
	
base_url = get_base_url()
