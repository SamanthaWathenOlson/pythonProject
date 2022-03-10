from psycopg import OperationalError, connect


def create_connection:
    conn = connect(
        host="", #os.environ.get("HOST") (example)
        # create environment variables through Pycharm, so real data is not obvious
        dbname="", #same as above ("DBNAME")
        user="", #same as above ("USER")
        password="", #same as above ("PASSWORD")
        port="" #same as above ("PORT")
        )

    except OperationalError as e:
       print(e)

    connection = create_connection()

    print(connection)

