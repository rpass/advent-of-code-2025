import os


def process_input(data):
    """
    Calculate the number of times a combination dial of 99 spaces lands on 0
    after following set instructions.

    Instructions come in a series of left and right turns of the dial.
    These are relative to the current position of the dial.
    The dial starts at 50.
    i.e. L33 moves the dial to 17. R8 moves the dial to 25. etc.
    The dial wraps. i.e. L50 moves the dial to 0. L1 moves the dial to 99. etc.


    Args:
        data: The contents of the input file as a string

    Returns:
        The processed result
    """
    # TODO: Implement your solution here
    instructions = data.split("\n")
    position = 50
    zero_count = 0
    print("Input: ", instructions)
    print("starting position: ", position)
    for instruction in instructions:
        direction = instruction[0] 
        distance = int(instruction[1:])
        if direction == 'L':
            position -= int(instruction[1:])
        else:
            position += int(instruction[1:])

        position = position % 99

        if position < 0:
            position += 100

        if position == 0:
            zero_count += 1
        print("position: ", position)

    return zero_count


def main():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, "input.txt")

    # Read input.txt from the same directory as this script
    with open(input_file, "r") as f:
        file_data = f.read()

    # Call the placeholder function with the file data
    result = process_input(file_data)

    # Print the result (or handle it as needed)
    print(result)


if __name__ == "__main__":
    main()
