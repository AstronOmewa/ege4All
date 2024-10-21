def game(s=1,m=1,operand='>=',mn=1,steps=[],errors=False):
    if eval(f'{s}{operand}{mn}'): return m%2==0
    if m < 0: return 0

    h = [game(eval(f'{s}{step}'),m-1,operand,mn,steps,errors) for step in steps]

    if (m-1)%2==0: return any(h)
    else: return all(h) if not errors else any(h)

    
print([s for s in range(1,14) if game(s,1,'<=',14,['+1','*2'],False)])