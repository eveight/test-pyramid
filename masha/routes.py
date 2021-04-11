
def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view(name='uploads', path='masha:image')
    config.add_route('home', '/')
    config.add_route('home2', '/home2')
