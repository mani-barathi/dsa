
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

def reverse(expression):
    result = ''
    for char in expression[::-1]:
        c = ')' if char == '(' else '(' if char == ')' else char
        result += c

    return result

def infix_to_prefix(infix):
    prefix = ''
    stack = []
    infix = reverse(infix)

    for char in infix:
        is_operator = char in operators
        is_bracket = char in brackets
        is_operand = not is_operator and not is_bracket

        if is_operand:
            prefix += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack:
                poped = stack.pop()
                if poped == '(':
                    break
                prefix += poped
        elif is_operator:
            if len(stack) == 0:
                stack.append(char)
            else:
                if precedense(char) > precedense(stack[len(stack) - 1]):
                    stack.append(char)
                elif precedense(char) == precedense(stack[len(stack) - 1]) and char == '^':
                    while stack and precedense(char) == precedense(stack[len(stack) - 1]) and char == '^':
                        prefix += stack.pop()
                    stack.append(char)
                elif precedense(char) == precedense(stack[len(stack) - 1]):
                    stack.append(char)
                elif precedense(char) < precedense(stack[len(stack) - 1]):
                    while stack and precedense(char) < precedense(stack[len(stack) - 1]):
                        prefix += stack.pop()
                    stack.append(char)

    while stack:
        prefix += stack.pop()

    return reverse(prefix)

expression = 'a+(b*c)-(d/e)'
expression = '((a+b-c)*d^e^f)/g'
expression = 'a+b*c'

print(f'infix   : {expression}')
print(f'prefix : {infix_to_prefix(expression)}')
