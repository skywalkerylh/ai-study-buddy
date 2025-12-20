from langchain_google_genai import ChatGoogleGenerativeAI
from src.config.settings import settings


def get_llm():
    # 2. 改用 Google 的類別
    return ChatGoogleGenerativeAI(
        google_api_key=settings.GOOGLE_API_KEY,  
        model=settings.MODEL_NAME,  
        temperature=settings.TEMPERATURE,
        convert_system_message_to_human=True
    )
