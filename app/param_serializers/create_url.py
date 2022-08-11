from pydantic import BaseModel


class URLSerializer(BaseModel):
    target_url: str
