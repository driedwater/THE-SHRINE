import sys

def CountLetters():
    c = sys.argv[1]
    cnt = dict()
    for char in c:
        if char != ',':
            if char not in cnt:
                cnt[char] = 0
            cnt[char] += 1
    
    for k in sorted(cnt.keys(), reverse=True):
        print(f"{k}:{cnt[k]}", end=' ')

if __name__ == "__main__":
    CountLetters()
