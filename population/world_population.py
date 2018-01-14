import json
import pygal.maps.world
from country_codes import get_country_code
#创建一个包含人口数量的字典
cc_populations={}
filename='population.json'
with open(filename) as f:
    pop_data=json.load(f)
#打印每个国家2010年的人口
for pop_dict in pop_data:
    if pop_dict['Year']=='2010':
        country_name=pop_dict['Country Name']
        population=int(float(pop_dict['Value']))
        code=get_country_code(country_name)
        if code :
            cc_populations[code]=population
wm=pygal.maps.world.World()
wm.title='2010 年 世界人口地图'
wm.add('2010',cc_populations)
wm.render_to_file('world_population.svg')

