def eval_rpn(tokens: list[str]) -> int:
    stack = []

    for token in tokens:
        if token not in ('+', '-', '*', '/'):
            stack.append(int(token))
            continue

        right = stack.pop()
        left = stack.pop()

        if token == '+':
            result = left + right
        elif token == '-':
            result = left - right
        elif token == '*':
            result = left * right
        else:
            quotient = abs(left) // abs(right)
            result = -quotient if (left < 0) != (right < 0) else quotient

        stack.append(result)

    return stack[-1]


if __name__ == '__main__':
    print(eval_rpn(['2', '1', '+', '3', '*']))
    print(eval_rpn(['4', '13', '5', '/', '+']))
    print(eval_rpn(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']))
