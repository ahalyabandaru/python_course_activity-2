def remove_duplicates(str):
    s = set()
    for i in str:
        s.add(i)
    st = ""
    for i in s:
        st = st+i
    return st
 
str = "Ahalya"
print(remove_duplicates(list(str)))
