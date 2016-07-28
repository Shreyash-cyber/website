"""
Prefectures ordered to conform with the Japanese entry
of ISO-3166 as this ordering is widely used in Japan.

See:
http://en.wikipedia.org/wiki/ISO_3166-2:JP
"""
from django.utils.translation import ugettext_lazy as _

#: A list of prefectures
JP_PREFECTURES = (
    ('hokkaido', _('Hokkaido'),),
    ('aomori', _('Aomori'),),
    ('iwate', _('Iwate'),),
    ('miyagi', _('Miyagi'),),
    ('akita', _('Akita'),),
    ('yamagata', _('Yamagata'),),
    ('fukushima', _('Fukushima'),),
    ('ibaraki', _('Ibaraki'),),
    ('tochigi', _('Tochigi'),),
    ('gunma', _('Gunma'),),
    ('saitama', _('Saitama'),),
    ('chiba', _('Chiba'),),
    ('tokyo', _('Tokyo'),),
    ('kanagawa', _('Kanagawa'),),
    ('niigata', _('Niigata'),),
    ('toyama', _('Toyama'),),
    ('ishikawa', _('Ishikawa'),),
    ('fukui', _('Fukui'),),
    ('yamanashi', _('Yamanashi'),),
    ('nagano', _('Nagano'),),
    ('gifu', _('Gifu'),),
    ('shizuoka', _('Shizuoka'),),
    ('aichi', _('Aichi'),),
    ('mie', _('Mie'),),
    ('shiga', _('Shiga'),),
    ('kyoto', _('Kyoto'),),
    ('osaka', _('Osaka'),),
    ('hyogo', _('Hyogo'),),
    ('nara', _('Nara'),),
    ('wakayama', _('Wakayama'),),
    ('tottori', _('Tottori'),),
    ('shimane', _('Shimane'),),
    ('okayama', _('Okayama'),),
    ('hiroshima', _('Hiroshima'),),
    ('yamaguchi', _('Yamaguchi'),),
    ('tokushima', _('Tokushima'),),
    ('kagawa', _('Kagawa'),),
    ('ehime', _('Ehime'),),
    ('kochi', _('Kochi'),),
    ('fukuoka', _('Fukuoka'),),
    ('saga', _('Saga'),),
    ('nagasaki', _('Nagasaki'),),
    ('kumamoto', _('Kumamoto'),),
    ('oita', _('Oita'),),
    ('miyazaki', _('Miyazaki'),),
    ('kagoshima', _('Kagoshima'),),
    ('okinawa', _('Okinawa'),),
)


#: A list of prefectures, the prefectures code as the first element.
JP_PREFECTURE_CODES = (
    ('01', _('Hokkaido'),),
    ('02', _('Aomori'),),
    ('03', _('Iwate'),),
    ('04', _('Miyagi'),),
    ('05', _('Akita'),),
    ('06', _('Yamagata'),),
    ('07', _('Fukushima'),),
    ('08', _('Ibaraki'),),
    ('09', _('Tochigi'),),
    ('10', _('Gunma'),),
    ('11', _('Saitama'),),
    ('12', _('Chiba'),),
    ('13', _('Tokyo'),),
    ('14', _('Kanagawa'),),
    ('15', _('Niigata'),),
    ('16', _('Toyama'),),
    ('17', _('Ishikawa'),),
    ('18', _('Fukui'),),
    ('19', _('Yamanashi'),),
    ('20', _('Nagano'),),
    ('21', _('Gifu'),),
    ('22', _('Shizuoka'),),
    ('23', _('Aichi'),),
    ('24', _('Mie'),),
    ('25', _('Shiga'),),
    ('26', _('Kyoto'),),
    ('27', _('Osaka'),),
    ('28', _('Hyogo'),),
    ('29', _('Nara'),),
    ('30', _('Wakayama'),),
    ('31', _('Tottori'),),
    ('32', _('Shimane'),),
    ('33', _('Okayama'),),
    ('34', _('Hiroshima'),),
    ('35', _('Yamaguchi'),),
    ('36', _('Tokushima'),),
    ('37', _('Kagawa'),),
    ('38', _('Ehime'),),
    ('39', _('Kochi'),),
    ('40', _('Fukuoka'),),
    ('41', _('Saga'),),
    ('42', _('Nagasaki'),),
    ('43', _('Kumamoto'),),
    ('44', _('Oita'),),
    ('45', _('Miyazaki'),),
    ('46', _('Kagoshima'),),
    ('47', _('Okinawa'),),
)
