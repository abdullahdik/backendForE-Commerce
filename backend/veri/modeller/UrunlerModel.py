from sqlalchemy.orm import Mapped, mapped_column

from veri.modeller.TemelVeriModeli import TemelVeriModeli

class UrunlerModel(TemelVeriModeli):
    __tablename__ = 'urunler'


    urun_adi : Mapped[str] = mapped_column(nullable=False)
    urun_kodu : Mapped[str] = mapped_column(nullable=False)
    urun_fiyati : Mapped[float] = mapped_column(nullable=False)
    urun_aciklamasi : Mapped[str] = mapped_column(nullable=False)