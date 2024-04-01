import time


class Timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0

    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        result = self.func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        self.alltime += elapsed
        print(f"{self.func.__name__} : {elapsed}, {self.alltime}")
        return result


@Timer
def list_comp(n):
    return [x * 2 for x in range(n)]


@Timer
def map_call(n):
    return list(map((lambda x: x * 2), range(n)))


result = list_comp(5)

list_comp(50000)  # list_comp : 2.00001522898674e-06, 2.00001522898674e-06
list_comp(500000)  # list_comp : 0.0016873001586645842, 0.001689300173893571
list_comp(1000000)  # 0.01592999999411404, 0.017619300168007612
print(result)  # [0, 2, 4, 6, 8]
print(f'all time {list_comp.alltime}')  # all time 0.05054970015771687

print('')

result = map_call(5)  # map_call : 4.800036549568176e-06, 4.800036549568176e-06

map_call(50000)  # map_call : 0.0019276998937129974, 0.0019324999302625656
map_call(500000)  # map_call : 0.025070100091397762, 0.027002600021660328
map_call(1000000)  # map_call : 0.052375399973243475, 0.0793779999949038
print(result)  # [0, 2, 4, 6, 8]
print(f'all time {map_call.alltime}')  # all time 0.0793779999949038

print(f"\n**map/comp = {round(map_call.alltime / list_comp.alltime, 3)}")
