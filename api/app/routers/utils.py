import logging
from datetime import datetime

# -------------------------------
# 1. Logging Setup
# -------------------------------
logger = logging.getLogger("ai_saas")
logger.setLevel(logging.INFO)

# Console handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)

def log_info(message: str):
    logger.info(message)

def log_error(message: str):
    logger.error(message)


# -------------------------------
# 2. Prompt Utilities (AI)
# -------------------------------
def format_chat_prompt(user_message: str, history: list = None) -> str:
    """
    Prepares a prompt for the AI model.
    
    Args:
        user_message: Latest message from user
        history: List of previous messages [{"role": "user/AI", "content": str}]
        
    Returns:
        Combined prompt string
    """
    prompt = ""
    if history:
        for msg in history:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            prompt += f"{role}: {content}\n"
    prompt += f"user: {user_message}\nAI: "
    return prompt


# -------------------------------
# 3. Timestamp / Formatting
# -------------------------------
def current_timestamp() -> str:
    """Return current UTC timestamp string"""
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")


# -------------------------------
# 4. Misc Helpers
# -------------------------------
def truncate_text(text: str, max_len: int = 200) -> str:
    """Truncate text for logs or preview"""
    return text if len(text) <= max_len else text[:max_len] + "..."