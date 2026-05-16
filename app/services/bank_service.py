import uuid

from app.models.bank_schemas import AutorizacionRequest, AutorizacionResponse
from app.repositories.card_repo import CardRepository


class BankService:
    def __init__(self, card_repo: CardRepository) -> None:
        self._card_repo = card_repo

    async def procesar_autorizacion(
        self, datos: AutorizacionRequest
    ) -> AutorizacionResponse:
        if not datos.numero_tarjeta.startswith("5"):
            return AutorizacionResponse(
                status="rechazado",
                mensaje="Numero de tarjeta invalido para Mastercard",
                codigo_autorizacion=None,
            )

        tarjeta = await self._card_repo.obtener_tarjeta_por_numero(datos.numero_tarjeta)
        if tarjeta is None:
            return AutorizacionResponse(
                status="rechazado",
                mensaje="Tarjeta no encontrada",
                codigo_autorizacion=None,
            )

        if datos.monto > tarjeta.saldo:
            return AutorizacionResponse(
                status="rechazado",
                mensaje="Fondos insuficientes",
                codigo_autorizacion=None,
            )

        nuevo_saldo = tarjeta.saldo - datos.monto
        await self._card_repo.actualizar_saldo(tarjeta.id, nuevo_saldo)

        return AutorizacionResponse(
            status="aprobado",
            mensaje="Autorizacion aprobada",
            codigo_autorizacion=str(uuid.uuid4()),
        )
