# Copyright (c) 2008-2011 by Enthought, Inc.
# Copyright (c) 2013 Continuum Analytics, Inc.
# All rights reserved.

from __future__ import absolute_import
import sys
import json

from ._version import get_versions
__version__ = get_versions()['version']

if sys.platform.startswith('linux'):
    from .linux import Menu, ShortCut

elif sys.platform == 'darwin':
    from .darwin import Menu, ShortCut

elif sys.platform == 'win32':
    from .win32 import Menu, ShortCut



def install(path, remove=False, root_prefix=sys.prefix,
            target_prefix=sys.prefix, env_name=None,
            env_setup_cmd=None):
    """
    install Menu and shortcuts
    """
    data = json.load(open(path))
    try:
        menu_name = data['menu_name']
    except KeyError:
        menu_name = 'Python-%d.%d' % sys.version_info[:2]

    shortcuts = data['menu_items']
    m = Menu(menu_name, prefix=root_prefix)
    if remove:
        for sc in shortcuts:
            ShortCut(m, sc, root_prefix=root_prefix,
                     target_prefix=target_prefix, env_name=env_name,
                     env_setup_cmd=env_setup_cmd).remove()
        m.remove()
    else:
        m.create()
        for sc in shortcuts:
            ShortCut(m, sc, root_prefix=root_prefix,
                     target_prefix=target_prefix, env_name=env_name,
                     env_setup_cmd=env_setup_cmd).create()

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions