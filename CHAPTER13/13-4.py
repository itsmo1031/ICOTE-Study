# Q18 괄호 변환

def balancing(bracket):
    if bracket == '':
        return bracket
    i = balanced_index(bracket)
    u = bracket[:i + 1]
    v = bracket[i + 1:]
    if is_balanced(u):
        balanced = u + balancing(v)
    else:
        tmp_str = '(' + balancing(v) + ')'
        u = u[1:-1]
        tmp_u = ''
        for nu in u:
            if nu == '(':
                tmp_u += ')'
            else:
                tmp_u += '('
        balanced = tmp_str + tmp_u
    return balanced


def balanced_index(bracket):
    cnt = 0
    for i in range(len(bracket)):
        if bracket[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i


def is_balanced(bracket):
    cnt = 0
    for b in bracket:
        if b == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True


def solution(p):
    return balancing(p)
