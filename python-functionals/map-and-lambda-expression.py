cube = lambda x: x ** 3

def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    mem = [0, 1]
    for i in range(2, n):
        mem.append(mem[i - 1] + mem[i - 2])
    return mem

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))