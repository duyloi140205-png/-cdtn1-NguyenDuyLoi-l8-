
import os
from datetime import date, timedelta

import pymysql
from dotenv import load_dotenv

load_dotenv()

TEST_DB = "csat_nps_buoi14_test"

# Chỉ kết nối tới database thử nghiệm.
db = pymysql.connect(
    host=os.getenv("DB_HOST", "127.0.0.1"),
    port=int(os.getenv("DB_PORT", "3306")),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASSWORD", ""),
    database=TEST_DB,
    autocommit=False,
)

try:
    with db.cursor() as cur:
        # Tạo dữ liệu thử nghiệm trong một transaction.
        cur.execute(
            "INSERT INTO Customer (FullName) VALUES (%s)",
            ("Khach hang kiem thu Buoi 14",),
        )
        customer_id = cur.lastrowid

        cur.execute(
            "INSERT INTO Store (StoreName) VALUES (%s)",
            ("Cua hang kiem thu Buoi 14",),
        )
        store_id = cur.lastrowid

        cur.execute(
            """
            INSERT INTO WarrantyTicket
                (CustomerID, StoreID, CompletedDate, Status)
            VALUES (%s, %s, %s, %s)
            """,
            (customer_id, store_id, date.today(), "Completed"),
        )
        ticket_id = cur.lastrowid

        # CREATE Survey
        cur.execute(
            """
            INSERT INTO Survey (TicketID, SentDate, ExpireDate)
            VALUES (%s, %s, %s)
            """,
            (ticket_id, date.today(), date.today() + timedelta(days=30)),
        )
        survey_id = cur.lastrowid
        print("CREATE SURVEY PASS:", survey_id)

        # CREATE Feedback
        cur.execute(
            """
            INSERT INTO Feedback
                (SurveyID, CSATScore, NPSScore, Comment, SubmittedDate)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (survey_id, 5, 9, "Kiem thu MySQL", date.today()),
        )
        feedback_id = cur.lastrowid
        print("CREATE FEEDBACK PASS:", feedback_id)

        # READ
        cur.execute(
            "SELECT CSATScore, NPSScore FROM Feedback WHERE FeedbackID=%s",
            (feedback_id,),
        )
        result = cur.fetchone()
        assert result == (5, 9)
        print("READ FEEDBACK PASS")

        # UPDATE
        cur.execute(
            """
            UPDATE Feedback
            SET CSATScore=%s, NPSScore=%s
            WHERE FeedbackID=%s
            """,
            (4, 8, feedback_id),
        )
        assert cur.rowcount == 1
        print("UPDATE FEEDBACK PASS")

        # INVALID DATA
        try:
            cur.execute(
                """
                UPDATE Feedback SET NPSScore=%s
                WHERE FeedbackID=%s
                """,
                (11, feedback_id),
            )
        except pymysql.MySQLError:
            print("INVALID NPS REJECTED PASS")
        else:
            raise AssertionError("MySQL accepted invalid NPS")

        # DELETE
        cur.execute(
            "DELETE FROM Feedback WHERE FeedbackID=%s",
            (feedback_id,),
        )
        assert cur.rowcount == 1
        print("DELETE FEEDBACK PASS")

        cur.execute(
            "DELETE FROM Survey WHERE SurveyID=%s",
            (survey_id,),
        )
        assert cur.rowcount == 1
        print("DELETE SURVEY PASS")

    print("CRUD MYSQL TEST PASS")

finally:
    # Không lưu dữ liệu thử nghiệm.
    db.rollback()
    db.close()
    print("ROLLBACK DONE")
