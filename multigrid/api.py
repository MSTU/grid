from multigrid import MultiGrid
from conf.configclient import LOCAL_WORK

__all__ = ['calculate', 'get', 'map', 'reload', 'ready', 'web_get']

_instance = MultiGrid(LOCAL_WORK)

calculate = _instance.calculate
get = _instance.get
map = _instance.map
reload = _instance.reload
ready = _instance.ready
web_get = _instance.web_get