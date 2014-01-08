#!/usr/bin/python

import sys
import os

__root_directory__ = os.path.abspath(os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0]))))
__curr_directory__ = os.getcwd()
__home_directory__ = os.path.expanduser("~")
__share_directory__ = __home_directory__ + "/.local/share"
__base_directory__ = __root_directory__ + "/base"
__data_directory__ = __base_directory__ + "/data"
__logs_directory__ = __base_directory__ + "/log"
__script_directory__ = __base_directory__ + "/script"
__cache_directory__ = __base_directory__ + "/cache"

__log_file__ = __logs_directory__ + "/error.log"

sys.path.append(__script_directory__)


import rattus

rattus.registry.setValue("path", {
                    "root": __root_directory__,
                    "cache": __cache_directory__,
                    "home": __home_directory__,
                    "data": __data_directory__,
                    "base": __base_directory__,
                    "logs": __logs_directory__,
                    "share": __share_directory__
                })
rattus.registry.setValue("basepath", {
                    "root": __base_directory__,
                    "font": __base_directory__ + "/font",
                    "icon": __base_directory__ + "/icon"
                })
rattus.registry.setValue("file", {
                    "log":  __log_file__
                })

rattus.init()


