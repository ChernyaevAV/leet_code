
def mergeAlternately2(word1: str, word2: str) -> str:
    res = ''
    length = len(word1) if len(word1) < len(word2) else len(word2)
    longest_word = word1 if len(word1) >= len(word2) else word2
    for i in range(length):
        res += word1[i] + word2[i]

    res += longest_word[length:]
    return res

def mergeAlternately1(word1: str, word2: str) -> str:
    res = ''
    if len(word1) == len(word2):
        for i in range(len(word1)):
            res += word1[i] + word2[i]
    elif len(word1) > len(word2):
        for i in range(len(word2)):
            res += word1[i] + word2[i]
        res += word1[len(word2)-len(word1):]
    else:
        for i in range(len(word1)):
            res += word1[i] + word2[i]
        res += word2[len(word1)-len(word2):]
    return res



if __name__ == '__main__':

    assert mergeAlternately1("abc", "pqr") == "apbqcr"
    assert mergeAlternately1("ab","pqrs") == "apbqrs"
    assert mergeAlternately1("abcd", "pq") == "apbqcd"

