def cw(text): #capitalize words
    return text.upper()
def rs(text): #reverse string
    return text[::-1]
def cc(text): #character count
    return len(text)-text.count(" ")
def wc(text): #word count
    return len(text.split())