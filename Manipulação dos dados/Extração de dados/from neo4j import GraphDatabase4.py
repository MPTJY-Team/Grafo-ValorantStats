from neo4j import GraphDatabase
import csv


class Neo4jConnection:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_indexes(self):
        with self.driver.session() as session:
            # Cria um índice para a propriedade TEAM do nó Team
            session.run("CREATE INDEX IF NOT EXISTS FOR (t:Team) ON (t.TEAM)")

    def import_teams(self, csv_file):
        with self.driver.session() as session:
            with open(csv_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Cria o nó Team com as propriedades do arquivo CSV
                    session.run(
                        "CREATE (t:Team {TeamID: $TeamID, TEAM: $TEAM, COUNTRY: $COUNTRY})",
                        parameters={
                            'TeamID': int(row['TeamID']),
                            'TEAM': row['TEAM'],
                            'COUNTRY': row['COUNTRY']
                        }
                    )


if __name__ == "__main__":
    neo4j_url = "neo4j+ssc://ee9c4b83.databases.neo4j.io"
    neo4j_username = "neo4j"
    neo4j_password = "4hEAOFQAinB6I7iVx00mSZtlFCVXST6ez4ie3MPYNtA"
    csv_file = 'Arquivo CSV/Arquivo_transicao/tbl_teams.csv'

    conn = Neo4jConnection(neo4j_url, neo4j_username, neo4j_password)
    try:
        conn.create_indexes()
        conn.import_teams(csv_file)
    finally:
        conn.close()
