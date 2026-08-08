import heapq

# Купа тут використовується, щоб сумувати попарно найменші кабелі спочатку, 
# і додавати до купи результат, як новий кабель, тоді загальні витрати 
# будуть мінімальні, тому що найдовші кабелі будуь брати участь в сумуванні менше


def min_connection_cost(cables):

    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first_smallest = heapq.heappop(cables)
        second_smallest = heapq.heappop(cables)

        connected = first_smallest + second_smallest
        total_cost += connected
        heapq.heappush(cables, connected)
    return total_cost

print(min_connection_cost([10, 1, 2, 7]))