"""
Heavily based on from https://github.com/jupyter/notebook/issues/1000#issuecomment-359875246
"""

import os.path
import json
import re
import ipykernel
import requests

from requests.compat import urljoin

try:  # Python 3 (see Edit2 below for why this may not work in Python 2)
    from notebook.notebookapp import list_running_servers
except ImportError:  # Python 2
    import warnings
    from IPython.utils.shimmodule import ShimWarning
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=ShimWarning)
        from IPython.html.notebookapp import list_running_servers


def generate_save_path():
    """Basically the only thing added by Joel"""
    path_to_here = os.path.abspath('')
    path_to_base = path_to_here.split("/theme")[0]
    path_from_base = path_to_here[len(path_to_base)+1:]
    nb_name = get_notebook_name().replace('.ipynb', '')
    return os.path.join(path_from_base, nb_name)


def get_eu_countries():
    """Extact all EU country codes"""
    url = 'https://restcountries.eu/rest/v2/regionalbloc/eu'
    r = requests.get(url)
    return [row['alpha2Code'] for row in r.json()]


def get_notebook_name():
    """
    Return the full path of the jupyter notebook.
    """
    kernel_id = re.search('kernel-(.*).json',
                          ipykernel.connect.get_connection_file()).group(1)
    servers = list_running_servers()
    for ss in servers:
        response = requests.get(urljoin(ss['url'], 'api/sessions'),
                                params={'token': ss.get('token', '')})
        for nn in json.loads(response.text):
            if nn['kernel']['id'] == kernel_id:
                relative_path = nn['notebook']['path']
                return relative_path

