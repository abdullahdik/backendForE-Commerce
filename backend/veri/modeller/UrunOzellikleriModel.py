from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from veri.modeller.TemelVeriModeli import TemelVeriModeli

class UrunOzellikleriModel(TemelVeriModeli):
    __tablename__ = 'urun_ozellikleri'

    urunler_id: Mapped[int] = mapped_column(ForeignKey('urunler.id'))
    urun_ozelligi : Mapped[str] = mapped_column(nullable=False)
    urun_degeri : Mapped[str] = mapped_column(nullable=False)