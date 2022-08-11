from pydantic import BaseModel


class URLInfo(BaseModel):
    is_active: bool
    clicks: int
    target_url: str
    url: str
    admin_url: str

    class Config:
        orm_mode = True
