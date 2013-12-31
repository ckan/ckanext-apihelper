import os
import json
import logging
import ckan.plugins as p
import ckan.new_authz as new_authz


log = logging.getLogger('ckanext_apihelper')


def get_doc(action):
    return p.toolkit.get_action(action).__doc__

def check_function(action):
    check_list = [
        private_check,
        rest_check,
        internal_function_check,
    ]
    for fn in check_list:
        if not fn(action):
            return False
    return True

def private_check(action):
    if action.startswith('_'):
        return False
    return True

def rest_check(action):
    if action.endswith('_rest'):
        return False
    return True

def internal_function_check(action):
    internal_fn = [
        'get_site_user',
    ]
    if action in internal_fn:
        return False
    return True

def extract_actions():
    actions = {}

    for action_module_name in ['get', 'create', 'update', 'delete']:
        log.info('Fetching actions from '
                 'ckan.logic.actions.{0}.py'.format(action_module_name))
        count = 0
        actions[action_module_name] = {}
        module_path = 'ckan.logic.action.' + action_module_name
        module = __import__(module_path)
        for part in module_path.split('.')[1:]:
            module = getattr(module, part)
        for k, v in module.__dict__.items():
            if check_function(k):
                # Only load functions from the action module or already
                # replaced functions.
                if (hasattr(v, '__call__')
                        and (v.__module__ == module_path
                             or hasattr(v, '__replaced'))):
                    k = new_authz.clean_action_name(k)
                    actions[action_module_name][k] = get_doc(k)
    #TODO: Deal with plugins as well
    return actions
