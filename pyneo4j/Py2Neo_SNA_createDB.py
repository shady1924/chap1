import py2neo
from py2neo import Graph, Node, Relationship

py2neo.authenticate("localhost:7474", "neo4j", "neo4j1")

graph = Graph("http://localhost:7474/db/data/")
graph.delete_all()

# Create data on Users and Relationships
bradley = Node("User", name="Bradley", surname="Green", age=24, city="Los Angeles")
matthew = Node("User", name="Matthew", surname="Cooper", age=36, city="Los Angeles")
lisa = Node("User", name="Lisa", surname="Adams", age=15, city="New York")
annie = Node("User", name="Annie", surname="Behr", age=25, city="Chicago")
ripley = Node("User", name="Ripley", surname="Aniston", city="Los Angeles")
john = Node("User", name="John", surname="Goodman", age=34, city="New York")
amy = Node("User", name="Amy", surname="Cooper", age=22)
mark = Node("User", name="Mark", surname="McAdams", age=17, city="Los Angeles")
dennis = Node("User", name="Dennis", surname="Lemon", age=42, city="Los Angeles")
bradley_matthew = Relationship(bradley,"FRIEND",matthew)
bradley_ripley = Relationship(bradley,"FRIEND",ripley)
bradley_john = Relationship(bradley,"FRIEND",john)
matthew_bradley = Relationship(matthew,"FRIEND",bradley)
lisa_matthew = Relationship(lisa,"FRIEND",matthew)
lisa_annie = Relationship(lisa,"FRIEND",annie)
annie_lisa = Relationship(annie,"FRIEND",lisa)
annie_matthew = Relationship(annie,"FRIEND",matthew)
annie_ripley = Relationship(annie,"FRIEND",ripley)

graph.create(bradley_matthew|matthew_bradley|bradley_ripley|bradley_john|lisa_matthew|lisa_annie|annie_lisa|annie_matthew|annie_ripley)
graph.create(amy|mark|dennis)


# Create data on Interests
music=Node("Interest", name='music')
sports=Node("Interest", name='sports')
dance=Node("Interest", name='dance')
bradley_music=Relationship(bradley,"INTEREST",music)
bradley_dance=Relationship(bradley,"INTEREST",dance)
john_dance=Relationship(john,"INTEREST",dance)
matthew_sports=Relationship(matthew,"INTEREST",sports)    
lisa_music=Relationship(lisa,"INTEREST",music)   
lisa_dance=Relationship(lisa,"INTEREST",dance)    
annie_sports=Relationship(annie,"INTEREST",sports)    
annie_music=Relationship(annie,"INTEREST",music)
ripley_music=Relationship(ripley,"INTEREST",music)
ripley_dance=Relationship(ripley,"INTEREST",dance)    
amy_sports=Relationship(amy,"INTEREST",sports)    
amy_dance=Relationship(amy,"INTEREST",dance)    
mark_music=Relationship(mark,"INTEREST",music)
mark_dance=Relationship(mark,"INTEREST",dance)    

graph.create(music|sports|dance)
graph.create(bradley_music|bradley_dance|john_dance|matthew_sports|lisa_music|lisa_dance)
graph.create(annie_sports|annie_music|ripley_music|ripley_dance|amy_sports|amy_dance|mark_music|mark_dance)



# Add places visited
pl1=Node("Place", ptype='Disco')
pl2=Node("Place", ptype='Coffee bar')
pl3=Node("Place", ptype='Church')
pl4=Node("Place", ptype='College')
pl5=Node("Place", ptype='pizza Corner')
pl6=Node("Place", ptype='Stadium')

class VISITED(Relationship): pass
bradley_pl1=VISITED(bradley,pl1,times=5)
bradley_pl3=VISITED(bradley,pl3, times=1)
lisa_pl1=Relationship(lisa,"VISITED",pl1,times=2)
lisa_pl2=Relationship(lisa,"VISITED",pl2,times=3)

graph.create(pl1|pl2|pl3|pl4|pl5|pl6|bradley_pl1|bradley_pl3|lisa_pl1|lisa_pl2)


# Add data on activity status
st1=Node("Status", text='I am sleeping', date='20150103')
st2=Node("Status", text='Going to ibiza', date='20101215')
st3=Node("Status", text='Added mark as friend', date='20130106')
st4=Node("Status", text='Going to college', date='20170102')
st5=Node("Status", text='Eating pizza', date='20150607')
st6=Node("Status", text='drinking coffee', date='20121212')
bradley_st1=Relationship(bradley,"STATUS",st1)
bradley_st2=Relationship(bradley,"STATUS",st2)
matthew_st3=Relationship(matthew,"STATUS",st3)
lisa_st4=Relationship(lisa,"STATUS",st4)
lisa_st5=Relationship(lisa,"STATUS",st5)
annie_st6=Relationship(annie,"STATUS",st6)

graph.create(st1|st2|st3|st4|st5|st6|bradley_st1|bradley_st2|matthew_st3|lisa_st4|lisa_st5|annie_st6)



# Create Rating data
bradley_rate_pl1=Relationship(bradley, "RATED", pl1, rating=5)
bradley_rate_pl3=Relationship(bradley, "RATED", pl3, rating=4)
lisa_rate_pl1=Relationship(lisa, "RATED", pl1, rating=2)
lisa_rate_pl2=Relationship(lisa, "RATED", pl2, rating=3)

graph.create(bradley_rate_pl1|bradley_rate_pl3|lisa_rate_pl1|
            lisa_rate_pl2)



