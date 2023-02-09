import importlib
from fastapi import APIRouter
from app.models import ValidationRequestPayload, ValidationResponse, ParseRequestPayload

router = APIRouter(prefix='/national_id', tags=['national_id'])


@router.post("/validate")
async def validate(payload: ValidationRequestPayload):
    module = importlib.import_module(f'idnumbers.nationalid.{payload.country}')
    is_valid = module.NationalID.validate(payload.id_number)
    return ValidationResponse(is_valid=is_valid)


@router.post("/parse")
async def parse(payload: ParseRequestPayload):
    module = importlib.import_module(f'idnumbers.nationalid.{payload.country}')
    parse_result = module.NationalID.parse(payload.id_number)
    return parse_result
