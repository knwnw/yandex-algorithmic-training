def solution(t_cond: int, t_room: int, mode: str) -> int:
    if mode == 'heat':
        return t_room if t_cond <= t_room else t_cond
    if mode == 'freeze':
        return t_cond if t_cond <= t_room else t_room
    if mode == 'auto':
        return t_room
    if mode == 'fan':
        return t_cond


t_room, t_cond = map(int, input().split())
mode = input()
print(solution(t_room, t_cond, mode))
