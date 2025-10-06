class Config(object):
    LOGGER = True
    API_ID = 21189715
    API_HASH = "988a9111105fd2f0c5e21c2c2449edfd"
    TOKEN = "7026867682:AAGjBzbfNklXEdh5usx-ykQ8odIY2Q3uEoQ"
    OWNER_ID = 8111174619
    SUPPORT_CHAT = "-1001956979385"
    START_IMG = "https://telegra.ph/file/faf065e6f231437ddb0c7.jpg"
    EVENT_LOGS = ()
    MONGO_DB_URI = "mongodb+srv://ayanosuvii0925:subhichiku123@cluster0.uw8yxkl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    DATABASE_URL = "postgres://u3uqmshuo2n4p6:pd8c4daad5981de80149dee5684fba8327b53ce61df435f3738ddba7e0a057183@cdf8md3um0j5m6.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d8d5mnrc9uhovu"
    CASH_API_KEY = ""
    TIME_API_KEY = ""
    SESSION_STRING = "BQGuP2cAT2fs4tRg0YldAcZFjRyjwFjGeh9_lwVKyrnnS1evc7Btnh_-neg_WpOjS6Mc7oWQD6rdhcq0CsIT-MzBDxLo4qsLym4DD5wHCm-hEqHtzxeD2TovMlSA1JTfWRZ65BT1vzn5zfncDgu6KnCwlxpq7Dv67cWkth8ENlzr92rs-_DibbaBFeZga6PkuPciy-ZwOIqVlNT3A21d25O1jN-EVP6Q19y4sNcm7j7VXM2kzSIYOI0SZPVt4LaeGPFwKFEobZbbuBuRxprX96kqCtXIROeRpkIP457haMfpo-WK3jTuQtxcyDV0SOCABzh8Db_jR6kYq3iXG4D1LYP2wWtgDwAAAAFGEz7IAA"  
    
    BL_CHATS = []
    DRAGONS = []
    DEV_USERS = []
    DEMONS = []
    TIGERS = []
    WOLVES = []

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
