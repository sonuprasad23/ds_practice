# day05/type_conversion.py
num_str = "123"
num_float = 45.67
num_int = 789

converted_int = int(num_str)
result1 = converted_int + 10
print(f"String '{num_str}' as int + 10 = {result1}")

converted_float_to_int = int(num_float)
print(f"Float {num_float} as int = {converted_float_to_int}")

converted_int_to_str = str(num_int)
print(f"Int {num_int} as str = '{converted_int_to_str}', Type: {type(converted_int_to_str)}")