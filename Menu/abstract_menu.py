class AbstractMenu:

    def run_loop(self):
        pass

    def events_handler(self):
        pass

    def happened(self, event):
        pass

    def triggered(self, event):
        pass

    def select_option(self):
        pass

    def clear_screen(self):
        pass

    def render_options(self):
        pass

    def render_text(self, _string, color, number_position, shift):
        pass

    def render_title(self):
        pass

    def update_display(self):
        pass
