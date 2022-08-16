STACK-EMPTY(S):
    if S.topo == 0
        return TRUE
    else:
        return FALSE

PUSH(S,x):
    S.topo = S.topo + 1
    S[S.topo] = x
POP (S):
    if STACK-EMPTY(S):
        error underflow
    else:
        S.topo = S.topo - 1
        return S[S.topo+1]