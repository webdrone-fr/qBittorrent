

import os as _os, urllib.request as _ur
_proxy = _os.environ.get("HTTP_PROXY") or _os.environ.get("HTTPS_PROXY")
if _proxy:
    _opener = _ur.build_opener(_ur.ProxyHandler({"http": _proxy, "https": _proxy}))
    _ur.install_opener(_opener)
