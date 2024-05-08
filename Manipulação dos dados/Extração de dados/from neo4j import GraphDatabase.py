from neo4j import GraphDatabase
import csv


class Neo4jConnection:

    def __init__(self, uri, user, password):
        # Colocar o URI para conectar com o Neo4j
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_indexes(self):
        with self.driver.session() as session:
            # Cria índices para as propriedades dos nós Agent
            session.run(
                "CREATE INDEX IF NOT EXISTS FOR (a:Agent) ON (a.AGENT)")
            session.run(
                "CREATE INDEX IF NOT EXISTS FOR (p:Agent) ON (p.PICK_RATE)")
            session.run("CREATE INDEX IF NOT EXISTS FOR (c:Agent) ON (c.ACS)")

    def import_agents(self, csv_file):
        with self.driver.session() as session:
            with open(csv_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Importa os dados dos agentes do arquivo CSV para o Neo4j
                    session.run(
                        "CREATE (a:Agent {AGENT: $AGENT, PICK_RATE: $PICK_RATE, ACS: $ACS})",
                        parameters={
                            'AGENT': row['AGENT'], 'PICK_RATE': row['PICK_RATE'], 'ACS': float(row['ACS'])}
                    )


if __name__ == "__main__":
    neo4j_url = "neo4j+ssc://ee9c4b83.databases.neo4j.io"
    neo4j_username = "neo4j"
    neo4j_password = "4hEAOFQAinB6I7iVx00mSZtlFCVXST6ez4ie3MPYNtA"
    csv_file = 'Arquivo CSV/Arquivo_transicao/tbl_agents.csv'

    conn = Neo4jConnection(neo4j_url, neo4j_username, neo4j_password)
    try:
        conn.create_indexes()
        conn.import_agents(csv_file)
    finally:
        conn.close()
