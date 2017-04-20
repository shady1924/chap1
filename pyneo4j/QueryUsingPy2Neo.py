import py2neo
from py2neo import Graph, Node, Relationship

py2neo.authenticate("localhost:7474", "neo4j", "xsharadx")

graph = Graph("http://localhost:7474/db/data/")

results=graph.run("""match (a:User)-[:FRIEND*..]-(b:User) return b
""")


# common interest between Bradley and other friends 
results=graph.run("""match (a:User{name:'Bradley'})-[:INTEREST]-(stuff)-[:INTEREST]-(newFriend) 
where not ( (a)-[:FRIEND]-(newFriend) )
return a, stuff,newFriend
""")

# Similarity of places visited by Bradley and Lisa 
results=graph.run("""match (a:User{name:'Bradley'})-[r1:VISITED]-(places)<-[r2:VISITED]-(b:User{name:'Lisa'}) 
with a,b,collect(abs(r1.times-r2.times)) as sim 
return a.name,b.name , REDUCE(s=0.0, i in sim|s+i)/SIZE(sim)  
""")


results=graph.run("""MATCH p=(d:Director)-[r:DIRECTED]->(m:Movie) RETURN p limit 1000
""")

for result in results:
    print(result)
    
