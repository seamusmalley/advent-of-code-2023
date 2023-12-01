# Constants
digit_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
digit_strings = list(digit_map.keys())
digits = list(digit_map.values())


# Part 1
def get_calibration_value(line: str) -> int:
    nums = []
    for char in line:
        if char in digits:
            nums.append(char)

    return int(nums[0] + nums[-1])


def trebuchet_calibration(input_filepath: str) -> int:
    input = open(input_filepath, 'r')
    lines = input.readlines()

    sum = 0
    for line in lines:
        sum += get_calibration_value(line)

    return sum


# Part 2
def get_first_digit(line: str) -> str:
    i, j = 0, 0
    while i < len(line):
        j = i
        while j < len(line):
            if line[i:j] in digits:
                return line[i:j]
            if line[i:j] in digit_strings:
                return digit_map[line[i:j]]
            j += 1
        i += 1


def get_last_digit(line: str) -> str:
    i, j = len(line), len(line)
    while i > -1:
        j = i
        while j > -1:
            if line[j:i] in digits:
                return line[j:i]
            if line[j:i] in digit_strings:
                return digit_map[line[j:i]]
            j -= 1
        i -= 1


def get_calibration_value_2(line: str) -> int:
    num1 = get_first_digit(line)
    num2 = get_last_digit(line)

    return int(num1 + num2)
    

def trebuchet_calibration_2(input_filepath: str) -> int:
    input = open(input_filepath, 'r')
    lines = input.readlines()

    sum = 0
    for line in lines:
        sum += get_calibration_value_2(line)

    return sum


if __name__ == '__main__':
    print(f'Part 1: {trebuchet_calibration("input.txt")}')
    print(f'Part 2: {trebuchet_calibration_2("input.txt")}')