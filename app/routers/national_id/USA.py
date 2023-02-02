from fastapi import APIRouter
from app.models import ValidationRequestPayload, ValidationResponse

from idnumbers.nationalid import USA

router = APIRouter(prefix='/national_id/USA', tags=['USA'])


@router.post("/validate", tags=['validate'], response_model=ValidationResponse)
async def validate(payload: ValidationRequestPayload):
    is_valid = USA.SocialSecurityNumber.validate(payload.id_number)
    return ValidationResponse(is_valid=is_valid)
