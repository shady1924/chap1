import json
from pymongo import  MongoClient
import pprint
from datetime import datetime
from bson.code import Code

def getconn(dbname):
    client = MongoClient()
    db = client[dbname]
    return db

def getCollection(db, collection):
    return db[collection]

def task_III(coll):
    
    key = {"sender":1}
    initial = { "count":0 , "recipientsum":0 }
    condition = {}
    reduce = "function (obj,prev) { \
                prev.count++ ; \
                prev.recipientsum = prev.recipientsum + obj.recipients.length + obj.cc.length; }"
    result = coll.group(key=key,
            condition=condition,
            initial=initial,
            reduce=reduce
         )
    print("\n\n")    
    pprint.pprint(coll)
    for doc in result:
        print (doc)


def task_IV(coll):

    matchstr = { "date" : { "$gt" : datetime(2000, 10, 20)  } }
    pipeline = [
             { "$match": { "date" : { "$gt" : datetime(2000, 10, 20) }  } },
             {"$group": {"_id" : "$sender", "mindate" : { "$min" : "$date" } } },
            {"$sort":{ "mindate":-1 }},
             {"$project":{"_id": 1, "mindate":1}}
        ]   
    print("\n\n")
    pprint.pprint(coll)
    result = coll.aggregate(pipeline)
#     pprint.pprint(result)
    for doc in result:
        print (doc)    

def task_V(db,coll):
    mapper = Code(""" 
                function () {
                    emit(this.sender, {
                        bcc: this.bcc.length
                    })
                }                
            """)
    
    reducer = Code(""" 
                function (key, values) {
                    result = {
                        bcccnt: 0 
                    };
                for (i = 0; i < values.length; i++) {
                            result.bcccnt += 1;
                          }
                
                    return result;
                }
    """)   
    print("\n\n")    
    pprint.pprint(coll)
    result = coll.map_reduce(mapper , reducer , "emails_MapReduce_cnt" , 
                                                 query= { "bcc": { "$exists": True , "$not": {"$size": 0} } } 
                             )
    for doc in result.find():
        print (doc) 
        
    pprint.pprint("Total Count for the output map reduce collection: " + str(db.emails_MapReduce_cnt.find().count()))

def word_count(coll):
    
    result =  coll.find({},{"text":1}).limit(2)
#     pprint.pprint(list(result) )

    mapper = Code(""" 
                function () { 
                    txt=this.text ;

                    wrds =  txt.split(" ");
                    for ( i=0 ; i < wrds.length ; i++) {
                        if (  wrds[i].length >1  ) { 
                            wrd=wrds[i].toLowerCase().replace('"|,',' ');
                            wrd=wrd.replace('(\\n)+','');
                            wrd=wrd.replace('.|;|,)/gi','');
                            emit(wrd,  1  );
                            }
                    }

                }                
            """)
    
    reducer = Code(""" 
                function (key, values) {
                    result = {
                        count : 0 
                    };            
                    values.forEach  ( function(v) { result.count += 1; } ) 
                    return {result};
                }
    """)  
    
    print("\n\n")    
    pprint.pprint(coll)
    result = coll.map_reduce(mapper , reducer , "word_cnt" 
                                                ,query= {"sender" : "rosalee.fleming@enron.com" } 
                             ).find()
    for doc in result:
        print (doc)  
            
def main():
    db = getconn("enron") 
    coll = getCollection(db, "emails")
    print(db)
    print(db.collection_names(include_system_collections=False))
#    Calling task III to Develop a single Grouping query to find all senders, the number of emails that each of they sent, and the number of recipients they sent to
#     task_III(coll)
#   Calling task IV to Develop a single Aggregation query
#     task_IV(coll)
#    Map reduce
    db['emails_MapReduce_cnt'].drop()
#     task_V(db,coll)
#    word count analysis
    word_count(coll)    
                     
main()
