from datetime import datetime

from sqlalchemy import inspect
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped



class TemelVeriModeli(DeclarativeBase):


    id : Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    olusturulma_tarihi: Mapped[datetime] = mapped_column(default=datetime.now())
    guncelleme_tarihi: Mapped[datetime] = mapped_column(default=datetime.now(), onupdate=datetime.now())


    def to_dict(self):
        sonuc = { column.key: getattr(self, column.key)
                  for column in inspect(self).mapper.column_attrs }

        return sonuc