from flask import Blueprint, request, jsonify, session
from src.repositories import survey_repository as repo
from src.services import survey_service as svc
from pymysql.err import IntegrityError
bp=Blueprint('survey',__name__,url_prefix='/api')
@bp.before_request
def require_login():
    if not session.get("username"):
        return jsonify(error="Vui lòng đăng nhập"), 401
@bp.get("/feedback")
def list_feedback():
    return jsonify(repo.list_feedback())


@bp.get("/feedback/<int:fid>")
def get_feedback(fid):
    feedback = repo.get_feedback(fid)

    if not feedback:
        return jsonify(error="Không tìm thấy phản hồi"), 404

    return jsonify(feedback), 200


@bp.put("/feedback/<int:fid>")
def update_feedback(fid):
    data = request.get_json(silent=True)
    updated = svc.update_feedback(fid, data)

    return jsonify(updated=bool(updated)), 200


@bp.delete("/feedback/<int:fid>")
def delete_feedback(fid):
    svc.delete_feedback(fid)
    return jsonify(deleted=True), 200

@bp.get('/surveys')
def list_surveys(): return jsonify(repo.list_surveys())

@bp.get('/surveys/<int:sid>')
def get_survey(sid):
    obj=repo.get_survey(sid)
    return (jsonify(obj),200) if obj else (jsonify(error='Không tìm thấy'),404)

@bp.post('/surveys')
def create_survey(): return jsonify(id=svc.create(request.get_json(silent=True))),201

@bp.put('/surveys/<int:sid>')
def update_survey(sid):
    n=svc.update(sid,request.get_json(silent=True) or {})
    return (jsonify(updated=True),200) if n else (jsonify(error='Không tìm thấy'),404)

@bp.delete('/surveys/<int:sid>')
def delete_survey(sid):
    n=repo.delete_survey(sid)
    return (jsonify(deleted=True),200) if n else (jsonify(error='Không tìm thấy'),404)


@bp.post("/surveys/<int:sid>/feedback")
def feedback(sid):
    data = request.get_json(silent=True)
    feedback_id = svc.respond(sid, data)
    return jsonify(id=feedback_id), 201


@bp.errorhandler(ValueError)
@bp.errorhandler(KeyError)
@bp.errorhandler(TypeError)
def bad_input(e): return jsonify(error=str(e)),400

@bp.errorhandler(LookupError)
def not_found(e): return jsonify(error=str(e)),404

@bp.errorhandler(IntegrityError)
def integrity(e): return jsonify(error='Dữ liệu tham chiếu không hợp lệ hoặc bị trùng'),409
