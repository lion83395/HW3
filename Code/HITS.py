from time import time

def initialize_authority(pages):
    
    return dict(zip(pages.keys(), [1]*len(pages)))

def clean_pages(pages):
    
    for page in pages:
        outside_links = []
        for i in range(len(pages[page])):
            if pages[page][i] not in pages or pages[page][i] == page: outside_links.append(i)
        outside_links.reverse()
        for outside_link in outside_links:
            pages[page].pop(outside_link)
    return pages
                
def initialize_L_matrices(pages):
    
    L_matrix = pages
    Lt_matrix = {}
    for page in pages:
        Lt_matrix[page] = []
    for page in pages:
        for link in pages[page]:
            Lt_matrix[link].append(page)
    return L_matrix, Lt_matrix

def multiply_matrix_vector(matrix, vector):
    
    result_matrix = {}
    for row in matrix:
        result_matrix[row] = 0
        for item in matrix[row]:
            result_matrix[row] += vector[item]
    return result_matrix        

def normalize(vector):
    
    max = 0
    for component in vector:
        if vector[component] > max:
            max = vector[component]
    if max == 0:
        return vector
    for component in vector:
        vector[component] = float(vector[component]) / max
    return vector
        
def vector_difference(vector1, vector2):
    
    if not (vector1 and vector2): return float("inf")
    total = 0
    for component in vector1:
        total += abs(vector1[component] - vector2[component])
    return total        

def HITS(pages):
    
    pages = clean_pages(pages) 
    authority_old = None
    authority = initialize_authority(pages)
    (L_matrix, Lt_matrix) = initialize_L_matrices(pages)
    while vector_difference(authority_old, authority) > 0.1:
        authority_old = authority
        hubbiness = normalize(multiply_matrix_vector(L_matrix, authority))
        authority = normalize(multiply_matrix_vector(Lt_matrix, hubbiness))
    return authority, hubbiness

def main():
    # read in data
    hubs = {}
    auths = {}
    # initial score
    hub_scores = {}
    auth_scores = {}
    fo=open("graph_1.txt","r")
    line=fo.readline()
    while line:
        line_array = line.split(",")
        line_array = [int(i) for i in line_array]
        
        if line_array[0] in hubs:
            hubs[line_array[0]].append(line_array[1])
        else:
            hubs[line_array[0]] = [line_array[1]]

        hub_scores[line_array[0]] = 1

        if line_array[1] in auths:
            auths[line_array[1]].append(line_array[0])
        else:
            auths[line_array[1]] = [line_array[0]]

        auth_scores[line_array[1]] = 1

        try:
            line = fo.readline()
        except:
            break
    
    (authority, hubbiness) = HITS(hubs)
    print ("Authority:"  + str(authority))
    print ("Hubbiness: " + str(hubbiness))
   
if __name__ == "__main__":
    begin = time() 
    main()
    end = time()
    print ('total time is %f' % (end - begin))