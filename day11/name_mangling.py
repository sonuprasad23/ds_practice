class MySecretClass:
    def __init__(self):
        self.__secret_value = 42 

    def get_secret(self):
        return self.__secret_value

obj_secret = MySecretClass()
print(f"Secret via getter: {obj_secret.get_secret()}")

try:
    print(f"Trying obj_secret.__secret_value: {obj_secret.__secret_value}")
except AttributeError as e:
    print(f"Error accessing __secret_value directly: {e}")


print(f"Accessing mangled name _MySecretClass__secret_value: {obj_secret._MySecretClass__secret_value}")