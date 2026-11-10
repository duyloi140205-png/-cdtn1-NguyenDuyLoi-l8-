import os
import re
from pathlib import Path

import pymysql
from dotenv import load_dotenv

load_dotenv()

TEST_DB = "csat_nps_buoi14_test"

sql = Path("migrations/001_init.sql").read_text(
    encoding="utf-8-sig"
)

# Chỉ kiểm thử trong database tạm, không dùng csat_nps.
sql = re.sub(
    r"CREATE DATABASE IF NOT EXISTS csat_nps\b",
    f"CREATE DATABASE IF NOT EXISTS {TEST_DB}",
    sql,
    flags=re.IGNORECASE,
)

sql = re.sub(
    r"\bUSE csat_nps\s*;",
    f"USE {TEST_DB};",
    sql,
    flags=re.IGNORECASE,
)

db = pymysql.connect(
    host=os.getenv("DB_HOST", "127.0.0.1"),
    port=int(os.getenv("DB_PORT", "3306")),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASSWORD", ""),
    autocommit=True,
)

try:
    with db.cursor() as cur:
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {TEST_DB}")

        cur.execute(f"USE {TEST_DB}")

        for statement in sql.split(";"):
            statement = statement.strip()
            if statement:
                cur.execute(statement)

        cur.execute("SHOW TABLES")
        tables = cur.fetchall()

        print("MIGRATION PASS")
        print("So bang:", len(tables))
        print("Danh sach bang:", tables)

except Exception as exc:
    print("MIGRATION FAIL")
    print(type(exc).__name__, str(exc))
    raise

finally:
    db.close()