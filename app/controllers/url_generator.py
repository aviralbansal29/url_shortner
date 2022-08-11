import validators

from fastapi import Depends, HTTPException, APIRouter, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

import app.models.url as urlModels
import app.param_serializers.create_url as param_serializers
import app.response_serializers.create_url as response_serializers
import app.services.url as url_services
import configs.database as databaseConfig


router = APIRouter()


def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)


@router.post('/url', response_model=response_serializers.URLInfo)
def create_url(
    url: param_serializers.URLSerializer,
    db: Session = Depends(databaseConfig.get_db)
):
    if not validators.url(url.target_url):
        raise_bad_request(message='Your provided URL is not valid')

    db_url = url_services.save_to_db(url, db)

    return db_url


def raise_not_found(request):
    message = f"URL '{request.url}' doesn't exist"
    raise HTTPException(status_code=404, detail=message)


@router.get("/{url_key}")
def forward_to_target_url(
    url_key: str,
    request: Request,
    db: Session = Depends(databaseConfig.get_db)
):
    db_url = (
        db.query(urlModels.URL)
        .filter(urlModels.URL.key == url_key, urlModels.URL.is_active)
        .first()
    )
    if db_url:
        url_services.update_url_clicks(db_url, db)
        return RedirectResponse(db_url.target_url)
    else:
        raise_not_found(request)
