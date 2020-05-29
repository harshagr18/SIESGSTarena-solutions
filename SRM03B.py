for case in range(int(input().strip())):
    N = int(input().strip())
    events = list(map(int, input().strip().split()))
    dec = min(events)
    for event in range(N):
        events[event] -= dec
    event = dec
    count = 0
    while events[event % N] - count > 0:
        event += 1
        count += 1
    print((event % N) + 1)