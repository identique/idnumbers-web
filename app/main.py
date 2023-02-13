import json
import logging
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, ValidationError
from fastapi.responses import JSONResponse

from .routers.national_id import router

app = FastAPI()
app.include_router(router)

logger = logging.getLogger('uvicorn.error')


@app.exception_handler(RequestValidationError)
@app.exception_handler(ValidationError)
async def validation_exception_handler(_, exception):
    exc_json = json.loads(exception.json())
    response = {"message": []}
    for error in exc_json:
        response['message'].append(error['loc'][-1] + f": {error['msg']}")
    logger.warning(json.dumps(response['message']))
    return JSONResponse(status_code=422, content=response)
