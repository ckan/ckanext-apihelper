import logging
import routes.mapper
import ckan.plugins as p
import extract

log = logging.getLogger('ckanext_apihelper')


class APIHelperPluginClass(p.SingletonPlugin):
    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IRoutes, inherit=True)
    p.implements(p.ITemplateHelpers, inherit=True)

    actions = None

    def _get_actions(self):
        if self.actions is None:
            self.actions = extract.extract_actions()
        return self.actions

    def api_action_list(self, action_type=None):
        api_actions = self._get_actions()
        if action_type is None:
            return api_actions
        return api_actions.get(action_type, {})

    #IConfigurer
    def update_config(self, config):
        p.toolkit.requires_ckan_version(min_version='2.1.1')
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_resource('resource', 'ckanext-apihelper')

    #IRoutes
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

    #ITemplateHelpers
    def get_helpers(self):
        helpers = {
                'apihelper_action_list': self.api_action_list,
        }
        return helpers


class APIHelperController(p.toolkit.BaseController):

    def get(self):
        return p.toolkit.render('apihelper/index.html')

    def create(self):
        return p.toolkit.render('apihelper/index.html')

    def update(self):
        return p.toolkit.render('apihelper/index.html')

    def delete(self):
        return p.toolkit.render('apihelper/index.html')
