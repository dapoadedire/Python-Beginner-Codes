def product(first, *args):
    result = first
    for x in args:
        result = result * x
    return result

a=product(2,3,3,4,5,6,7,8,9,10,11)
print(a)


def square(items):
    for i, x in enumerate(items):
        items[i] = x * x    # Modify items in-place

a = [1, 2, 3, 4, 5]
square(a)