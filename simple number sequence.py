def missing(s):
    for j in range(1, len(s)//2):
        badsplit_num = ''.join([str(9) for i in range(j)])
        badsplit_nums = {badsplit_num:[str(int(badsplit_num)+1), str(int(badsplit_num)+2)], str(int(badsplit_num)-1):[str(int(badsplit_num)), str(int(badsplit_num)+1)], str(int(badsplit_num)+1):[str(int(badsplit_num)+2), str(int(badsplit_num)+3)]}
        for num in badsplit_nums.keys():
            split = [s[i:i+j] for i in range(0, len(s), j)]
            if num in split:
                a = split.index(num) + 1
                newsplit = [str(i) for i in split[a:]]
                newsplit = ''.join(newsplit)
                newsplit = [newsplit[i:i+j+1] for i in range(0, len(newsplit), j+1)]
                if newsplit:
                    if newsplit[0] in badsplit_nums[num]:
                        split = split[:a]
                        split.extend(newsplit)
                        break
        split = [int(i) for i in split]
        score = 0
        for i in range(len(split)-1):
            if split[i] != split[i+1]-1:
                score += 1
                save = split[i+1]-1 
        if score == 1:
            return save
        if score == 0:
            return -1
    return -1

s_list = ["123567","899091939495","9899101102","599600601602","8990919395","998999100010011003","99991000110002","979899100101102","900001900002900004900005900006"]

for s in s_list:
    print(missing(s))
