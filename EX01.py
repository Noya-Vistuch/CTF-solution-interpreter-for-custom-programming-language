def chu(tokens, stack, variables):
    """
     Pushes a numerical value or the value of a variable onto the stack.
    :param tokens: List of tokens from the command line
    :param stack: Stack for storing values
    :param variables: Dictionary for storing variables and their values
    :return: None
    """
    if tokens[1][0] == '!':  # If the token starts with '!', it's a variable
        var_name = tokens[1][1:]  # Extract the variable name
        if var_name not in variables:  # If the variable is not already in the dictionary, initialize it with 0
            variables[var_name] = 0
        stack.append(variables[var_name])  # Push the variable's value onto the stack
    else:
        stack.append(tokens[1])  # If it's a numerical value, push it onto the stack


def pabiku(tokens, stack, variables):
    """
    Pops the top value from the stack and assigns it to the specified variable.
    :param tokens: List of tokens from the command line
    :param stack: Stack for storing values
    :param variables: Dictionary for storing variables and their values
    :return: None
    """
    var_name = tokens[1][1:]  # Extract the variable name
    variables[var_name] = stack.pop()  # Pop the top value from the stack and assign it to the variable


def club(tokens, stack, variables):
    """
     Adds two values (either variables or numerical values) and stores the result in the specified variable.
    :param tokens: List of tokens from the command line
    :param stack: Stack for storing values
    :param variables: Dictionary for storing variables and their values
    :return: None
    """
    result_var = tokens[3][1:]  # Extract the result variable name
    # Check different combinations of variables and numbers, perform addition, and store the result in the result variable
    if tokens[1][0] == "!" and tokens[2][0] == "!":
        var_name1 = tokens[1][1:]
        var_name2 = tokens[2][1:]
        variables[result_var] = int(variables[var_name1]) + int(variables[var_name2])
    elif tokens[1][0] != "!" and tokens[2][0] == "!":
        var_value1 = tokens[1]
        var_name2 = tokens[2][1:]
        variables[result_var] = int(var_value1) + int(variables[var_name2])
    elif tokens[2][0] != "!" and tokens[1][0] == "!":
        var_value2 = tokens[2]
        var_name1 = tokens[1][1:]
        variables[result_var] = int(variables[var_name1]) + int(var_value2)
    else:
        var_value1 = tokens[1]
        var_value2 = tokens[2]
        variables[result_var] = int(var_value1) + int(var_value2)


def bebe(tokens, variables):
    """
    Converts a numerical value to its ASCII equivalent character and stores it in the specified variable.
    :param tokens: List of tokens from the command line
    :param variables: Dictionary for storing variables and their values
    :return: None
    """
    if tokens[1][0] == "!":
        var_name = tokens[1][1:]
        ascii_value = int(variables[var_name])
    else:
        ascii_value = int(tokens[1])
    result_var = tokens[2][1:]
    variables[result_var] = chr(ascii_value)


def baba(tokens, stack, variables):
    """
    Subtracts the second value from the first value (either variables or numerical values) and stores the result in the specified variable.
    :param tokens: List of tokens from the command line
    :param stack: Stack for storing values
    :param variables: Dictionary for storing variables and their values
    :return: None
    """
    result_var = tokens[3][1:]
    if tokens[1][0] == "!" and tokens[2][0] == "!":
        var_name1 = tokens[1][1:]
        var_name2 = tokens[2][1:]
        variables[result_var] = int(variables[var_name1]) - int(variables[var_name2])
    elif tokens[1][0] != "!" and tokens[2][0] == "!":
        var_value1 = tokens[1]
        var_name2 = tokens[2][1:]
        variables[result_var] = int(var_value1) - int(variables[var_name2])
    elif tokens[2][0] != "!" and tokens[1][0] == "!":
        var_value2 = tokens[2]
        var_name1 = tokens[1][1:]
        variables[result_var] = int(variables[var_name1]) - int(var_value2)
    else:
        var_value1 = tokens[1]
        var_value2 = tokens[2]
        variables[result_var] = int(var_value1) - int(var_value2)


def bubu(tokens, variables):
    """
    Converts a character or the value of a variable to its ASCII value and stores it in the specified variable.
    :param tokens: List of tokens from the command line
    :param variables: Dictionary for storing variables and their values
    :return: None
    """
    if len(tokens) == 3:
        if tokens[1][0] == "!":
            var_name = tokens[1][1:]
            letter = variables[var_name]
        else:
            letter = tokens[1]
        result_var = tokens[2][1:]
    else:
        letter = " "
        result_var = tokens[1][1:]
    variables[result_var] = ord(letter)


def pika(variables):
    """
    Prints the value of the variable x
    :param variables: Dictionary for storing variables and their values
    :return: None
    """
    print(variables["x"])


def process_code(code_lines):
    """
    Decodes the Girlang code language
    :param code_lines: List of lines of code
    :return: Dictionary containing variables and their values after processing the code
    """
    stack = []
    variables = {}

    for line in code_lines:
        tokens = line.split()

        if tokens[0] == 'chu':
            chu(tokens, stack, variables)
        elif tokens[0] == 'pabiku':
            pabiku(tokens, stack, variables)
        elif tokens[0] == 'club':
            club(tokens, stack, variables)
        elif tokens[0] == 'bebe':
            bebe(tokens, variables)
        elif tokens[0] == 'baba':
            baba(tokens, stack, variables)
        elif tokens[0] == 'bubu':
            bubu(tokens, variables)
        elif tokens[0] == 'bobo':
            bobo(tokens, variables)
        elif tokens[0] == 'gir':
            gir(tokens, variables)
        elif tokens[0] == 'golatu':
            golatu(tokens, variables)
        elif tokens[0] == 'pika':
            pika(variables)

    return variables


def bobo(tokens, variables):
    """
    Concatenates two strings (either variables or literal strings) and stores the result in the specified variable.
    :param tokens: List of tokens from the command line
    :param variables: Dictionary for storing variables and their values
    :return: None
    """
    if tokens[1][0] == "!" and tokens[2][0] == "!":
        var_name1 = tokens[1][1:]
        var_name2 = tokens[2][1:]
        str1 = variables[var_name1]
        str2 = variables[var_name2]
    elif tokens[1][1] == "!" and tokens[2][0] != "!":
        var_name1 = tokens[1][1:]
        str1 = variables[var_name1]
        str2 = tokens[2]
    elif tokens[1][1] != "!" and tokens[2][0] == "!":
        var_name2 = tokens[1][1:]
        str2 = variables[var_name2]
        str2 = tokens[2]
    else:
        str1 = tokens[1]
        str2 = tokens[2]

    result_var = tokens[3][1:]
    variables[result_var] = str1 + str2


def gir(tokens, variables):
    """
     Divides the first value by the second value (either variables or numerical values) and stores the integer quotient in the specified variable.
    :param tokens: List of tokens from the command line
    :param variables: Dictionary for storing variables and their values
    :return: None
    """
    if tokens[1][0] == "!" and tokens[2][0] == "!":
        var_name1 = tokens[1][1:]
        var_name2 = tokens[2][1:]
        value1 = variables[var_name1]
        value2 = variables[var_name2]
    elif tokens[1][0] == "!" and tokens[2][0] != "!":
        var_name1 = tokens[1][1:]
        value1 = variables[var_name1]
        value2 = tokens[2]
    elif tokens[1][0] != "!" and tokens[2][0] == "!":
        var_name2 = tokens[1][1:]
        value2 = variables[var_name2]
        value1 = tokens[2]
    else:
        value1 = tokens[1]
        value2 = tokens[2]
    result_var = tokens[3][1:]
    # Check for division by zero
    if value2 != 0:
        variables[result_var] = int(value1) // int(value2)
    else:
        print("Error: Division by zero")


def golatu(tokens, variables):
    """
    Computes the modulo of the division of the first value by the second value (either variables or numerical values) and stores the result in the specified variable.
    :param tokens: List of tokens from the command line
    :param variables: Dictionary for storing variables and their values
    :return: None
    """
    if tokens[1][0] == "!" and tokens[2][0] == "!":
        var_name1 = tokens[1][1:]
        var_name2 = tokens[2][1:]
        value1 = variables[var_name1]
        value2 = variables[var_name2]
    elif tokens[1][0] == "!" and tokens[2][0] != "!":
        var_name1 = tokens[1][1:]
        value1 = variables[var_name1]
        value2 = tokens[2]
    elif tokens[1][0] != "!" and tokens[2][0] == "!":
        var_name2 = tokens[1][1:]
        value2 = variables[var_name2]
        value1 = tokens[2]
    else:
        value1 = tokens[1]
        value2 = tokens[2]
    result_var = tokens[3][1:]

    variables[result_var] = int(value1) % int(value2)


# Define the main function to read the code from the file and process it
def main():
    # Prompt the user to enter the file path
    file_path = input("Enter the file path: ")

    try:
        # Read the code from the file
        with open(file_path, "r") as file:
            code_lines = file.readlines()

        # Process the code
        result = process_code(code_lines)
    except FileNotFoundError:
        print("File not found. Please make sure you entered the correct file path.")

if __name__ == "__main__":
    main()