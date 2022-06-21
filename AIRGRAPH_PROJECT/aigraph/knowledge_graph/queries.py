from knowledge_graph import connector

class queries:
    
    connect = connector.connector() #Create connector object
    
    '''
    This method is used to open a conection to the neo4j database by calling the connect method from the connector class
    '''
    def open(self):
        self.connect.connect() #Open connection
    
    '''
    This method returns all the local researcher specialising in AI
    '''
    def match(self):
        
        qmatch = 'match (res:Surname)-[h:Has_A]-(r:rating) where res.pField CONTAINS "Artificial intelligence" or (res.sField CONTAINS "Artificial intelligence") return res,r' #Query for all AI researchers
        match = self.connect.execute(qmatch) #Execute query and store results in the match variable
        return  match #Return the results of the executed query
              
    '''
    This method returns the number of new AI researchers each year
    '''
    def year(self):
        
        years=[] #Used for storing the results in a list instead of a dictionary
        qyear = 'match (res:Surname)-[h:Has_A]-(r:rating) where res.pField CONTAINS "Artificial intelligence" or (res.sField CONTAINS "Artificial intelligence")  return res,r order by r.rStart' #Query for extracting new researchers for each year
        year = self.connect.execute(qyear) # execute query and store results in year variable
        
        #Add resutls in a list
        for node in year:
            (years.append(node['r']['rStart']))  
        return years #Return the list
    
    '''
    This method is used to search a researcher From the database
    @Surname: The surname of the researcher to be searched
    '''
    def search(self,surname):
        
        qsearch = 'match (res:Surname)-[h:Has_A]-(r:rating) where res.pField CONTAINS "Artificial intelligence" or (res.sField CONTAINS "Artificial intelligence") and (res.Surname="'+surname+'") return res,r' #Query for searhing researcher from database
        found = self.connect.execute(qsearch)  #Execute query and store results in found variable
        return (found)  #Return the results
    
    '''
    This method returns all the instistutions grouped by the different ratings that each institution has
    '''
    def ratingGraph(self):
        
        qrating ='match (res:Surname)-[h:Has_A]-(r:rating),(res:Surname)-[b:Is_Based]-(inst:Institution) where res.pField CONTAINS "Artificial intelligence" or (res.sField CONTAINS "Artificial intelligence")  return count(r),count(inst),inst.Institution,r.Rating order by inst.Institution' #Query for grouping institutions by rating
        ratings = self.connect.execute(qrating) #Execute query and store results in ratings variable
        return ratings #return the ratings variable
    
    ''' 
    This method returns the 5 most intensive AI research instituitions which are UCT, WITS, UP, SU and UKZN, and returns the number of citations for each instituion
    '''
    def topUniversities(self):
        
        qTop=("PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>"
              +"\nPREFIX magc: <https://makg.org/class/>"
              +"\nPREFIX dcterms: <http://purl.org/dc/terms/>"
              +"\nPREFIX foaf: <http://xmlns.com/foaf/0.1/>"
              +"\nPREFIX fabio: <http://purl.org/spar/fabio/>"
              +"\nPREFIX prism: <http://prismstandard.org/namespaces/basic/2.0/>"
              +"\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#>"
              +"\nPREFIX org: <http://www.w3.org/ns/org#>"
              +"\nPREFIX magp: <https://makg.org/property/>"
              +"\nSELECT distinct ?affilName ?citCountAffil"
              +"\nWHERE {"
              +"\n?paper rdf:type magc:Paper ."
              +'\n?paper prism:keyword "artificial intelligence"^^xsd:string .'
              +"\n?paper fabio:hasDiscipline ?field ."
              +"\n?paper fabio:hasDiscipline ?field ."
              +"\n?paper dcterms:title ?paperTitle ."
              +"\n?paper dcterms:creator ?author ."
              +"\n?author org:memberOf ?affiliation ."
              +"\n?affiliation foaf:name ?affilName ."
              +"\n?affiliation magp:citationCount ?citCountAffil ."
              +"\n?paper prism:publicationDate ?paperPubDate ."
              +'\nfilter (str(?affilName)="University of the Witwatersrand"|| str(?affilName)="University of Cape Town"||'
              +'\nstr(?affilName)="University of Pretoria"||str(?affilName)="University of KwaZulu-Natal"||str(?affilName)="Stellenbosch University")'
              +"}"
              +"\nGROUP BY ?affilName ?citCountAffil"
              +"\nORDER BY DESC(?citCountAffil)"
              +"\nLIMIT 100") #SPAQL query for retrieving the top 5 AI research institutions 
        return self.connect.sparqlExecute(qTop) #Execute the query and return the results
    
    '''
    This method returns all the research paper titles that are associated with AI for all the Top 5 institutions 
    '''
              
    def topics(self):
                
        qTopics = ("PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>"
                   +"\nPREFIX magc: <https://makg.org/class/>"
                   +"\nPREFIX dcterms: <http://purl.org/dc/terms/>"
                   +"\nPREFIX foaf: <http://xmlns.com/foaf/0.1/>"
                   +"\nPREFIX fabio: <http://purl.org/spar/fabio/>"
                   +"\nPREFIX prism: <http://prismstandard.org/namespaces/basic/2.0/>"
                   +"\nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#>"
                   +"\nPREFIX org: <http://www.w3.org/ns/org#>"
                   +"\nPREFIX magp: <https://makg.org/property/>"
                   +"\nSELECT distinct ?affilName ?citCountAffil ?paperTitle"
                   +"\nWHERE {"
                   +"\n?paper rdf:type magc:Paper ."
                   +'\n?paper prism:keyword "artificial intelligence"^^xsd:string .'
                   +"\n?paper fabio:hasDiscipline ?field ."
                   +"\n?paper dcterms:title ?paperTitle ."
                   +"\n?paper dcterms:creator ?author ."
                   +"\n?author org:memberOf ?affiliation ."
                   +"\n?affiliation foaf:name ?affilName ."
                   +"\n?affiliation magp:citationCount ?citCountAffil ."
                   +"\n?paper prism:publicationDate ?paperPubDate ."
                   +'\nfilter (str(?affilName)="University of the Witwatersrand"|| str(?affilName)="University of Cape Town"||'
                   +'\nstr(?affilName)="University of Pretoria"||str(?affilName)="University of KwaZulu-Natal"||str(?affilName)="Stellenbosch University")' 
                   +"\n}"
                   +"\nGROUP BY ?affilName ?citCountAffil ?paperTitle" 
                   +"\nORDER BY DESC(?citCountAffil)"
                   +"\nLIMIT 100") #Query for retrieving all papers with AI in their title
        return self.connect.sparqlExecute(qTopics) #Execute the query and return the results
          
        
    '''This method uses the close method from the connector class to close the connection to the database
    '''
    def close(self):
        self.connect.close() #Close connection