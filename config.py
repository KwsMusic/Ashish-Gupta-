from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID")6277238293)

PING_IMG = getenv("PING_IMG", "")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/b510693c25a82b8288b9a.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Dost_support")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Zidd_Bot")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6277238293").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
