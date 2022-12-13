
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5965300871:AAFAYEp935IRFdnvBtu0A-h9fQ0vo_29VKo")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", 13323016))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "68e791e616100248b0a53ae86a661a12")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQC0YCEwGJETIwjc_Zx9HdbK1GNYDr07i3SSk11KYhMjcr8KmLwQnslkZOy9Am50QU4R7VO0IDcaiIesZOD53GuJ6It66i70WPZuX9zIdVwxAttro2nlGdlu8ZJD9F0wBbrObdgzUbwFqawW-fPpEOPQvfxnY2zSmE-yCeuKfEkV2GNE-al3f4hYqpfA5plfDrw2RyCPwYzZoxaJtHkUNWoVG3-djM95lqnyZ8zy8K2OeCo4-AW4zSn2sh5H2uj9Z3zGE6UqWUnANgMBzH78YXvyCVkrXJiw8pIfL9HMU1qLUb9iFYO6nyx5B6g9Q77Wt17TIF-BsFEUZP-CIufruHBgWH5FTAA")

# Database URL from https://cloud.mongodb.com/
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://test:test@cluster0.krokuyo.mongodb.net/?retryWrites=true&w=majority")

# Your database name from mongoDB
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

# ID of users that can use the bot commands
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1484670284").split())

# Should bot search for document files in channels
DOC_SEARCH = os.environ.get("DOC_SEARCH", "yes").lower()

# Should bot search for video files in channels
VID_SEARCH = os.environ.get("VID_SEARCH", "no").lower()

# Should bot search for music files in channels
MUSIC_SEARCH = os.environ.get("MUSIC_SEARCH", "no").lower()




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
