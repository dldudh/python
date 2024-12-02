def infinite_numbers():
    num = 0
    while True:
        yield num
        num += 1

def echo_coroutine():
    while True:
        value = (yield)
        if value is not None:
            print(f"받은 값 {value * 2}")

gen = infinite_numbers()
co = echo_coroutine()
next(co)

for _ in range(10):
    value = next(gen)
    co.send(value)