import numpy as np




def time1(elo_table):
    initial_pairs = []
    assert(len(elo_table) % 4 == 0)
    for i in range(0, len(elo_table), 2):
        initial_pairs.append([elo_table[i], elo_table[i+1]])
    
    n_courts = len(elo_table) // 4
    court_assignments = []
    initial_pairs_indices = np.arange(len(initial_pairs)).tolist()
    
    for i in range(n_courts):
        chosen_pairs = np.random.choice(initial_pairs_indices, 2, replace = False)
        for p in chosen_pairs:
            idx = initial_pairs_indices.index(p)
            initial_pairs_indices.pop(idx)
        
        chosen_members = [*initial_pairs[chosen_pairs[0]], *initial_pairs[chosen_pairs[1]]]
        court_assignments.append( chosen_members )
        
    ### we can add constraints here and if it doesn't satisfy just keep on rerunning until we have something.
        
    return court_assignments



def time2(elo_table):
    ### 1. divide into group of 8.
    ### 2. pick 4 and 4 from each group
    ### assumption, we always assume the length of elo_table is divisible by 4 because we need 4 people to do doubles.
    ### if len(elo_table) % 4 == 0 and len(elo_table) % 8 != 0, then we just group last 4 people in elo table as one group and be done with.
    final_groups = []
    group_size = 8
    assert(len(elo_table) % 4 == 0)
    if len(elo_table) % group_size != 0:
        ## we cut off last 4
        final_groups.append(elo_table[-4:])
        elo_table = elo_table[:-4]
    
    initial_groups = []
    n_groups = len(elo_table) // group_size
    for i in range(n_groups):
        initial_groups.append(elo_table[i*group_size:i*group_size+group_size])
        
    for group in initial_groups:
        ## pick 4
        chosen = np.random.choice(group, 4, replace = False).tolist()
        ### append the non chosen 4
        non_chosen = []
        for g in group:
            if g not in chosen: non_chosen.append(g)
            
        
        final_groups.append( chosen )
        final_groups.append( non_chosen )
        
        
        
    ### add final conditions if needed and then just while loop the whole thing until condition is satisfied.
    return final_groups


if __name__ == "__main__":
    elo_table = ['a', 'b', 'c', 'd', 
                 'e', 'f', 'g', 'h', 
                 'i', 'j', 'k', 'l', 
                 'm', 'n', 'o', 'p', 
                 'q', 'r', 's', 't', 
                 'u', 'v', 'w', 'x', 
                 'y', 'z', 'aa', 'bb']
    result = time1(elo_table)
    print(result)
    result2 = time2(elo_table)
    print('------')
    print(result2)


