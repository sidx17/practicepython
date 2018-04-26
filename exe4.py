import re
def checkpalin(str):
    pattern=r"[^a-zA-Z0-9]"
    nstr=re.sub(pattern,"",str)
    nstr=nstr.lower()
    str_list=list(nstr)
    str_list.reverse()
    nstr_rev="".join(str_list)
    if(nstr==nstr_rev):
        return True
    else:
        return False

print(checkpalin("rac@ e(*car))"))