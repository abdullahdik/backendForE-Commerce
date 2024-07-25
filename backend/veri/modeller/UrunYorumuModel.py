from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from veri.modeller.TemelVeriModeli import TemelVeriModeli

class UrunYorumuModel(TemelVeriModeli):
    __tablename__ = "urun_yorumu"

    siparis_id : Mapped[int] = mapped_column(ForeignKey('siparis.id'))
    urunler_id : Mapped[int] = mapped_column(ForeignKey('urunler.id'))
    urun_yorumu : Mapped[str] = mapped_column(nullable = False)
    urun_puani : Mapped[int] = mapped_column(nullable = False)