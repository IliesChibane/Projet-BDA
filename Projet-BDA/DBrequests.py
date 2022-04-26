# importing the module
from gc import collect
from pymongo import MongoClient
   
# creating a MongoClient object 
client = MongoClient() 
     
# connecting with the portnumber and host 
client = MongoClient('localhost', 27017)
   
# accessing the database 
database = client['projet_bda'] 
    
# access collection of the database 
collection = database['world'] 

def QST1():
    return len(collection.distinct("Name"))

def QST2():
    return collection.distinct("Continent")

def QST3():
    return collection.find_one({"Name":"Algeria"})

def QST4():
    countries = []
    for post in (collection.find({"Continent":"Africa", "Population":{"$lt": 100000}}).sort("Name")):
        countries.append(post["Name"])
    return countries

def QST5():
    countries = []
    for post in (collection.find({"Continent":"Oceania", "IndepYear":{"$ne": "NA"}}).sort("Name")):
        countries.append(post["Name"])
    return countries

def QST6():
    countries = []
    for post in (collection.find().sort("SurfaceArea", -1).limit(1)):
        countries.append(post["Name"])
    return countries

def QST7():
    continents_infos = {}
    for post in collection.distinct("Continent"):
            continent_infos = {}
            count = collection.count_documents({"Continent":post})
            count_indi = collection.count_documents({"Continent":post, "IndepYear":{"$ne": "NA"}})
            continent_infos["Number of countries"] = count
            continent_infos["Size of the population"] = 0
            continent_infos["Number of independent countries"] = count_indi
            continents_infos[post] = continent_infos

    pipe = [{'$group': {'_id': "$Continent", 'total': {'$sum': '$Population'}}}]
    for post in collection.aggregate(pipeline=pipe):
        continents_infos[post["_id"]]["Size of the population"] = post["total"]

    return continents_infos

def QST8():
    n = collection.find_one({"Name":"Algeria"})["Cities"]
    count = sum(map(lambda x: int(x['Population']), n))

    return count

def QST9():
    capital = collection.find_one({"Name": "Algeria"})["Capital"]
    keys = ["Name", "Population"]
    capital_info = [capital[key] for key in keys]
    return capital_info