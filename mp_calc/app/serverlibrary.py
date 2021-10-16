import copy


def merge(array, p, q, r, byfunc):
    sorted_arr = []
    left_arr = array[p:q]
    right_arr = array[q:r]
    left_index = 0
    right_index = 0

    # print('MERGE', left_arr, right_arr)
    # print('M-START', array[p:r])

    while True:
        if len(left_arr) + len(right_arr) == len(sorted_arr):
            break

        if left_index >= len(left_arr):
            sorted_arr.append(right_arr[right_index])
            right_index += 1
            continue

        if right_index >= len(right_arr):
            sorted_arr.append(left_arr[left_index])
            left_index += 1
            continue

        if byfunc(left_arr[left_index]) < byfunc(right_arr[right_index]):
            sorted_arr.append(left_arr[left_index])
            left_index += 1
        else:
            sorted_arr.append(right_arr[right_index])
            right_index += 1

    array[p:r] = sorted_arr
    # print('M-END', sorted_arr, array[p:r])


def mergesort_recursive(array, p, r, byfunc):
    if p == r:
        return
    if p + 1 == r:
        return

    p0 = p
    r0 = p + (r - p) // 2
    # p1 = r0 + 1
    r1 = r

    mergesort_recursive(array, p0, r0, byfunc)
    mergesort_recursive(array, r0, r1, byfunc)
    merge(array, p0, r0, r, byfunc)


def mergesort(array, byfunc=None):
    if byfunc is None:
        byfunc = lambda x: x

    mergesort_recursive(array, 0, len(array), byfunc)
    return array


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.__items:
            return None

        val = self.__items[-1]
        del self.__items[-1]
        return val

    def peek(self):
        if not self.__items:
            return None

        return self.__items[-1]

    @property
    def is_empty(self):
        return self.__items == []

    @property
    def size(self):
        return len(self.__items)


class EvaluateExpression:
    valid_char = '0123456789+-*/() '
    operators = '+-*/()'
    operands = '0123456789'
    verbose = False

    def __init__(self, string=""):
        self.expression = string

    def insert_space(self):
        new_string = ''

        for k, char in enumerate(self.expression):
            if char in self.operators:
                new_string += f' {char} '
            else:
                new_string += char

        return new_string

    @property
    def expression(self):
        return self._expression

    @expression.setter
    def expression(self, new_expr):
        for char in new_expr:
            if char not in self.valid_char:
                self._expression = ""
                return

        self._expression = new_expr

    def process_operator(self, operand_stack, operator_stack):
        if operator_stack.is_empty:
            return

        op = operator_stack.pop()
        right = operand_stack.pop()
        left = operand_stack.pop()

        if op == '+':
            operand_stack.push(left + right)
        elif op == '-':
            operand_stack.push(left - right)
        elif op == '*':
            operand_stack.push(left * right)
        elif op == '/':
            operand_stack.push(left // right)

    def debug(self, *args, **kwargs):
        if self.verbose:
            print(*args, **kwargs)

    def evaluate(self):
        operand_stack = Stack()
        operator_stack = Stack()
        expression = self.insert_space()
        tokens = expression.split()

        for k, token in enumerate(tokens):
            self.debug([k], token)

            if token in self.operands:
                operand_stack.push(int(token))

            elif token in '+-':
                while not operator_stack.is_empty:
                    if operator_stack.peek() in '()':
                        break

                    self.process_operator(
                        operand_stack, operator_stack
                    )
                operator_stack.push(token)

            elif token in '*/':
                while not operator_stack.is_empty:
                    if operator_stack.peek() not in '*/':
                        break

                    self.process_operator(
                        operand_stack, operator_stack
                    )
                operator_stack.push(token)

            elif token == '(':
                operator_stack.push('(')

            elif token == ')':
                while operator_stack.peek() != '(':
                    self.process_operator(
                        operand_stack, operator_stack
                    )

                # remove final (
                operator_stack.pop()

            self.debug('OPERATOR', operator_stack)
            self.debug('OPERAND', operand_stack)

        self.debug('A-OPERATOR', operator_stack)
        self.debug('A-OPERAND', operand_stack)

        while not operator_stack.is_empty:
            self.process_operator(
                operand_stack, operator_stack
            )

        self.debug('F-OPERATOR', operator_stack)
        self.debug('F-OPERAND', operand_stack)
        final_val = operand_stack.peek()
        return final_val


def get_smallest_three(challenge):
    records = challenge.records
    times = [r for r in records]
    mergesort(times, lambda x: x.elapsed_time)
    return times[:3]





