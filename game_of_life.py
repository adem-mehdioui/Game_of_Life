import numpy as np




frame   =  np.array([[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]])


def compute_number_neighbors(paded_frame, index_line, index_column):

    number_neighbors=0

    for line in range(index_line-1, index_line+2):
       for column in range (index_column-1, index_column+2):
         
         if line == index_line and column == index_column:
                continue  # Skip the central element
         
         if(paded_frame[line,column] == 1):
           number_neighbors += 1

        

    return number_neighbors



def compute_next_frame(frame):

    #etape 1 : on calcule la matrice avec bordure

    paded_frame = np.pad(frame, 1, mode='constant')

    #get dimensions of the frame
    
    num_rows, num_columns = frame.shape


    alive_neighbors = 0  


    for i in range (0, num_rows):
        for j in range (0, num_columns):

            alive_neighbors = compute_number_neighbors(paded_frame, i, j)

            if paded_frame[i, j] == 0:

                if alive_neighbors == 3:
                    frame[i, j] = 1
            else:

                if alive_neighbors == 2 or alive_neighbors == 3:
                    frame[i, j] = 0
                    


    return frame




while True:

    print("###########\n",frame)
    frame = compute_next_frame(frame)





       














