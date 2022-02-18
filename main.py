def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    S = [0]
    for i in range(n):
        S.append(S[i] + A[i])

    cnt = {}
    ans = 0

    for i in range(n):
        if S[i] in cnt:
            cnt[S[i]] += 1
        else:
            cnt[S[i]] = 1

        if S[i + 1] - k in cnt:
            ans += cnt[S[i + 1] - k]

    print(ans)


if __name__ == '__main__':
    main()
