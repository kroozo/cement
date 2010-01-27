"""
sayhi for the helloworld application.
"""

import os

from cement import namespaces
from cement.core.log import get_logger
from cement.core.opt import init_parser
from cement.core.hook import define_hook, register_hook
from cement.core.plugin import CementPlugin, register_plugin

log = get_logger(__name__)

VERSION = '0.1'
REQUIRED_CEMENT_API = '0.5-0.6:20100115'
BANNER = """
sayhi v%s (api:%s)
""" % (VERSION, REQUIRED_CEMENT_API)
 
@register_plugin() 
class sayhiPlugin(CementPlugin):
    #
    # Define hooks here, like so:
    #
    #   define_hook('sayhi_hook')
    
    def __init__(self):
        CementPlugin.__init__(self,
            label='sayhi',
            version=VERSION,
            description='sayhi plugin for helloworld',
            required_api=REQUIRED_CEMENT_API,
            banner=BANNER,
            controller='sayhiController'
            )
 
#      
# HOOKS: Usually defined in the main plugin file (here).  Functions
# that you decorate with @register_hook() will be run whenever/wherever 
# run_hooks('the_hook_name') is called.
#
@register_hook()
def options_hook(*args, **kwargs):
    """
    Register root options.
    """
    root_options = init_parser()
    root_options.add_option('--sayhi-root-option', action ='store_true', 
        dest='sayhi_root_option', default=None, help='example root option'
    ) 
    return ('root', root_options)
          
@register_hook()
def post_options_hook(cli_opts, cli_args, **kwargs):
    """Handle root options here."""
    pass
