keys = ['k1', 'k2', 'k3']
values = [10, 20, 30]

d_from_lists= {}

if len(keys) == len(values):
    for i in range(len(keys)):
        d_from_lists[keys[i]] = values[i]

print(f"Dict from lists (loop): {d_from_lists}")


if len(keys) == len(values):
    d_comp = {keys[i]: values[i] for i in range(len(keys))}
    print(f"Dict from lists (comp): {d_comp}")


if len(keys) == len(values):
    d_zip = dict(zip(keys, values))
    print(f"Dict from lists (zip): {d_zip}")

    