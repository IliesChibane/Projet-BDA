# importing the module
from gc import collect
from tokenize import Name
from pymongo import MongoClient
   
# creating a MongoClient object 
client = MongoClient() 
     
# connecting with the portnumber and host 
client = MongoClient('localhost', 27017)
   
# accessing the database 
database = client['BDD'] 
    
# access collection of the database 
collection = database['world'] 

def QST1(): # Déterminer le nombre exact de pays 
    return len(collection.distinct("Name")) #or return collection.distinct("Name").length

def QST2(): # Lister les différents continents 
    return collection.distinct("Continent")

def QST3(): # Lister les informations de l’Algérie
    return collection.find_one({"Name":"Algeria"})

def QST4(): #  Lister les pays du continent Africain, ayant une population inférieure à 100000 habitants
    countries = []
    for post in (collection.find({"Continent":"Africa", "Population":{"$lt": 100000}},{"Name" :1}).sort("Name")):
        countries.append(post["Name"])
    return countries

def QST5(): # Lister les pays indépendant du continent océanique 
    countries = []
    for post in (collection.find({"Continent":"Oceania", "IndepYear":{"$ne": "NA"}},{"Name" :1}).sort("Name")):
        countries.append(post["Name"])
    return countries

def QST6(): # Quel est le plus gros continent en termes de surface ? (un seul continent affiché à la fin) 
    countries = []
    for post in (collection.find().sort("SurfaceArea", -1).limit(1)):
        countries.append(post["Name"])
    return countries

def QST7(): #  Donner par continents le nombre de pays, la population totale et en bonus le nombre de pays indépendant. 
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

def QST8(): #  Donner la population totale des villes d’Algérie 
    n = collection.find_one({"Name":"Algeria"})["Cities"]
    count = sum(map(lambda x: int(x['Population']), n))

    return count

def QST9(): #  9. Donner la capitale (uniquement nom de la ville et population) d’Algérie 
    capital = collection.find_one({"Name": "Algeria"})["Capital"]
    keys = ["Name", "Population"]
    capital_info = [capital[key] for key in keys]
    return capital_info

def QST10(): # 10. Quelles sont les langues parlées dans plus de 15 pays ? 
    '''
            db.world.aggregate([
        {
        $addFields: { Langue : {$concatArrays: ["$OffLang","$NotOffLang" ] } }
        },
        {$unwind: "$Langue"
        },
        { $group: {
            _id:"$Langue.Language",
            "nb" : {$sum :1}        
        }
        },
        { $match: { "nb": { $gt: 15 } } }
    ])

    '''
    languages = []
    pipe = [{'$addFields': { "Langue" : {'$concatArrays': ["$OffLang","$NotOffLang" ] } }},{'$unwind': "$Langue"},{'$group': { "_id":"$Langue.Language", "Number of Countries" : {'$sum' :1}}}, { '$match': { "nb": { '$gt': 15 } } }]

    for post in  collection.aggregate(pipeline=pipe):
        languages.append(post)
    return languages


def QST11(): # 11. Calculer pour chaque pays le nombre de villes (pour les pays ayant au moins 100 villes), en les triant par ordre décroissant du nombre de villes
    '''
    db.world.aggregate([
    {   
        $addFields: { villes : {$size: { "$ifNull": [ "$Cities", [] ] } } }
    }, 
    {
      $match: {
        villes: { $gt: 100 }
      }
    },
    {   $sort: {"villes":-1}  },
    {
       $project: {
            _id: "$Name",
            "Number of Cities" :"$villes"
       }
    }
])
    '''
    pays = []
    pipe = [{ '$addFields': { "villes" : {'$size': { "$ifNull": [ "$Cities", [] ] } } }}, {'$match': {"villes": { '$gt': 100 }}},{   '$sort': {"villes":-1}  },{'$project': {"_id": "$Name","Number of Cities" :"$villes"}}]
    for post in  collection.aggregate(pipeline=pipe):
        pays.append(post)
    return pays

def QST12(): # 12. Lister les 10 villes les plus habitées, ainsi que leur pays, dans l’ordre décroissant de la population
    '''
            db.world.aggregate([
        {$unwind: "$Cities"
        },
        {$sort: {"Cities.Population":-1} },
        { $limit : 10 },
        {$sort: {"Cities.Population":1} },
        {
        $project: {
            _id:"$Cities.Name",
            "Country":"$Name",
            "City Population":"$Cities.Population"
                }
        }
    ])
    '''
    villes = []
    pipe = [{'$unwind': "$Cities"},{'$sort': {"Cities.Population":-1} },{ '$limit' : 10 },{'$sort': {"Cities.Population":1} },{'$project': { "_id":"$Cities.Name","Country":"$Name","City Population":"$Cities.Population"}}]
    for post in  collection.aggregate(pipeline=pipe):
        villes.append(post)
    return villes

def QST13(): # 13. Lister les pays pour lesquels l’Arabe est une langue officielle 
    '''
    db.world.find({"OffLang.Language":{$eq:"Arabic"}},{"Name":1})
    '''
    countries =[]
    for post in (collection.find({"OffLang.Language":{'$eq':"Arabic"}},{"Name":1})):
        countries.append(post["Name"])
    return countries

def QST14(): # 14. Lister les 5 pays avec le plus de langues parlées 
    '''
    db.world.aggregate([
    {
        $addFields: { c : {$concatArrays: ["$OffLang","$NotOffLang" ] } }
    },
    {   
        $addFields: { langs : {$size: { "$ifNull": [ "$c", [] ] } } }
        
    }, 
    {   
        $sort: {"langs":-1} 
    },
    { $limit : 5 },
    {
       $group: {
            _id:"$Name"
       }
    }
])
'''
    countries =[]
    pipe = [ {'$addFields': { "c" : {'$concatArrays': ["$OffLang","$NotOffLang" ] } }},{  '$addFields': { "langs" : {'$size': { "$ifNull": [ "$c", [] ] } } }},{ '$sort': {"langs":-1} },{ '$limit' : 5 },{'$group': {"_id":"$Name"}}]

    for post in collection.aggregate(pipeline=pipe):
        countries.append(post["_id"])
    return countries

def QST15(): # 15. Lister les pays pour lesquels la somme des populations des villes est supérieure à la population du pays. 
    '''
        db.world.aggregate([
    {
        $addFields: { somme : {$sum: "$Cities.Population"}  } 
    },
    {
        $addFields:{comp : {$cmp: ['$somme','$Population']}}
    },
    {$match: {comp:{$gt:1}}},
    {
      $project: {
            _id:"$Name",
            "Total Cities Population":"$somme",
            "Country Population":"$Population"
      }
    }
])
    '''
    countries =[]
    pipe = [    {
        '$addFields': { "somme" : {'$sum': "$Cities.Population"}  } 
    },
    {
        '$addFields':{"comp" : {'$cmp': ['$somme','$Population']}}
    },
    {'$match': {"comp":{'$gt':1}}},
    {
      '$project': {
            "_id":"$Name",
            "Total Cities Population":"$somme",
            "Country Population":"$Population"
      }
    }]

    for post in collection.aggregate(pipeline=pipe):
        countries.append(post["_id"])

    return countries




