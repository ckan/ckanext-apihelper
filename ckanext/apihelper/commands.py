import os
import json
import logging
import ckan.plugins as p
import ckan.new_authz as new_authz


log = logging.getLogger('ckanext_apihelper')


class ActionExtractor(p.toolkit.CkanCommand):
    """ Extract all the action functions into JSON.

    Usage: paster extract_actions

    Extracted from ckan.logic.get_action()
    """
    summary = __doc__.split('\n')[0]

    def command(self):
        self._load_config()
        actions = {}

        for action_module_name in ['get', 'create', 'update', 'delete']:
            log.info('Fetching actions from '
                     'ckan.logic.actions.{0}.py'.format(action_module_name))
            actions[action_module_name] = {}
            module_path = 'ckan.logic.action.' + action_module_name
            module = __import__(module_path)
            for part in module_path.split('.')[1:]:
                module = getattr(module, part)
            for k, v in module.__dict__.items():
                if not k.startswith('_') and not k.endswith('_rest'):
                    # Only load functions from the action module or already
                    # replaced functions.
                    if (hasattr(v, '__call__')
                            and (v.__module__ == module_path
                                 or hasattr(v, '__replaced'))):
                        k = new_authz.clean_action_name(k)
                        actions[action_module_name][k] = v.__doc__

                        # Whitelist all actions defined in logic/action/get.py as
                        # being side-effect free.
                        if action_module_name == 'get' and \
                           not hasattr(v, 'side_effect_free'):
                            v.side_effect_free = True
        #TODO: Deal with plugins as well
        here = os.path.abspath(os.path.dirname(__file__))
        apihelper = os.path.join(here, 'public', 'apihelper', 'actions.json')
        log.info('Writing JSON to {0}'.format(apihelper))
        try:
            with open(apihelper, 'w') as actions_json:
                json.dump(actions, actions_json)
            log.info('actions.json created successfully '
                     'in {0}'.format(apihelper))
        except Exception as e:
            log.error("Houston, we have a problem", exc_info=1)
