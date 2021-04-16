"""
l = ["Lee", "Kim", "Park"]
l_sort = l.sort()   #스트링 리스트를 정렬할 경우 첫 알파벳 아스키코드 기준으로 정렬된다. (캐릭터는 알파벳이 하나니까 당연히 그걸 기준으로 정렬)

print(l)
"""

import collections as ct


def solution(participant, complettion):
    participant.sort()
    complettion.sort()
    ans = ct.Counter(participant) - ct.Counter(complettion)

    return ans

# collections 모듈에 관한 설명은 https://wikidocs.net/84392 에서 확인!!
