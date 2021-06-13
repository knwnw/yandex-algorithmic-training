def solution(results: list) -> int:
    win_idx = results.index(max(results))
    possible_results = []
    for i in range(win_idx + 1, len(results) - 1):
        if (results[i] % 5 == 0 and results[i] % 10 != 0
                and results[i] > results[i + 1]):
            possible_results.append(results[i])
    if possible_results:
        vasily_result = max(possible_results)
        vasily_place = 0
        for res in results:
            if vasily_result - res < 0:
                vasily_place += 1
        return vasily_place + 1
    return 0
