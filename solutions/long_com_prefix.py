from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

if __name__ == '__main__':
    # strs = ["flower", "flow", "flight"]
    # print(longestCommonPrefix(strs)) #"fl"

    strs = ["dog", "racecar", "car"]
    print(longestCommonPrefix(strs)) #""