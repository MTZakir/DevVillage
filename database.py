import sqlite3

def init_db():
    try:
        with sqlite3.connect('chat_history.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS chat_messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    message TEXT
                )
            ''')
    except sqlite3.Error as e:
        print("Error initializing database:", e)

# Function to add a message to the chat history
def add_chat_message(user_id, message):
    try:
        with sqlite3.connect('chat_history.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO chat_messages (user_id, message) VALUES (?, ?)
            ''', (user_id, message))
    except sqlite3.Error as e:
        print("Error adding message to chat history:", e)

# Function to get all chat history with user information
def get_chat_history():
    try:
        with sqlite3.connect('chat_history.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT user_id, message FROM chat_messages
            ''')
            chat_history = cursor.fetchall()
        return chat_history
    except sqlite3.Error as e:
        print("Error fetching chat history:", e)
