## rules and all the pieces 

# Every piece has a one hot kinda vector with a bit representing white and black
black_king = [1,0,0,0,0,0,1] # [Bl/Wh, P, R, B, Kn, Q, K]

#the board represents a matrix of 0s and [vectors], 0s are not occupied blocks and vectors are occupied

# maybe all 0s - [0,0,0,0,0,0,0] is an empty block

# Technically its pruning the search tree using Neural Nets
