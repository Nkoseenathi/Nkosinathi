import solver_mod

def  solvable(S):

    if solver_mod.is_win(S):
        solvable_mod.print_state(S)
        return True 

    else:
        n=solver_mod.find_space(S)

        if solver_mod.is_frog(S,n-1)==True:
            solver_mod.move(S, n-1)
            return solvable(S)
            
        if solver_mod.is_frog(S, n-2):
            move(S, n-2)
            return solvable(S)
            
        if solver_mod.is_toad(S, n+1)==True:
            solver_mod.move(S, n-2)
            return solvable(S)
            
        if solver_mod.is_toad(S, n+2):
            solver_mod.move(S, n+2)
            return solvable(S)
        
        else:return False
            