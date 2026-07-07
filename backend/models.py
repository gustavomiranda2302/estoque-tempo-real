from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import Column, Enum, Integer, String, DateTime
from sqlalchemy.sql import func
import enum
from database import Base


class PeriodoEnum(str, enum.Enum):
    primeiro_tempo = "primeiro_tempo"
    intervalo = "intervalo"
    segundo_tempo = "segundo_tempo"
    encerrado = "encerrado"


class Partida(Base):
    __tablename__ = "partidas"

    id = Column(Integer, primary_key=True, index=True)
    time_a = Column(String, nullable=False)
    time_b = Column(String, nullable=False)
    placar_time_a = Column(Integer, nullable=False, default=0)
    placar_time_b = Column(Integer, nullable=False, default=0)
    tempo = Column(
        Enum(PeriodoEnum), nullable=False, default=PeriodoEnum.primeiro_tempo
    )
    atualizacao = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )


class PartidaBase(BaseModel):
    time_a: str = Field(..., min_length=1)
    time_b: str = Field(..., min_length=1)


class PartidaCreate(PartidaBase):
    pass


class PartidaRead(PartidaBase):
    id: int
    placar_time_a: int
    placar_time_b: int
    tempo: PeriodoEnum
    atualizacao: datetime
    model_config = ConfigDict(from_attributes=True)
