
operators = '+-*/^'
brackets =  '()'

def precedense(char):
    if char in '^':
        return 3
    if char in '*/':
        return 2
    if char in '+-':
        return 1
    return -1


def infix_to_postfix(infix):
    postfix = ''
    stack = []

    for char in infix:
        is_operator = char in operators
        is_bracket = char in brackets
        is_operand = not is_operator and not is_bracket

        if is_operand:
            postfix += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack:
                poped = stack.pop()
                if poped == '(':
                    break
                postfix += poped
        elif is_operator:
            if len(stack) == 0:
                stack.append(char)
            else:
                if precedense(char) > precedense(stack[len(stack) - 1]):
                    stack.append(char)
                elif precedense(char) == precedense(stack[len(stack) - 1]) and char == '^':
                    stack.append(char)
                else:
                    while stack and precedense(char) <= precedense(stack[len(stack) - 1]):
                        postfix += stack.pop()
                    stack.append(char)

    while stack:
        postfix += stack.pop()

    return postfix

expression = 'a+(b*c)-(d/e)'
expression = '((a+b-c)*d^e^f)/g'
# expression = 'a+b*c'

print(f'infix   : {expression}')
print(f'postfix : {infix_to_postfix(expression)}')
