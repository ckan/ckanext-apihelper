import ckan.plugins as p


class APIHelperPluginClass(p.SingletonPlugin):
    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IRoutes, inherit=True)

    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'templates')

    def after_map(self, map):
        map.connect(
            'apihelper', '/apihelper/',
            controller='ckanext.apihelper.plugin:APIHelperController',
            action='view'
        )
        return map


class APIHelperController(p.toolkit.BaseController):

    def view(self):
        return 'meh'
