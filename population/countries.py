from pygal_maps_world.i18n import COUNTRIES
#需要安装pygal_maps_world模块
for country_code in sorted(COUNTRIES.keys()):
    print(country_code,COUNTRIES[country_code])