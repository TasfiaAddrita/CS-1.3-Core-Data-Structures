#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_index here (iteratively and/or recursively)
    first_matching_index = find_all_indexes(text, pattern)
    return first_matching_index[0] if len(first_matching_index) != 0 else None

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""

    '''
    worksheet: String Algorithms, pt. 2

    let p = len(pattern)
    let t = len(text)

    p * t = checking every letter in text against every letter in pattern
    p(p-1) = p(p^2 - 1) = # REVIEW N/A VALUES IN WORKSHEET

    Best time complexity -- O(___), 
    Worst time complexity -- 
        O( p*t - p^2 + p ) = 
        O( p*t + 1) - p^2 ) =
        O( p*t - p^2 ) remove constant since it doesn't have that much of an effect

    if p < t, then O(p * t)
    '''

    if pattern == '':
        return list(range(0, len(text)))

    index = 0
    t_index = 0  # first letter of pattern
    matching_indexes_list = []
    
    while index <= len(text) - len(pattern):
        if text[index + t_index] == pattern[t_index]:
            # if t_index is the last index in pattern
            if t_index == len(pattern) - 1:
                matching_indexes_list.append(index)
                t_index = 0
                index += 1
            else:
                t_index += 1
        else:
            t_index = 0  # reset
            index += 1
                
    return matching_indexes_list

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))

def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")

if __name__ == '__main__':
    main()
