arr = list(input())
result = []
# +, - 제거
for i in range(len(arr)):
    if arr[i] == '-':
        arr[i] = arr[i-1]
for i in range(len(arr)-1, -1, -1):
    if arr[i] == '+':
        arr[i] = arr[i+1]

if arr.count('[') != arr.count(']'):
    print(False)
elif arr.count('{') != arr.count('}'):
    print(False)
elif arr.count('(') != arr.count(')'):
    print(False)
else:
    for idx in arr:
        if idx in '[{(':
            result.append(idx)
        elif idx in [']})']:
            if len(result) == 0:
                print(False)
                break
            if idx == ')' and (result[-1] == '{' or result[-1] == ']'):
                print(False)
                break
            if idx == '}' and (result[-1] == '(' or result[-1] == '['):
                print(False)
                break
            if idx == ']' and (result[-1] == '{' or result[-1] == '('):
                print(False)
                break
            result.pop()
    print(True)
