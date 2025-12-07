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
    instructions = data.split("\n")
    position = 50
    zero_count = 0
    print("Input: ", instructions)
    print("starting position: ", position)

    # all the posible outcomes from a turn:
    # the dial moves right and doesn't pass or stop on zero
    # dial moves right and lands on zero
    # dial moves right and passes zero once or more times
    # dial moves left and doesn't pass or stop on zero
    # dial moves left and stops on zero, landing on it only once
    # dial moves left and passes zero only once
    # dial moves left and passes zero multiple times
    
    for instruction in instructions:
        # parse instruction
        direction = instruction[0] 
        distance = int(instruction[1:])

        # record starting position
        starting_position = position
    
        # determine direction as subtraction (left) or addition (right)
        if direction == 'L':
            position -= distance
        else:
            position += distance
        print("position: ", position)

        # tally a zero if the position is now negative
        # after starting at a positive position
        if position <= 0 and starting_position > 0:
            print("++ from negative position and positive starting position")
            zero_count += 1

        # calculate the multiples of 100 as proxy for
        # full turns around the wheel
        quotient = abs(position) // 100
        zero_count += quotient
        
        # normalise position to determine 0 to 99 position
        position = position % 100

        if position < 0:
            position += 100

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
