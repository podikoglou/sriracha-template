from sriracha import Controller, render_view

class Index(Controller):

    def handle_request(self, request):
        return render_view('index', model={})
