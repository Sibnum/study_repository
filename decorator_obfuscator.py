def obfuscator(func):
    def wrapper():
        result_func = func()
        name = result_func['name']
        password = result_func['password']
        new_name = name[:1] + '*******' + name[-1:]
        new_password = '*' * len(password)
        return {'name': new_name, 'password': new_password}
    return wrapper


@obfuscator
def get_credentials():
    return {
        'name': 'StasBasov',
        'password': 'iamthebest'
    }


print(get_credentials())
