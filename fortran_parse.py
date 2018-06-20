from sys import argv

def removejunk(txtfile):
    with open(file_path, 'r') as f:
        for x in f.readlines():
            x = x.strip().split(' ')[2:]
            yield ''.join(a for a in x)

def get_dictonary(templist):
    result = {}
    for x in templist:
        y = x.split(',')
        result.setdefault(y[0], [])
        result[y[0]].append(y[-1])
    return result

def consecutive(nums):
    nums    = list(set(nums))
    ranges  = sum((list(t) for t in zip(nums, nums[1:]) if t[0]+1 != t[1]), [])
    iranges = iter(nums[0:1] + ranges + nums[-1:])
    return ', '.join([str(n) + '-' + str(next(iranges)) for n in iranges])

def getsummary(inptxt):
    andindex  = None
    thentxt   = []
    truelist  = []
    falselist = []
    try:
        andindex  = inptxt.index('AND')
    except: pass

    for t in range(inptxt.index('THEN') + 1, inptxt.index('STOP')):
        thentxt.append(inptxt[t].lower())

    if not andindex:
        for i in range(inptxt.index('IF') + 1, inptxt.index('THEN')):
            if inptxt[i].startswith('-'):
                falselist.append(inptxt[i].lower().strip('-'))
            else:
                truelist.append(inptxt[i].lower())
        if not falselist:
            true_result  = get_dictonary(truelist)
            keyword_true = ''
            for k, v in true_result.items():
                keyword_true = keyword_true +'('+ k +'('+ ', '.join(x for x in v) +')),'

            return 'if {} then ({})'.format(
                keyword_true.strip(','),
                ', '.join(a for a in thentxt)
            )
        else:
            false_result  = get_dictonary(falselist)
            true_result   = get_dictonary(truelist)
            keyword_true  = ''
            keyword_false = ''

            for k, v in true_result.items():
                keyword_true = keyword_true +'('+ k +'('+ ', '.join(x for x in v) +')),'

            for k, v in false_result.items():
                keyword_false = keyword_false +'('+ k +'('+ ', '.join(x for x in v) +')),'

            return 'if {} (not {}) then ({})'.format(
                keyword_true.strip(','), keyword_false.strip(','),
                ', '.join(a for a in thentxt)
            )
    else:
        before_and_false = []
        before_and_true  = []
        after_and_false  = []
        after_and_true   = []
        for i in range(inptxt.index('IF') + 1, inptxt.index('AND')):
            if inptxt[i].startswith('-'):
                before_and_false.append(inptxt[i].lower().strip('-'))
            else:
                before_and_true.append(inptxt[i].lower())
        for i in range(inptxt.index('AND') + 1, inptxt.index('THEN')):
            if inptxt[i].startswith('-'):
                after_and_false.append(inptxt[i].lower().strip('-'))
            else:
                after_and_true.append(inptxt[i].lower())
        if not before_and_false and not after_and_false:
            true_before_and = get_dictonary(before_and_true)
            true_after_and  = get_dictonary(after_and_true)

            keyword_true_before_and = ''
            keyword_true_after_and  = ''

            for k, v in true_before_and.items():
                keyword_true_before_and = keyword_true_before_and +'('+ k +'('+ consecutive([int(x.strip('+').strip("'")) for x in v]) +')),'

            for k, v in true_after_and.items():
                keyword_true_after_and = keyword_true_after_and +'('+ k +'('+ consecutive([int(x.strip('+').strip("'")) for x in v]) +')),'

            return 'if {} AND {} then ({})'.format(
                keyword_true_before_and.strip(','),
                keyword_true_after_and.strip(','),
                ', '.join(a for a in thentxt)
            )

        elif not before_and_false and after_and_false:
            true_before_and = get_dictonary(before_and_true)
            true_after_and  = get_dictonary(after_and_true)
            false_after_and = get_dictonary(after_and_false)

            keyword_true_before_and = ''
            keyword_true_after_and  = ''
            keyword_false_after_and = ''

            for k, v in true_before_and.items():
                keyword_true_before_and = keyword_true_before_and +'('+ k +'('+ ', '.join(x for x in v) +')),'

            for k, v in true_after_and.items():
                keyword_true_after_and = keyword_true_after_and +'('+ k +'('+ ', '.join(x for x in v) +')),'

            for k, v in false_after_and.items():
                keyword_false_after_and = keyword_false_after_and + '(' + k + '(' + ', '.join(x for x in v) + ')),'

            return 'if {} AND {} (not {}) then ({})'.format(
                keyword_true_before_and.strip(','),
                keyword_true_after_and.strip(','),
                keyword_false_after_and.strip(','),
                ', '.join(a for a in thentxt)
            )
        elif before_and_false and not after_and_false:
            true_before_and = get_dictonary(before_and_true)
            true_after_and  = get_dictonary(after_and_true)
            false_before_and = get_dictonary(before_and_false)

            keyword_true_before_and  = ''
            keyword_true_after_and   = ''
            keyword_false_before_and = ''

            for k, v in true_before_and.items():
                keyword_true_before_and = keyword_true_before_and +'('+ k +'('+ ', '.join(x for x in v) +')),'

            for k, v in true_after_and.items():
                keyword_true_after_and = keyword_true_after_and +'('+ k +'('+ ', '.join(x for x in v) +')),'

            for k, v in false_before_and.items():
                keyword_false_before_and = keyword_false_before_and + '(' + k + '(' + ', '.join(x for x in v) + ')),'


            return 'if {} (not {}) AND {} then ({})'.format(
                keyword_true_before_and.strip(','),
                keyword_false_before_and.strip(','),
                keyword_true_after_and.strip(','),
                ', '.join(a for a in thentxt)
            )
        else:
            true_before_and  = get_dictonary(before_and_true)
            true_after_and   = get_dictonary(after_and_true)
            false_before_and = get_dictonary(before_and_false)
            false_after_and  = get_dictonary(after_and_false)

            keyword_true_before_and  = ''
            keyword_true_after_and   = ''
            keyword_false_before_and = ''
            keyword_false_after_and  = ''

            for k, v in true_before_and.items():
                keyword_true_before_and = keyword_true_before_and +'('+ k +'('+ ', '.join(x for x in v) +')),'

            for k, v in true_after_and.items():
                keyword_true_after_and = keyword_true_after_and +'('+ k +'('+ ', '.join(x for x in v) +')),'

            for k, v in false_before_and.items():
                keyword_false_before_and = keyword_false_before_and + '(' + k + '(' + ', '.join(x for x in v) + ')),'

            for k, v in false_after_and.items():
                keyword_false_after_and = keyword_false_after_and + '(' + k + '(' + ', '.join(x for x in v) + ')),'

            return 'if {} (not {}) AND {} (not {}) then ({})'.format(
                keyword_true_before_and.strip(','),
                keyword_false_before_and.strip(','),
                keyword_true_after_and.strip(','),
                keyword_false_after_and.strip(','),
                ', '.join(a for a in thentxt)
            )

if __name__ == '__main__':
    if len(argv) < 2:
        raise RuntimeError('USAGE:python3 parse.py path/to/file')
    file_path = argv[1]
    inptxt = removejunk(file_path)
    inptxt = [t.strip() for t in inptxt]
    result = getsummary(inptxt)
    print(result)
