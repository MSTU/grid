from multigrid import api

__all__ = ['get_by_id', 'get_id', 'get_by_job']

get_by_id = api.web_get
get_id = api.web_get_ids
get_by_job = api.web_get_results_from_job