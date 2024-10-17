import psycopg2


def get_connection():
    name = 'postgres'
    password = 'password'
    url = f"postgresql://{name}:{password}@localhost"
    return psycopg2.connect(url)


def query_execute(query: str):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
        conn.commit()


def define_status_type():
    query = """
    CREATE TYPE
        STATUS
    AS ENUM
        ('todo', 'doing', 'done');
    """
    query_execute(query=query)
    print("define status type: Done")


def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS tasks (
        id UUID PRIMARY KEY,
        title varchar(128) NOT NULL,
        content TEXT,
        status INT,
        created_at TIMESTAMP NOT NULL,
        updated_at TIMESTAMP NOT NULL
    )
    """

    query_execute(query=query)
    print("create table: Done")


def main():
    # define_status_type()
    create_table()


if __name__ == "__main__":
    main()
