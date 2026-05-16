from fastapi import APIRouter

from app.controllers.auth_controller import autorizar
from app.models.bank_schemas import AutorizacionRequest, AutorizacionResponse

router = APIRouter()


@router.post("/autorizar", response_model=AutorizacionResponse)
async def autorizar_tarjeta(datos: AutorizacionRequest) -> AutorizacionResponse:
    return await autorizar(datos)
