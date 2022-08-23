import validators

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse

from . import crud, models, schemas
from .database import SessionLocal, engine
from .config import get_settings
from sqlalchemy.orm import Session
from starlette.datastructures import URL

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def url_error(request):
    message = f"URL '{request.url}' erronea"
    raise HTTPException(status_code=404, detail=message)

def error_400(message):
    raise HTTPException(status_code=400, detail=message)


@app.get("/")
def bienvenido():
    return "Bienvenido al api"

@app.post("/url", response_model=schemas.URLInfo)
def url_Crea(url: schemas.URLBase, db: Session = Depends(get_db)):
    if not validators.url(url.target_url):
        raise_bad_request(message="Your provided URL is not valid")

    db_url = crud.create_db_url(db=db, url=url)
    return info(db_url)


@app.get("/{url_key}")
def regresa_url(
    url_key: str, request: Request, db: Session = Depends(get_db)
):
    if db_url := crud.get_db_url_by_key(db=db, url_key=url_key):
        crud.update_db_clicks(db=db, db_url=db_url)
        return RedirectResponse(db_url.target_url)
    else:
        url_error(request)


@app.get(
    "/admin/{secret_key}",
    name="administration info",
    response_model=schemas.URLInfo,
)
def get_url_info(
    secret_key: str, request: Request, db: Session = Depends(get_db)
):
    if db_url := crud.get_db_url_by_secret_key(db, secret_key=secret_key):
        return info(db_url)
    else:
        url_error(request)

