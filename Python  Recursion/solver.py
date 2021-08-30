import solver_mod

def  solvable(S):
    print(S)
    solver_mod.print_state(S)
    print()

    if solver_mod.is_win(S):
        solver_mod.print_state(S)
        return True 

    else:
        n=solver_mod.find_space(S)
        
        if n-1>=0 and n-1<=len(S)-1:
            if solver_mod.is_frog(S,n-1)==True:
                solver_mod.move(S, n-1)
                return solvable(S)
            
        if n-2>=0 and n-2<=len(S)-1:   
            if solver_mod.is_frog(S, n-2):
                move(S, n-2)
                return solvable(S)
        
        if n>=0 and n+2<=len(S)-1:
            if solver_mod.is_toad(S, n+2)==True:
                solver_mod.move(S, n+2)
                return solvable(S)
            
        elif n>=0 and n+1<=len(S)-1:
            if solver_mod.is_toad(S, n+1):
                solver_mod.move(S, n+1)
                return solvable(S)
        
        else:return False
        
def main():
    lt=eval(input())
    print(lt)
main()