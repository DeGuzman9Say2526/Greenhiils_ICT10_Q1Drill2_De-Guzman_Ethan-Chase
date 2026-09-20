from pyscript import document

def addition(e):
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    ans = first_number + second_number

    document.getElementById('display').innerHTML = f'The sum of {first_number} and {second_number} is {ans}'

def subtraction(e):
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    ans = first_number - second_number

    document.getElementById('display').innerHTML = f'The difference of {first_number} and {second_number} is {ans}'

def multiplication(e):
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    ans = first_number * second_number

    document.getElementById('display').innerHTML = f'The product of {first_number} and {second_number} is {ans}'

def division(e):
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)

    if second_number == 0:
        document.getElementById('display').innerHTML = 'No thanks.'
        return

    ans = first_number / second_number
    document.getElementById('display').innerHTML = f'The quotient of {first_number} and {second_number} is {ans}'

def modulus(e):
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)

    if second_number == 0:
        document.getElementById('display').innerHTML = 'No thanks.'
        return

    ans = first_number % second_number
    document.getElementById('display').innerHTML = f'The remainder of {first_number} and {second_number} is {ans}'

def exponent(e):
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    ans = first_number ** second_number

    document.getElementById('display').innerHTML = f'{first_number} raised to {second_number} is {ans}'

def floor_div(e):
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)

    if second_number == 0:
        document.getElementById('display').innerHTML = 'No thanks.'
        return

    ans = first_number // second_number
    document.getElementById('display').innerHTML = f'The floor division of {first_number} and {second_number} is {ans}'