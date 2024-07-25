from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from veri.modeller.TemelVeriModeli import TemelVeriModeli


class SiparisModel(TemelVeriModeli):
    __tablename__ = "siparis"

    urunler_id : Mapped[int] = mapped_column(ForeignKey('urunler.id'))
    siparis_tarihi : Mapped[date] = mapped_column(default=date.today())
    firma : Mapped[int] = mapped_column(nullable= False)
    musteri_id : Mapped[int] = mapped_column(ForeignKey('musteri.id'))