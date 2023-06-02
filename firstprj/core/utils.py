def number_to_words(number):
    # Define the word representations for numbers up to 19
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
            'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
            'eighteen', 'nineteen']

    # Define the word representations for tens
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    # Define the word representations for powers of ten
    scales = ['thousand', 'million', 'billion', 'trillion']

    # Convert the number into a string and split it into groups of three digits
    number_str = str(number)
    groups = [number_str[max(0, i - 3):i] for i in range(len(number_str), 0, -3)]
    groups = [int(group) for group in groups[::-1]]  # Convert each group to an integer

    # Handle the case for zero
    if number == 0:
        return ones[0]

    # Initialize an empty list to store the words for each group
    words = []

    # Iterate over each group and convert it to words
    for i, group in enumerate(groups):
        if group > 0:
            # Convert the hundreds place
            hundreds = group // 100
            if hundreds > 0:
                words.append(ones[hundreds] + ' hundred')

            # Convert the tens and ones places
            tens_ones = group % 100
            if tens_ones > 0:
                if tens_ones < 20:
                    words.append(ones[tens_ones])
                else:
                    tens_digit = tens_ones // 10
                    ones_digit = tens_ones % 10
                    words.append(tens[tens_digit - 2])
                    if ones_digit > 0:
                        words.append(ones[ones_digit])

            # Add the scale word if necessary
            if i > 0:
                words.append(scales[i - 1])

    # Return the final word representation
    return ' '.join(words)
