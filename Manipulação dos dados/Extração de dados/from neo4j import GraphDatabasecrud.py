from neo4j import GraphDatabase
import csv


class Neo4jConnection:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    # CRUD

    def create_node(self, label, properties):
        with self.driver.session() as session:
            session.run(f"CREATE (n:{label} $properties)",
                        properties=properties)

    def read_node(self, label, identifier, value):
        with self.driver.session() as session:
            result = session.run(
                f"MATCH (n:{label} {{{identifier}: $value}}) RETURN n", value=value)
            return result.single()[0]

    def update_node(self, label, identifier, value, updates):
        with self.driver.session() as session:
            session.run(f"MATCH (n:{
                        label} {{{identifier}: $value}}) SET n += $updates", value=value, updates=updates)

    def delete_node(self, label, identifier, value):
        with self.driver.session() as session:
            session.run(
                f"MATCH (n:{label} {{{identifier}: $value}}) DETACH DELETE n", value=value)


# Operações CRUD
if __name__ == "__main__":
    conn = Neo4jConnection("neo4j+ssc://ee9c4b83.databases.neo4j.io",
                           "neo4j", "4hEAOFQAinB6I7iVx00mSZtlFCVXST6ez4ie3MPYNtA")

    conn.create_node('Player', {'PlayerID': 1, 'PLAYER': 'Nome do Jogador',
                     'COUNTRY': 'País', 'TEAM': 'Equipe', 'ACS': 100, 'KD': 1.5})

    player = conn.read_node('Player', 'PlayerID', 1)
    print(player)

    conn.update_node('Player', 'PlayerID', 1, {'TEAM': 'Nova Equipe'})

    conn.delete_node('Player', 'PlayerID', 1)

    conn.close()
