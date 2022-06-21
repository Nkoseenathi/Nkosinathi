from neo4j import GraphDatabase
from SPARQLWrapper import SPARQLWrapper, JSON
class connector:
    
    conn=''
    session=''
    sparql=''
    
    '''
    This methd connects to the neo4j database and the SPARQL endpoint
    '''
    def connect(self):
        self.sparql = SPARQLWrapper("https://makg.org/sparql") #URL for connecting to the microsoft academic graph SPARQL endpoint
        self.conn = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j","jnkosi")) # Connnect to the neo4j database 
        self.session = self.conn.session()#Create a session for the connection        
    '''
    This method executes neo4j queries passed into it
    '''
    def execute(self,query):
        nodes = self.session.run(query)#executes query
        return ((nodes.data()))#Return results from the database
    '''
    This method executes SPARQL queries
    '''
    def sparqlExecute(self,query):
        self.sparql.setQuery(query)#Executes the query
        self.sparql.setReturnFormat(JSON)#Set the format that the results are going to be in to JSON
        results = self.sparql.query().convert()#Get the results     
        return results#Return the results
    '''
    This nethod closes the connection to the neo4j database
    '''
    def close(self):
        self.conn.close()#Close connection
        
    
        
    