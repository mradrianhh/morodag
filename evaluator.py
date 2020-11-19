import sys

class Node:
    def __init__(self):
        self.item = None
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def push(self, item):
        oldtop = self.top
        self.top = Node()
        self.top.item = item
        if self.is_empty():
            self.top.next = None
        else:
            self.top.next = oldtop

    def pop(self):
        item = self.top.item
        self.top = self.top.next
        return item

class Evaluator():
    def __init__(self, expression):
        self.vals = LinkedStack()
        self.ops = LinkedStack()
        self.expression = expression

    def parse_expression(self):
        for element in self.expression:
            if element == "(":
                continue
            elif element == ")":
                self.calculate()
            elif element.isnumeric():
                self.vals.push(float(element))
            elif element in ["+", "-", "*", "/"]:
                self.ops.push(element)
            else:
                raise Exception("Expression not supported.")
        
        print(self.vals.pop())

    def calculate(self):
        val1 = self.vals.pop()
        val2 = self.vals.pop()
        op = self.ops.pop()
        
        val = 0
        if op == "+":
            val = val1 + val2
        elif op == "-":
            val = val1 - val2
        elif op == "*":
            val = val1 * val2
        elif op == "/":
            val = val1 / val2

        self.vals.push(val)
            

if __name__ == "__main__":
    evaluator = Evaluator(sys.argv[1])
    evaluator.parse_expression()
    
