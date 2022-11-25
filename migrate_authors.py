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

            authors = set()
            for record in res:
                for article in record[0].get('articles'):
                    author = article.get("author")

                    if not author:
                        authors.add("unknown")
                        continue
                    
                    multi_authors = author.split(",")
                    authors.update(multi_authors)

            authors.remove('')

        author_tups = [(author,) for author in authors]
        write_query = 'INSERT INTO usa.author (name) VALUES %s ON CONFLICT DO NOTHING'
        with conn.cursor() as cur:
            execute_values(cur, write_query, author_tups)

if __name__ == "__main__":
    categories = ["top", "sports", "health", "business", "entertainment"]
    for cat in categories:
        main(cat)
