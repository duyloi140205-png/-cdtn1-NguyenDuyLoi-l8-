from src.repositories.db import connect

def list_surveys():
    with connect() as db:
        with db.cursor() as cur:
            cur.execute("""SELECT s.SurveyID,s.TicketID,s.SentDate,s.ExpireDate,c.FullName,st.StoreName FROM Survey s JOIN WarrantyTicket t ON t.TicketID=s.TicketID JOIN Customer c ON c.CustomerID=t.CustomerID JOIN Store st ON st.StoreID=t.StoreID ORDER BY s.SurveyID""")
            return cur.fetchall()

def get_survey(survey_id):
    with connect() as db:
        with db.cursor() as cur:
            cur.execute('SELECT * FROM Survey WHERE SurveyID=%s',(survey_id,))
            return cur.fetchone()

def create_survey(data):
    with connect() as db:
        with db.cursor() as cur:
            cur.execute('INSERT INTO Survey(TicketID,SentDate,ExpireDate) VALUES (%s,CURDATE(),%s)',(data['ticket_id'],data['expire_date']))
            result=cur.lastrowid
        db.commit()
        return result

def update_survey(survey_id,expire_date):
    with connect() as db:
        with db.cursor() as cur:
            cur.execute('UPDATE Survey SET ExpireDate=%s WHERE SurveyID=%s',(expire_date,survey_id))
            count=cur.rowcount
        db.commit()
        return count

def delete_survey(survey_id):
    with connect() as db:
        with db.cursor() as cur:
            cur.execute('DELETE FROM Survey WHERE SurveyID=%s',(survey_id,))
            count=cur.rowcount
        db.commit()
        return count

def create_feedback(survey_id,csat,nps,comment):
    with connect() as db:
        with db.cursor() as cur:
            cur.execute('INSERT INTO Feedback(SurveyID,CSATScore,NPSScore,Comment,SubmittedDate) VALUES (%s,%s,%s,%s,CURDATE())',(survey_id,csat,nps,comment))
            result=cur.lastrowid
        db.commit()
        return result
