from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)

    def is_empty(self):
        return len(self.container) == 0


def revers_string(str_to_reverse):
    stack = Stack()
    for ch in str_to_reverse:
        stack.push(ch)
    reversed_str = ''
    for ch in range(stack.size()):
        reversed_str += stack.pop()
    return reversed_str


def is_balanced(str_to_check):
    stack = Stack()

    for ch in str_to_check:
        if ch == '{' or ch == '[' or ch == '(':
            stack.push(ch)

        if ch == '}':
            if stack.size() > 0 and stack.peek() == '{':
                stack.pop()
            else:
                return False

        if ch == ']':
            if stack.size() > 0 and stack.peek() == '[':
                stack.pop()
            else:
                return False

        if ch == ')':
            if stack.size() > 0 and stack.peek() == '(':
                stack.pop()
            else:
                return False

    if stack.size() == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(revers_string('barak obama'))

    print(is_balanced("[[{(((())}]]"))
