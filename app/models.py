import importlib
from pydantic import BaseModel, validator


class ValidationResponse(BaseModel):
    is_valid: bool


class ValidationRequestPayload(BaseModel):
    country: str
    id_number: str

    @validator('country')
    def country_validation(cls, country):
        try:
            importlib.import_module(f'idnumbers.nationalid.{country}')
        except ModuleNotFoundError:
            raise ValueError(f"The country {country} is not support now.")
        return country

    @validator('id_number')
    def id_number_validation(cls, id_number):
        if not id_number:
            raise ValueError("Invalid id number")
        return id_number


class ParseRequestPayload(BaseModel):
    country: str
    id_number: str

    @validator('country')
    def country_validation(cls, country):
        try:
            module = importlib.import_module(f'idnumbers.nationalid.{country}')
        except ModuleNotFoundError:
            raise ValueError(f"The country {country} is not support now.")
        if not module.NationalID.METADATA.parsable:
            raise ValueError(f"ID for this country {country} is not parsable")
        return country

    @validator('id_number')
    def id_number_validation(cls, id_number):
        if not id_number:
            raise ValueError("Invalid id number")
        return id_number
