from sqlalchemy.orm import mapped_column, Mapped

from veri.modeller.TemelVeriModeli import TemelVeriModeli



class MusteriModel(TemelVeriModeli):
    __tablename__ = "musteri"

    musteri_adi : Mapped[str] = mapped_column(nullable=False)
    musteri_soyadi : Mapped[str] = mapped_column(nullable=False)
    musteri_cinsiyeti : Mapped[str] = mapped_column(nullable=False)