"""
입력
    첫째 줄에 문자열이 주어진다. 문자열의 길이는 1보다 크거나 같고, 1,000,000보다 작거나 같다.
    둘째 줄에 폭발 문자열이 주어진다. 길이는 1보다 크거나 같고, 36보다 작거나 같다.
    두 문자열은 모두 알파벳 소문자와 대문자, 숫자 0, 1, ..., 9로만 이루어져 있다.

출력
    첫째 줄에 모든 폭발이 끝난 후 남은 문자열을 출력한다.
"""

_string = input()
_bomb = input()
bomb_len = len(_bomb)
stack = []

for char in _string:
    stack.append(char)
    if len(stack) >= bomb_len and ''.join(stack[-bomb_len:]) == _bomb:
        for _ in range(bomb_len):
            stack.pop()

result = ''.join(stack)
print(result if result else "FRULA")