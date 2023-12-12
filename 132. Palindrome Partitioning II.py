import sys 
print(sys.getrecursionlimit())
sys.setrecursionlimit(3000)
from math import inf 

# targest, find fewest palindrome to make up the entire string 


# given a string, return all palindrome that begins at index 0 
def all_pal(s): 
    res = [] 
    for i in range(1, len(s) + 1): 
        if check_pal(s[:i]): 
            res.append(s[:i])
    return reversed(res)
            
def check_pal(s): 
    l = len(s) // 2
    for i in range(l): 
        if s[i] != s[- 1 - i]: 
            return False 
    return True 


def solver(s):
    # in memo, given index, store min cuts from index - end 
    memo = {} 
    if check_pal(s): 
        return 0 
    def recur(index): 
        if index in memo: 
            return memo[index]
        if index == len(s): 
            return 0 
        if check_pal(s[index:]):
            return 1
        all = all_pal(s[index:])
        res = inf 
        for pal in all: 
            l = len(pal)
            tmp = recur(index + l)
            if tmp == 1: 
                memo[index] = 1 + tmp 
                return 1 + tmp
            res = min(res, 1 + tmp)
        memo[index] = res
        return res 
    
    return recur(0) - 1





s = "aabaaa"

# s  = "bcozzltywqyvgurhlsvmclrkvmdldwnueawtkzgiwpdtidjouhxtvrkygyofkjdyxfuaohhkwxnkdfzmfodzoiuenpvqhunvutpipgidfvyucssxjqmdtwvfqqoyqgskfdcakjeraiipfvfhhghmriqojfyifnmoeisqwpzhxtniktwjkneudrwunqracbxhkyjuifyzohfqpctkeudzspzmuyhfwhexstgekfnddtphsunuwlldchfmzjdxglmzfvohxltcebtizdvihsfazzjrtbhsitwntdmofjutdytogdhbkiieqtaluaorepkxkaxhflmxlaesmndxjefklxprytnwvmxomidwzmqxzdedgtjclalckzvftcvikxbkanytvfpnvxmrmrwsdexscypdjxlgpzzeroppuidblcujkddyuhczexfijhvahaxctlsyfeoaxjoqzpqulgccwugtnxijuunfprgypmiphndpajnkmwauonnucmqfnlvcftkwyznqacbgovjkzubnfrktwgghbcpytistwgbabuiknrakrqyzpewqovgwkjnveatfbbvvkwapjlemcousoikffuotqsdgotqmkahmpkjmjrjevvjianpjukozovrrdqprzhwxbuvzqtsjzmgkmbqmmqlxvvunfwonlppzvhjxcuhbxazcicpimmyjlkluxszomsdnecbkijnzwqechtvsueywibiiyyxowxkjjxesixgdjupvzlmglqypkedwzigljlgouhulwurpdmavlvrqwqfutumauoprvodqqkshrfxmqedtaunfrprkpdgnjhrzipvikcnbjlskbwvkgmfcckdnzxvzcykzzfdpnzmenqblihodlxtjblsvibbjjsvwgizsgoactbtsmrdicosgodqguahvxbwjuyuqpipugxfbhppljwfaxwegmzpjfqlmltakllhiwohwryirtelmjxinqramorhvlxcgisralgwwikmnqqservajglvgqlhwlqbjyvuhktzitkddlwlqdfpwgsjnjsqcoxpppuxmlqveeztyedksbjummbovzzdqepmacmkdtwluomdltxctojjipziszwnefmodauuwzfsbhoukttbxnbblvdknjnqktvihtkpcqecxampjvvgwmkmclozwfpiceriplnywkyyvzhxtgqubusivpsocsrcwicvonidusiaghgvowwylhaxdszsaopfpttxcjrbghgqgpekwaukrejbtgaehcinglkeairlzyzuqxqrosgcocrdbbmyyxprzavpndyyrwusrlfkibnfthkzigbqczkhvbuojzhbjqqxueuliejpbhvewmlwxkojduklksndhhgyuceyghvqhorvslznhodsduokbkomvvqpsyqhcldvieafqrpsbtvqivypjynqmxvwojcpgdaurxdjedfdmkpnusibeqibglfiyituxzfenfhaxjxdioyxodebkpbcxizizeqjyeqnwohpmnfzclxojnlgjsnoretfpiuahgoyaenjxehkvstoyafuepmtftrngfihlvucfrvjggoxrxixknuzrqgpxeedszbrcemxwrtylkvywegjydmpxvtmpnkjusifgfuozwyttuvhafbpadghligebcndgtorgevkzoebjzfnrczvhdjpmhljntzrkjkcailyklzqbrqsbjgqkwgghzltiolfrbwjcgkgcggbsngricfjdtmxouujahqozpxgpqavpcdaowwuwnoxbmusgwjotxavyjowusgdaxtaxvadmwwucnhfpuefzgyvaqwmsovldnesgpuqkpncnkcbpljtxwtxigxuizozytwkytpgogcbyqkehfjzwxvpygqkahszxocdunhnvbebolgacykeilzcecbtwtoydpqgtadnszjjohwpmwcmiczuwbkyzfvmqfiptunyeblyrpllbfllaxpri"

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"

# s = "ab"

print(solver(s))