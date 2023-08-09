import re

# configure regex
KEY_PATTERN = re.compile(r'\[(.+)\]')
VALUE_PATTERN = re.compile(r'"(.+)"')

# error comments
text_cant_open_configure_file = "Can't open conf.txt"


def load_configure_data():
    # load conf file
    try:
        with open("Configure/conf.txt", 'r') as conf_file:
            configure_data = dict()
            for line in conf_file:
                configure_data[str(re.findall(KEY_PATTERN, line)[0])] = str(re.findall(VALUE_PATTERN, line)[0])
        return configure_data
    except IOError:
        print(text_cant_open_configure_file)
        return dict()


def load_configure_file():
    # load conf file
    try:
        with open("Configure/conf.txt", 'r') as conf_file:
            configure_file = []
            for line in conf_file:
                configure_file.append(line)
        return configure_file
    except IOError:
        print(text_cant_open_configure_file)
        return dict()


def change_configure_file(key, value):
    configure_file = load_configure_file()
    try:
        with open("Configure/conf.txt", 'w') as conf_file:
            for line in configure_file:
                if str(re.findall(KEY_PATTERN, line)[0]) != key:
                    conf_file.write(line)
                else:
                    conf_file.write("[" + key + "] = \"" + value + "\"\n")
    except IOError:
        print(text_cant_open_configure_file)
