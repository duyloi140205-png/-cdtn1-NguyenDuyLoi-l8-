from datetime import date
from src.repositories import survey_repository as repo

def create(data):
    if not isinstance(data,dict): raise ValueError('JSON không hợp lệ')
    ticket_id=int(data['ticket_id'])
    expire=date.fromisoformat(data['expire_date'])
    if expire<date.today(): raise ValueError('Ngày hết hạn phải từ hôm nay trở đi')
    return repo.create_survey({'ticket_id':ticket_id,'expire_date':expire})

def update(survey_id,data):
    expire=date.fromisoformat(data['expire_date'])
    if expire<date.today(): raise ValueError('Ngày hết hạn không hợp lệ')
    return repo.update_survey(survey_id,expire)

def respond(survey_id,data):
    survey=repo.get_survey(survey_id)
    if not survey: raise LookupError('Không tìm thấy khảo sát')
    if survey['ExpireDate'] < date.today(): raise ValueError('Khảo sát đã hết hạn')
    if not isinstance(data,dict): raise ValueError('JSON không hợp lệ')
    csat=data.get('csat_score'); nps=data.get('nps_score')
    if type(csat)!=int or not 1<=csat<=5: raise ValueError('CSAT phải là số nguyên 1-5')
    if type(nps)!=int or not 0<=nps<=10: raise ValueError('NPS phải là số nguyên 0-10')
    comment=data.get('comment','')
    if not isinstance(comment,str) or len(comment)>2000: raise ValueError('Nhận xét không hợp lệ')
    return repo.create_feedback(survey_id,csat,nps,comment)
