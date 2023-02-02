from pydantic import BaseModel, validator


class ValidationResponse(BaseModel):
    is_valid: bool


class ValidationRequestPayload(BaseModel):
    id_number: str

    @validator('id_number')
    def id_number_validation(cls, id_number):
        if not id_number:
            raise ValueError("Invalid id number")
        return id_number
