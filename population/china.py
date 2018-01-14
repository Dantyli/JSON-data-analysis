import pygal.maps.world
wm=pygal.maps.world.World()
wm.title='China'
wm.add('China',['cn'])
wm.render_to_file('china.svg')