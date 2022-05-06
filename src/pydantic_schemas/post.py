from pydantic import BaseModel, validator, Field

class Post(BaseModel):
    '''
    If the variable is privat, then name: str = Field(alias="_name")
    '''
    id: int #= Field(le=2)
    abbreviation: str
    city: str
    conference: str
    division: str
    full_name: str
    name: str

    # @validator('id')
    # def check_that_id_is_less_that_two(cls, v):  # le = 2
    #     if v > 2:
    #         raise ValueError('id is not less that two')
    #     else:
    #         return v


