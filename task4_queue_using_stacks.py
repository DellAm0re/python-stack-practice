class MyQueue:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def _move_if_needed(self) -> None:
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

    def pop(self) -> int:
        self._move_if_needed()
        return self.output_stack.pop()

    def peek(self) -> int:
        self._move_if_needed()
        return self.output_stack[-1]

    def empty(self) -> bool:
        return not self.input_stack and not self.output_stack


if __name__ == '__main__':
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(queue.peek())   # 1
    print(queue.pop())    # 1
    print(queue.empty())  # False
