from psycopg2 import connect
from psycopg2.extras import execute_values

# Get this from ENV variables or configuration store
config = {
    "host": "0.0.0.0",
    "dbname": "news",
    "user": "root",
    "password": "root",
    "port": "5432"
}
    

def main(category: str):

    with connect(**config) as conn:
        read_query = f'SELECT news FROM usa.{category}'

        with conn.cursor() as cur:
            cur.execute(read_query)
            res = cur.fetchall()

            news_sources = set()
            for record in res:
                for article in record[0].get('articles'):
                    source = article.get("source")
                    news_sources.add(source.get("name"))

        names = [(name,) for name in news_sources]

        write_query = 'INSERT INTO usa.publisher (name) VALUES %s ON CONFLICT DO NOTHING'
        with conn.cursor() as cur:
            execute_values(cur, write_query, names)

if __name__ == "__main__":
    categories = ["top", "sports", "health", "business", "entertainment"]
    for cat in categories:
        main(cat)
