from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field


class AutorizacionRequest(BaseModel):
    numero_tarjeta: str = Field(..., min_length=1)
    cvc: str = Field(..., min_length=1)
    fecha_expiracion: str = Field(..., min_length=1)
    monto: float = Field(..., gt=0)


class AutorizacionResponse(BaseModel):
    status: Literal["aprobado", "rechazado"]
    mensaje: str = Field(..., min_length=1)
    codigo_autorizacion: Optional[str] = None


class ClienteBancarioPB(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: str = Field(..., min_length=1)
    numero_tarjeta: str = Field(..., min_length=1)
    cvc: str = Field(..., min_length=1)
    franquicia: Literal["Visa", "Mastercard"]
    saldo: float
