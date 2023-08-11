#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    # Get the command-line arguments
    argv = sys.argv[1:]

    # Calculate the number of arguments
    num_arguments = len(argv)

    # Print the number of arguments and appropriate suffix
    if num_arguments == 0:
        print("{} arguments.".format(num_arguments))
    elif num_arguments == 1:
        print("{} argument:".format(num_arguments))
    else:
        print("{} arguments:".format(num_arguments))

    # Print each argument along with its position
    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")
