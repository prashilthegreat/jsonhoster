from requests import post,get
import sys
if __name__ == '__main__':    
    data = {
    "grant_type":"client_credentials",
   "client_id":"WLKv1QripyMLltQgM0K0wqsbTPUENHvv2tbnuJSX8sa5iLJKUG",
   "client_secret":"gIyKtAg8oqsz3GvPZ90bCT7XYLCHjUaV5FBBAscG"
    }
    headers = {"Content-Type": "application/json; charset=utf-8"}
	# https://api.petfinder.com/v2/oauth2/token   
    r = post("https://api.petfinder.com/v2/oauth2/token",json = data, headers = headers)   
    token = r.json()["access_token"]
    getRequest = get("https://api.petfinder.com/v2/animals",headers = {"Authorization":"Bearer "+token})
    # print(getRequest.json())
    # arg1 = sys.argv[1]

    animal_list = getRequest.json()['animals']
    if(len(sys.argv) == 1):

        for animal in animal_list:
            print("No arguments provided, showing all animals ",animal)
    elif(len(sys.argv) == 2):
        animal_type1= sys.argv[1]

        animal_list = getRequest.json()['animals']
        filtered_animals = [s for s in animal_list if s['type'] == animal_type1]
        for animal in filtered_animals:
            print("Argument: Animal type is " + animal_type1 ,animal)
    elif(len(sys.argv) == 3):
        animal_type1= sys.argv[1]
        animal_type2= sys.argv[2]
        animal_list = getRequest.json()['animals']
        filtered_animals = [s for s in animal_list if s['type'] == animal_type1 or  s['type'] == animal_type2 ]
        for animal in filtered_animals:
            print("Argument: Animal types are " + animal_type1 + animal_type2 ,animal)

