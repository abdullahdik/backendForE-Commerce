from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from veri.modeller.TemelVeriModeli import TemelVeriModeli


class SiparisUrunuModel(TemelVeriModeli):
    __tablename__ = "siparis_urunu"

    siparis_id : Mapped[int] = mapped_column(ForeignKey(("siparis.id")))
    urunler_id : Mapped[int] = mapped_column(ForeignKey(("urunler.id")))
    adeti : Mapped[int] = mapped_column(nullable=False)
    birim_fiyat : Mapped[float] = mapped_column(nullable=False)