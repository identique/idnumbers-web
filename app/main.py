import json
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, ValidationError
from fastapi.responses import JSONResponse

from .routers.national_id.USA import router as usa_router

app = FastAPI()

app.include_router(usa_router)


@app.exception_handler(RequestValidationError)
@app.exception_handler(ValidationError)
async def validation_exception_handler(_, exception):
    exc_json = json.loads(exception.json())
    response = {"message": []}
    for error in exc_json:
        response['message'].append(error['loc'][-1] + f": {error['msg']}")
    return JSONResponse(status_code=422, content=response)
