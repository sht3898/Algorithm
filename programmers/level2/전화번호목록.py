def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        check = 0
        for j in range(len(phone_book)):
            if i == j:
                continue
            elif phone_book[i] == phone_book[j][:len(phone_book[i])]:
                answer = False
                check = 1
                break
        if check:
            break
    return answer


def solution2(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer


if __name__ == '__main__':
    print(solution2(['119', '97674223', '1195524421']))  # False
    print(solution2(['123','456','789']))   # Ture
    print(solution2(['12','123','1235','567','88']))    # False
