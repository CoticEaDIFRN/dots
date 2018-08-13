import getpass
from dots.models import Colaborador
from django.core.exceptions import ValidationError


def get_input_data(field, message, default=None):
    raw_value = input(message)
    if default and raw_value == '':
        raw_value = default
    try:
        val = field.clean(raw_value, None)
    except ValidationError as e:
        print("Error: %s" % '; '.join(e.messages))
        val = None
    return val


def get_password():
    password = None
    while password is None:
        password = getpass.getpass()
        password2 = getpass.getpass('Password (again): ')
        if password != password2:
            print("Error: Your passwords didn't match.")
            password = None
            continue

        if password.strip() == '':
            print("Error: Blank passwords aren't allowed.")
            password = None
            continue

        return password


def criar_primeiro_colaborador(apps, schema_editor):
    print('\nCadastre o administrador')
    user = Colaborador()
    user.cpf = get_input_data(Colaborador._meta.get_field('cpf'), 'CPF: ')
    user.nome = get_input_data(Colaborador._meta.get_field('nome'), 'Nome: ')
    user.is_staff = True
    user.is_superuser = True
    user.set_password(get_password())
    user.save()
