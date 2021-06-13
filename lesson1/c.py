def solution(number_to_add: str, num1: str, num2: str, num3: str) -> str:
    norm_num_to_add = normalize(number_to_add)
    norm_num1 = normalize(num1)
    norm_num2 = normalize(num2)
    norm_num3 = normalize(num3)

    result = ''
    result += 'YES\n' if norm_num_to_add == norm_num1 else 'NO\n'
    result += 'YES\n' if norm_num_to_add == norm_num2 else 'NO\n'
    result += 'YES' if norm_num_to_add == norm_num3 else 'NO'
    return result


def normalize(number: str) -> str:
    result = ''
    for char in number:
        if char.isdigit():
            result += char
    if len(result) == 11 and result[0] == '8':
        result = '7' + result[1:]
    if len(result) == 7:
        result = '7495' + result
    return result


if __name__ == '__main__':
    number_to_add = input()
    num1, num2, num3 = input(), input(), input()
    print(solution(number_to_add, num1, num2, num3))
