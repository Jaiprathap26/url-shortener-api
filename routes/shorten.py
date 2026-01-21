from flask import Blueprint, request, redirect
from flask_restx import Api, Resource, fields  
from models import db, ShortURL
from utils.code_genrator import generate_short_code

shorten_bp = Blueprint("shorten",__name__)
api = Api(shorten_bp, doc="/docs")

url_model = api.model("URL",{
    "url": fields.String(required=True)
})

@api.route("/shorten")
class CreateShortURL(Resource):
    @api.expect(url_model)
    def post(self):
        data = request.get_json()


        if not data or "url" not in data:
            return {"error": "URL is required"}, 400
        

        short_code = generate_short_code()

        new_url = ShortURL(
            original_url = data["url"],
            short_code = short_code
        )

        db.session.add(new_url)
        db.session.commit()

        return {
            "id": new_url.id,
            "url": new_url.original_url,
            "short_code": new_url.short_code,
            "createdAt": new_url.created_at.isoformat(),
            "updateAt": new_url.updated_at.isoformat()
        }, 201
    
@api.route("/shorten/<string:code>")
class GetUpdateDeleteURL(Resource):
    def get(self, code):
        url = ShortURL.query.filter_by(short_code = code).first()
        if not url:
            return {"error": "Not found"}, 404
        
        return {
            "id": url.id,
            "url": url.original_url,
            "short_code": url.short_code,
            "createdAt": url.created_at.isoformat(),
            "updateAt": url.updated_at.isoformat()
        },


@api.expect(url_model)
def put(self, code):
    url = ShortURL.query.filter_by(short_code=code).first()
    if not url:
        return {"error": "Not found"},404
    
    data = request.get_json()
    url.original_url= data["url"]
    db.session.commit()

    return {
        "id": url.id,
        "url":url.original_url,
        "shortcode": url.short_code,
        "updateAt": url.update_at
    }

    def delete(self, code):
        url = ShortURL.query.filter_by(short_code=code).first()
        if not url:
            return{"error": "Not found"},404
        
        db.session.delete(url)
        db.session.commit()
        return "", 204
    
@api.route("/shoerten/<string:code>/stats")
class Stats(Resource):
    def get(self, code):
        url = ShortURL.query.filter_by(short_code=code).first()
        if not url:
            return {"error": "Not found"},404
        

        return{
            "id": url.id,
            "url": url.original_url,
            "shortcode": url.short_code,
            "accessCount": url.access_count
        }
    
@shorten_bp.route("/<string:code>")
def redirect_to_original(code):
    url = ShortURL.query.filter_by(short_code=code).first()
    if not url:
        return{"error":"Not found"}, 404
    
    url.access_count +=1
    db.session.commit()

    return redirect(url.original_url, code=301)