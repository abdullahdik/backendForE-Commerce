from flask import Blueprint

from blueprints.GenelBP import genel_bp
from veri import MagazaModel, MusteriModel,SiparisModel, SiparisUrunuModel, UrunKategorisiModel, UrunlerModel, UrunOzellikleriModel, UrunYorumuModel

v1_bp = Blueprint('v1_bp', __name__)

v1_bp.register_blueprint(genel_bp(MagazaModel, 'magaza_bp'), url_prefix='/magaza')
v1_bp.register_blueprint(genel_bp(MusteriModel, 'musteri_bp'), url_prefix='/musteri')
v1_bp.register_blueprint(genel_bp(SiparisModel, 'siparis_bp'), url_prefix='/siparis')
v1_bp.register_blueprint(genel_bp(SiparisUrunuModel, 'sipari_surunu_bp'), url_prefix='/siparis_urunu')
v1_bp.register_blueprint(genel_bp(UrunKategorisiModel, 'urun_kategorisi_bp'), url_prefix='/urun_kategorisi')
v1_bp.register_blueprint(genel_bp(UrunlerModel, 'urunler_bp'), url_prefix='/urunler')
v1_bp.register_blueprint(genel_bp(UrunOzellikleriModel, 'urun_ozellikleri_bp'), url_prefix='/urun_ozellikleri')
v1_bp.register_blueprint(genel_bp(UrunYorumuModel, 'urun_yorumu_bp'), url_prefix='/urun_yorumu')


api_bp = Blueprint('api_bp', __name__)
api_bp.register_blueprint(v1_bp, url_prefix='/v1')

