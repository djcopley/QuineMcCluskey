from .minimize import minimize, format_minimized_expression


def cli():
    variables = int(input("Enter number of terms: "))
    mt = list(map(int, input("Enter minterms: ").split()))
    dc = list(map(int, input("Enter don't care terms: ").split()))

    minimized = minimize(variables, mt, dc)
    formatted_minimized = format_minimized_expression(minimized)

    print('\nMinimized Implicants: {}'.format(minimized))
    print('Minimized Expression: {}'.format(formatted_minimized))
