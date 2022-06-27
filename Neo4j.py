from neo4j import GraphDatabase
from py2neo import Graph

uri             = "bolt://localhost:7474"

userName        = "neo4j"

password        = "abc"

graph = GraphDatabase.driver(uri = "bolt://localhost:7687", auth=(userName, password))


session =  graph.session()

q1 = """CREATE (Onni:person { name: "Onni"}),

                                (Elias:person { name: "Elias"}),

                                (Eetu:person { name: "Eetu"}),

                                (Leo:person { name: "Leo"}),

                                (Leena:person { name: "Leena"}),

                                (Twain:person { name: "Twain"}),

                                (Ansa:person { name: "Ansa"}),

                                (Anneli:person { name: "Anneli"}),
                                

                                (Onni)-[:friend {miles: 259}]->(Eetu),

                                (Onni)-[:friend {miles: 259}]->(Elias),

                                (Elias)-[:friend {miles: 259}]->(Leo),

                                (Leena)-[:friend {miles: 259}]->(Elias),

                                (Eetu)-[:friend {miles: 259}]->(Leena),

                                (Leena)-[:friend {miles: 259}]->(Twain),

                                (Ansa)-[:friend {miles: 259}]->(Leo),

                                (Twain)-[:friend {miles: 259}]->(Ansa),

                                (Ansa)-[:friend {miles: 259}]->(Anneli),

                                (Onni)<-[:friend {miles: 259}]-(Eetu),

                                (Onni)<-[:friend {miles: 259}]-(Elias),

                                (Elias)<-[:friend {miles: 259}]-(Leo),

                                (Leena)<-[:friend {miles: 259}]-(Elias),

                                (Eetu)<-[:friend {miles: 259}]-(Leena),

                                (Leena)<-[:friend {miles: 259}]-(Twain),

                                (Ansa)<-[:friend {miles: 259}]-(Leo),

                                (Twain)<-[:friend {miles: 259}]-(Ansa),

                                (Ansa)<-[:friend {miles: 259}]-(Anneli)"""
                                
                                
cqlShorestPath      = """MATCH (p1:person { name: 'Ansa' }),(p2:person { name: 'Elias' }), path = shortestPath((p1)-[*..15]-(p2))

                      RETURN path"""
                      
                      
nodes = session.run(q1)

shortestPath = session.run(cqlShorestPath)

print("Shortest path between nodes - Ansa and Elias:")


results = [record for record in shortestPath.data()]

print(results[0]['path'])



