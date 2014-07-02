from rat import part

if (part.config['application.abstract'] == 1):
    from abstract import *
if (part.config['application.glut'] == 1):
    from glut import *
if (part.config['application.game'] == 1):
    from game import *
if (part.config['application.wgtk'] == 1):
    from wgtk import *
if (part.config['application.bgtk'] == 1):
    from bgtk import *