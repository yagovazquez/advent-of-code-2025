def merge(word1, word2):
    
    len1, len2 = len(word1), len(word2)
    large = min(len1,len2)       
    result = [None]*(large*2)

    for i in range(large*2):
        if (i % 2) == 0:
            result[i] = word1[i//2]
        else:
            result[i] = word2[(i+1)//2 - 1]
    
    if len2>len1:
        result.append(word2[large::])
    else:
        result.append(word1[large::])
        
    return ''.join(result)
