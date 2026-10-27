def is_valid(s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            stack.append(char)
        else:
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


if __name__ == '__main__':
    for value in ['()', '()[]{}', '(]', '([{}])', '([)]']:
        print(f'{value}: {is_valid(value)}')
