stack=[10,20,30,40]
print(f"Original stack : {stack}")

last_item=stack.pop()
print(f"Popped last item: {last_item}, Stack now: {stack}")

first_item=stack.pop(0)
print(f"Popped first item: {first_item}, Stack now : {stack}")