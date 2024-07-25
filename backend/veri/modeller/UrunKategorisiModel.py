from sqlalchemy.orm import Mapped, mapped_column

from veri.modeller.TemelVeriModeli import TemelVeriModeli


class UrunKategorisiModel(TemelVeriModeli):
    __tablename__ = 'urun_kategorisi'


    kategori_adi: Mapped[str] = mapped_column(nullable=False)