input_list = open("input.txt", "r").readlines()

def find_chars(datastream, distinct_chars):
    last_seen = []
    counter = 0
    for i in datastream:
        counter += 1
        last_seen.append(i)
        if counter >= distinct_chars:
            dic = {}    
            for k in last_seen:
                if k in dic.keys():
                    break
                else:
                    dic[k] = 1
            last_seen.pop(0)            
            if len(dic.keys()) == distinct_chars:
                return counter

print(find_chars(str(input_list[0]), 4))