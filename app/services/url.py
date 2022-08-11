import secrets

from sqlalchemy.orm import Session

import app.models.url as urlModels
import app.param_serializers.create_url as param_serializers


def save_to_db(
    url: param_serializers.URLSerializer, db: Session
) -> urlModels.URL:
    '''
    Creates entry for url in db and returns model for saved info
    '''
    key = secrets.token_urlsafe(10)
    secret_key = secrets.token_hex(16)
    db_url = urlModels.URL(
        target_url=url.target_url, key=key, secret_key=secret_key
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    db_url.url = key
    db_url.admin_url = secret_key
    return db_url


def update_url_clicks(db_url: urlModels.URL, db: Session) -> urlModels.URL:
    '''
    Updates DB to add one more click to url
    '''
    db_url.clicks += 1
    db.commit()
    db.refresh(db_url)
    print(db_url.clicks)
    return db_url
