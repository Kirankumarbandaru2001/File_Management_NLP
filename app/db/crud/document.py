from app.db.models.document import Document
from app.db.connection import get_db

def create_document(document: Document):
    with get_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO documents (title, file_path, file_type, parsed_text, created_at)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id;
                """,
                (document.title, document.file_path, document.file_type, document.parsed_text, document.created_at),
            )
            document_id = cursor.fetchone()[0]
            conn.commit()
            return document_id

def get_document_by_id(doc_id: int) -> Document:
    with get_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM documents WHERE id = %s;", (doc_id,))
            row = cursor.fetchone()
            if row:
                return Document(
                    id=row[0],
                    title=row[1],
                    file_path=row[2],
                    file_type=row[3],
                    parsed_text=row[4],
                    created_at=row[5],
                )
            return None
