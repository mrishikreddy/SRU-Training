death = [(1,0),(3,0),(4,1),(2,4)]

def find_path(i,j):
    if i==5-1 and j==5-1:
        return 1
    elif (i >= 5 or j >= 5):
        return 0
    for box in death:
        if i==box[0] and j==box[1]:
            return 0
    return find_path(i,j+1) + find_path(i+1,j)

print("The number of possible paths are: ", find_path(1,2))