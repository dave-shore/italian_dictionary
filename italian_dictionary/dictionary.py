from .scraper import *


# ------italian_dictionary-------
def get_definition(word, headers, all_data=True, limit=None):
    if all_data:
        return get_data(word, headers)
    else:
        defs = get_data(word, headers, all_data=False)
        if limit is not None and len(defs) > limit:
            del defs[limit:]
        return defs
