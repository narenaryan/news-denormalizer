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

        with conn.cursor() as cur1:
            cur1.execute(read_query)
            res = cur1.fetchall()

            for record in res:
                news_articles = []
                for article in record[0].get('articles'):
                    author = article.get("author")
                    
                    if not author:
                        author = "unknown"

                    news_article = (
                        article.get("url"),
                        article.get("title"),
                        author,
                        article.get("content"),
                        article.get("urlToImage"),
                        article.get("description"),
                        article.get("publishedAt"),
                        article.get("source").get("name"),
                    )
                    news_articles.append(news_article)

                write_query = """INSERT INTO usa.article
                (url, title, author, content, image, description, published_at, source)
                VALUES %s 
                ON CONFLICT DO NOTHING"""

                with conn.cursor() as cur2:
                    execute_values(cur2, write_query, news_articles)

if __name__ == "__main__":
    categories = ["top", "sports", "health", "business", "entertainment"]
    for cat in categories:
        main(cat)
