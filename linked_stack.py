import sys

class Node:
    def __init__(self):
        self.item = None
        self.next = None

    def set_item(self, item):
        self.item = item

    def set_next(self, next):
        self.next = next

    def get_item(self):
        return self.item

    def get_next(self):
        return self.next

class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def size(self):
        length = 0
        current = self.top
        while(current != None):
            length += 1
            current = current.next
        return length

    def push(self, item):
        oldtop = self.top
        self.top = Node()
        self.top.item = item
        if self.is_empty():
            self.top.next = None
        else:
            self.top.next = oldtop

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty.")
        else:
            item = self.top.item
            self.top = self.top.next
            return item

class Evaluator():
    def __init__(self, expression):
        self.expression = expression

        self.vals = LinkedStack()
        self.ops = LinkedStack()

    def parse_expression(self):
        for element in self.expression:
            if element == "(":
                continue
            elif element == ")":
                self.calculate()
            elif element.isnumeric():
                self.push_val(element)
            elif element in ["+", "-", "*", "/"]:
                self.push_op(element)
            else:
                continue
        print(self.vals.pop())

    def push_val(self, val):
        self.vals.push(float(val))

    def push_op(self, op):
        self.ops.push(op)

    def calculate(self):
        val1 = self.vals.pop()
        val2 = self.vals.pop()
        op = self.ops.pop()
        if op == "+":
            self.vals.push(val1 + val2)
        elif op == "-":
            self.vals.push(val1 + val2)
        elif op == "*":
            self.vals.push(val1*val2)
        elif op == "/":
            self.vals.push(val1/val2)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("Please provide an expression.")
    
    evaluator = Evaluator(sys.argv[1])
    evaluator.parse_expression()
