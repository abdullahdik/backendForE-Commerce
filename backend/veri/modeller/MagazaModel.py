from sqlalchemy.orm import Mapped, mapped_column

from veri.modeller.TemelVeriModeli import TemelVeriModeli


class MagazaModel(TemelVeriModeli):
    __tablename__ = 'magaza'

    # magaza_id : Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    magaza_adi : Mapped[str] = mapped_column(nullable=False)
    magaza_adresi : Mapped[str] = mapped_column(nullable=False)
    magaza_tel : Mapped[str] = mapped_column(nullable=False)
    magaza_yetkilikisi : Mapped[str] = mapped_column(nullable=False)


