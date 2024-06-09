def subseq(s):
    output = []
    if len(s) == 0:
        output.append("")
        return output
    
    smallerOutput = subseq(s[1:])

    for subs in smallerOutput:
        output.append(subs)

    for subs in smallerOutput:
        output.append(s[0] + subs)
    
    return output

print(subseq("abc"))