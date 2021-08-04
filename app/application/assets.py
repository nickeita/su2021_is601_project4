from flask import current_app as app
from flask_assets import Bundle


def compile_static_assets(assets):
    # Home asset bundles
    home_style_bundle = Bundle('src/less/*.less', filters='less,cssmin', output='dist/css/style.min.css',
                               extra={'rel': 'stylesheet/css'})

    home_js_bundle = Bundle('src/js/home.js', filters='jsmin', output='dist/js/home.min.js')

    assets.register('home_styles', home_style_bundle)
    assets.register('home_js', home_js_bundle)

    if app.config['FLASK_ENV'] == 'development':
        home_style_bundle.build()
        home_js_bundle.build()
