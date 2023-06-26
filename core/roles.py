from rolepermissions.roles import AbstractUserRole


class Administrador(AbstractUserRole):
    available_permissions = {'criar_usuarios': True, 'ver_usuarios': True, 'criar_lotes': True, 'ver_lotes': True}


class Fiscal(AbstractUserRole):
    available_permissions = {'criar_usuarios': False, 'ver_usuarios': False, 'criar_lotes': False, 'ver_lotes': True}