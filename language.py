from Configure.configure import load_configure_data, change_configure_file


class Language:
    current_language = load_configure_data()['language']

    def change_language(self, new_language):
        self.current_language = new_language
        change_configure_file("language", new_language)

    def return_language(self):
        return self.current_language
