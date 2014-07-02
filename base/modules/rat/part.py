"""

Here you can disable rat module parts

It is very useful if you don't need every part
User should not install more packages :)

"""

config = {
    "application" : 1,
    "application.abstract" : 1,
    "application.bgtk" : 1,
    "application.game" : 0,
    "application.glut" : 0,
    "application.wgtk" : 0,
    "geometry" : 1,
    "geometry.vector" : 1,
    "cache" : 1,
    "ftool" : 1,
#    "logger" : 1, Unloadable
#    "registry" : 1, Unloadable
    "service" : 1
}
