import sqlite3

from data.config import PATH_DATABASE
from utils.const_functions import get_unix, get_date

# Converting taken list to a dictionary
def dict_convert(cursor, row):
    save_dict ={}
    for idx,col in enumerate(cursor.description):
        save_dict[col[0]] = row[idx]

    return save_dict

####################################################################################################
##################################### Request formatting #######################################

# Formatting request without arguments
def update_format(sql, parameters: dict):
    values = ", ".join([
        f"{item} = ?" for item in parameters
    ])
    sql += f" {values}"
    return sql, list(parameters.values())

# Formatting request with arguments
def update_format_where(sql, parameters: dict):
    sql += " WHERE "

    sql += " AND ".join([
        f"{item} = ?" for item in parameters
    ])

    return sql, list(parameters.values())

########################################### REQUESTS TO DATABASE ###########################################

# Add user
def add_userx(user_id, user_login):
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_convert
        con.execute("INSERT INTO storage_users "
                    "(user_id, user_login, user_name, user_lastname, user_date, user_unix) "
                    "VALUES (?, ?, ?, ?, ?, ?)",
                    [user_id, user_login, 0, 0, get_date(), get_unix()])


# Get user
def get_userx(**kwargs):
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_convert
        sql = "SELECT * FROM storage_users"
        sql, parameters = update_format_where(sql, kwargs)
        return con.execute(sql, parameters).fetchone()


# Add First name
def add_user_name(user_id, user_name, **kwargs):
    print(user_id)
    print(user_name)
    with sqlite3.connect(PATH_DATABASE) as con:
        con.execute(f"UPDATE storage_users SET user_name = ? WHERE user_id = ?", (user_name, user_id))


# Add Last name
def add_user_lastname(user_id, user_lastname, **kwargs):
    print(user_id)
    print(user_lastname)
    with sqlite3.connect(PATH_DATABASE) as con:
        con.execute(f"UPDATE storage_users SET user_lastname = ? WHERE user_id = ?", (user_lastname, user_id))

def add_user_login(user_id, user_login, **kwargs):
    print(user_id)
    print(user_login)
    with sqlite3.connect(PATH_DATABASE) as con:
        con.execute(f"UPDATE storage_users SET user_login = ? WHERE user_id = ?", (user_login, user_id))


# Creating all database pages
def create_dbx():
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_convert

        # Creating DB that storages users info
        if len(con.execute("PRAGMA table_info(storage_users)").fetchall()) == 7:
            print("DB was found")
        else:
            con.execute("CREATE TABLE storage_users("
                        "increment INTEGER PRIMARY KEY AUTOINCREMENT,"
                        "user_id INTEGER,"
                        "user_login TEXT,"
                        "user_name TEXT,"
                        "user_lastname TEXT,"
                        "user_date TIMESTAMP,"
                        "user_unix INTEGER"
                        ")")
            print("DB was not found | Creating...")
