from fastapi import HTTPException, status

from app.models.bank_schemas import AutorizacionRequest, AutorizacionResponse
from app.repositories.card_repo import CardRepository
from app.services.bank_service import BankService


async def autorizar(datos: AutorizacionRequest) -> AutorizacionResponse:
    try:
        repo = CardRepository()
        service = BankService(repo)
        return await service.procesar_autorizacion(datos)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error critico procesando autorizacion",
        ) from exc
