from string import ascii_lowercase
pad = []
char_low = list(ascii_lowercase)
for i in range(8):
    if i == 5 or i == 7: 
        pad.append(char_low[:4])
        del char_low[:4]
    else:
        pad.append(char_low[:3])
        del char_low[:3]
pad = [[], []] + pad 
def main(digits): 
    digits = list(digits)
    digits = [int(_) for _ in digits]
    return solver(digits)

def solver(digits):
    if len(digits) == 0: 
        return []
    if len(digits) == 1: 
        n = digits[0]
        return pad[n]
    combs = solver(digits[1:])
    first = digits[0]
    result = []
    for char in pad[first]: 
        for comb in combs: 
            result.append(char + comb)
    return result
