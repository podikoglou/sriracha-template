from controllers.index import Index
#from sriracha import StaticController

routes = {
    '/': Index(),
#    '/static/(.*)', StaticController('./public/')
}
