import time
from set import Set, HashTable

def time_it(func):
    # Made wth love by Ben :heart: - DS 2.3
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        # print(func.__name__ + ' took ' + str((end - start) * 10000) + ' ms\n')
        print(func.__name__ + ' took ' + str((end - start)) + ' seconds')
        return result
    return wrapper

def get_dict_words():
    f = open('/usr/share/dict/words')
    word_list = f.readlines()
    word_list = [word.strip() for word in word_list]
    f.close()
    return word_list

# help from https://stackoverflow.com/questions/11989502/producing-all-the-anagrams-from-a-string-python
def simple_anagram(elements):
    if len(elements) <= 1:
        return elements
    else:
        ans = []
        for perm in simple_anagram(elements[1:]):
            for index in range(len(elements)):
                ans.append(perm[:index] + elements[0:1] + perm[index:])
        return ans

# @time_it
def real_anagram(elements):
    dict_words = get_dict_words()
    sim_ana = simple_anagram(elements)
    real_ana = []
    for word in sim_ana:
        if word in dict_words:
            real_ana.append(word)
    return real_ana

def get_circle_letters(words):
    circle_letters = []
    for w in words:
        circle_letters.extend([w[i] for i in words[w]])
    return circle_letters

def get_final_jumble(letters):
    s = Set(letters)
    # print(s.items())
    two_combos = []
    meh = []
    i = 0
    for l1 in s.items():
        for l2 in s.items()[i:]:
            if (l1 + l2) not in two_combos:
                two_combos.append(l1 + l2)
        i += 1
    # real_ana = real_anagram(two_combos)
    for combo in two_combos:
        meh.extend(real_anagram(combo))
    
    results = []
    for m in meh:
        # print(m)
        copy = letters.copy()
        copy.remove(m[0])
        copy.remove(m[1])
        # print(copy) 
        print(''.join(copy))
        real_ana = real_anagram(''.join(copy))
        print(real_ana)
        for ana in real_ana:
            results.append(meh + '-' + ana)
        
    print(results)

if __name__ == "__main__":
    jumble = ['tefon', 'sokik', 'niumem', 'siconu']
    words = [real_anagram(j)[0] for j in jumble]
    circle_indexes = [[2, 4], [0, 1, 3], [4], [3, 4]]
    circle_letters = get_circle_letters(dict(zip(words, circle_indexes)))
    print(circle_letters)
    print(get_final_jumble(circle_letters))
    
    # words = {real_anagram(j)[0]:[] for j in jumble}
    # print(words)
