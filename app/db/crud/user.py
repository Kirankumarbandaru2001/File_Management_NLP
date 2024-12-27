from app.db.models.user import User
from app.db.connection import get_db_connection

def create_user(user: User):
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO users (username, email, hashed_password, created_at)
                VALUES (%s, %s, %s, %s)
                RETURNING id;
                """,
                (user.username, user.email, user.hashed_password, user.created_at),
            )
            user_id = cursor.fetchone()[0]
            conn.commit()
            return user_id

def get_user_by_username(username: str) -> User:
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE username = %s;", (username,))
            row = cursor.fetchone()
            if row:
                return User(
                    id=row[0],
                    username=row[1],
                    email=row[2],
                    hashed_password=row[3],
                    created_at=row[4],
                )
            return None
