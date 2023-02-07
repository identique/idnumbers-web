import importlib
from fastapi import APIRouter
from app.models import ValidationRequestPayload, ValidationResponse

router = APIRouter(prefix='/national_id', tags=['national_id'])


@router.post("/validate")
async def test(payload: ValidationRequestPayload):
    module = importlib.import_module(f'idnumbers.nationalid.{payload.country}')
    is_valid = module.NationalID.validate(payload.id_number)
    return ValidationResponse(is_valid=is_valid)
