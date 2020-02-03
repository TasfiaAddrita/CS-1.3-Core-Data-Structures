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
    # TODO: Implement find_index here (iteratively and/or recursively)


# def find_all_indexes(text, pattern):
def find_all_indexes(string, target):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    # assert isinstance(text, str), 'text is not a string: {}'.format(text)
    # assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    assert isinstance(string, str), 'text is not a string: {}'.format(text)
    assert isinstance(target, str), 'pattern is not a string: {}'.format(text)

    # TODO: Implement find_all_indexes here (iteratively and/or recursively)

    if target == '':
        return list(range(0, len(string)))

    index = 0
    t_index = 0  # first letter of target word
    start_index = None
    matching_indexes_list = []
    # xyz = [index for index, value in enumerate(string) if string[index] == target[0] and index <= len(string) - len(target) and index != 0]
    # print(xyz)
    # xyz_index = 0
    # went_back = False

    while index < len(string):
        if string[index].isalpha():
            # if string[index] == target[0] and index <= len(string) - len(target) and not went_back:
            #     xyz.append(index)
            #     went_back = False
            if string[index] == target[t_index]:
                if t_index == 0:
                    start_index = index
                if t_index == len(target) - 1:
                    matching_indexes_list.append(start_index)
                    t_index = 0
                    if string[index] == target[t_index]:
                        if len(target) == 1:
                            index += 1
                        continue
                else:
                    t_index += 1  # go to next letter of target word
            else:
                t_index = 0  # reset
                if string[index] == target[t_index]:
                    start_index = index
                    t_index += 1
                else:
                    start_index = None

                # if xyz_index == 0:
                #     xyz_index += 1
                # print(xyz, xyz_index)
                # if len(xyz) != 0 and xyz_index < len(xyz):
                #     index = xyz[xyz_index]
                #     xyz_index += 1
                #     # t_index += 1
                #     # went_back = True
                #     start_index = None
                #     continue

        index += 1
    # assert matching_indexes_list == [1]
    # return list(set(matching_indexes_list))
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
    # main()
    # print(find_all_indexes('ababc', 'abc'))
    # print(find_all_indexes('aaaaab', 'aaab')) # fails
    # print(find_all_indexes('abc', 'a'))
    # print(find_all_indexes('aaa', 'aa'))
