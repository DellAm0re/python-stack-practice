def decode_string(s: str) -> str:
    stack = []
    current = ''
    number = 0

    for char in s:
        if char.isdigit():
            number = number * 10 + int(char)
        elif char == '[':
            stack.append((current, number))
            current = ''
            number = 0
        elif char == ']':
            previous, repeat = stack.pop()
            current = previous + current * repeat
        else:
            current += char

    return current


if __name__ == '__main__':
    for value in ['3[a]2[bc]', '3[a2[c]]', '2[abc]3[cd]ef']:
        print(decode_string(value))
