import os


def env_as_str(name, default):
    return os.getenv('DJANGO_%s' % name, default)


def env_as_bool(name):
    return env_as_str(name, 'True') == 'True'


def env_as_list(name, default):
    return [x for x in env_as_str(name, default).split(',') if x != '']
