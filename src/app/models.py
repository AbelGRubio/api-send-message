from pydantic import BaseModel, EmailStr


class EmailRequest(BaseModel):
    email: EmailStr
    subject: str
    message: str
