def longest_valid_parentheses(s: str) -> int:
    stack = [-1]
    longest = 0

    for index, char in enumerate(s):
        if char == '(':
            stack.append(index)
        else:
            stack.pop()
            if not stack:
                stack.append(index)
            else:
                longest = max(longest, index - stack[-1])

    return longest


if __name__ == '__main__':
    for value in ['(()', ')()())', '', '()(())']:
        print(f'{value!r}: {longest_valid_parentheses(value)}')
