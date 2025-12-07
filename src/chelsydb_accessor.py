import os
from typing import Optional, Tuple

import psycopg


def get_conn():
    """Create a new connection to chelsydb using environment variables with sensible defaults."""
    return psycopg.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "chelsydb"),
        user=os.getenv("DB_USER", "testuser"),
        password=os.getenv("DB_PASSWORD", "testpass"),
    )


def insert_data(data: str) -> int:
    """Insert a row into testtbl1 and return the new id."""
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO testtbl1 (data) VALUES (%s) RETURNING id", (data,))
        new_id = cur.fetchone()[0]
    return new_id


def fetch_data(row_id: int) -> Optional[Tuple[int, str]]:
    """Fetch a row by id from testtbl1."""
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT id, data FROM testtbl1 WHERE id = %s", (row_id,))
        row = cur.fetchone()
    return row
