import os
import dotenv


dotenv.load_dotenv(dotenv.find_dotenv())


SQLITE_DB_FILEPATH = 'tech_interview_bot/tech_interviewer.db'
BOT_TOKEN = os.environ.get('TECH_INTERVIEW_BOT_TOKEN', '')
