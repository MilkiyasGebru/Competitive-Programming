def main():
    Arr = input().split()
    M = int(Arr[0])
    N = int(Arr[1])
    a = int(Arr[2])
    print(flagstones(M, N, a))
def flagstones(M, N, a):
    if M % a == 0:
        M = M
    else:
        M = (M // a + 1) * a
    if N % a == 0:
        N = N
    else:
        N = (N // a + 1) * a
    return (M * N) // (a * a)
main()
