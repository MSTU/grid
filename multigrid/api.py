from modelgrid import ModelGrid
from conf.configclient import LOCAL_WORK

__all__ = ['calculate', 'get', 'map', 'reload', 'ready']

_instance = ModelGrid(LOCAL_WORK)

calculate = _instance.calculate
get = _instance.get
map = _instance.map
reload = _instance.reload
ready = _instance.ready
web_get = _instance.web_get
web_get_ids = _instance.web_get_ids
web_get_results_from_job = _instance.web_get_results_from_job