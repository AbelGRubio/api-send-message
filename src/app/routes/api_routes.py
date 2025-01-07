from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from ..configuration import __version__
from ..models import EmailRequest
from ..functions import send_message


api_router = APIRouter()


@api_router.get("/health")
def health() -> JSONResponse:
    """
    Check if everything is working
    """
    status_code = 200
    return JSONResponse(
        content={'version': __version__},
        status_code=status_code
    )


@api_router.options("/send-email")
def handle_options():
    return {"status": "OK"}


# Endpoint para enviar correos
@api_router.post("/send-email")
def send_email(email_request: EmailRequest):
    try:
        # Enviar correo
        send_message(email_request)
        return {"message": "Correo enviado con éxito"}
    except Exception as e:
        raise HTTPException(status_code=500,
                            detail=f"Error al enviar el correo: {str(e)}")