from os import getenv


# Database Connection is handled when running the bot, see run_bot.py and botclient.py
def get_db_credentials():
    v =  {
        'DB_USER' : getenv('POSTGRE_USER'),
        'DB_PASS' : getenv('POSTGRE_PASSWORD'),
        'DB_HOST' : getenv('POSTGRE_HOSTNAME'),
        'DB_PORT' : getenv('POSTGRE_PORT'),
        'DB_NAME' : getenv('POSTGRE_DATABASE_NAME')
    }
    print(v)
    return v