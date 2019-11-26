def compact(seq):
    i=0
    while i < len(seq)-1:        
        if (seq[i] == seq[i+1]):
            seq.pop(seq[i])
        else:
            i=i+1    
    return seq

print(compact([1,1,1]))
print(compact([1,1,2,2,3,2]))
print(compact([]))
