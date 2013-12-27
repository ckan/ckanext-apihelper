import routes.mapper
import ckan.plugins as p


class APIHelperPluginClass(p.SingletonPlugin):
    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IRoutes, inherit=True)

    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_public_directory(config, 'public')

    def after_map(self, map):
        map.redirect('/apihelper', '/apihelper/get')
        map.redirect('/apihelper/', '/apihelper/get')
        with routes.mapper.SubMapper(map,
                controller='ckanext.apihelper.plugin:APIHelperController') as m:
            m.connect('apihelper_get', '/apihelper/get', action='get')
            m.connect('apihelper_create', '/apihelper/create', action='create')
            m.connect('apihelper_update', '/apihelper/update', action='update')
            m.connect('apihelper_delete', '/apihelper/delete', action='delete')
        return map


class APIHelperController(p.toolkit.BaseController):

    def get(self):
        return p.toolkit.render('apihelper/index.html')

    def create(self):
        return p.toolkit.render('apihelper/index.html')

    def update(self):
        return p.toolkit.render('apihelper/index.html')

    def delete(self):
        return p.toolkit.render('apihelper/index.html')
