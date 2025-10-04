import re
import sys

def SearchPattern():
    candidate = sys.argv[1]
    pattern = sys.argv[2]

    z = len([*re.finditer(f'(?={pattern})', candidate)])
    print(f'Pattern appears {z} time!')
if __name__ == "__main__":
    SearchPattern()
