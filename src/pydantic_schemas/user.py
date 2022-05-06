from pydantic import BaseModel, validator
from src.enums.user_enums import Gender, Statuses, UserErrors


class User(BaseModel):
    id: int = None  # if not required
    name: str
    email: str
    gender: Gender
    status: Statuses

    @validator('email')
    def check_that_dog_presented_in_email(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.values)
