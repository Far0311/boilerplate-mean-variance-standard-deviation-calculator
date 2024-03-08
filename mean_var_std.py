import numpy as np

def calculate(list):
     if len(list) == 9: #check if the list has 9 elements
        nparray = np.array(list) #converts list into numpy array
        array = nparray.reshape(3, 3) #converts 1x9 array to 3x3 array

        calculations = {
            'mean': [np.mean(array, axis = 0).tolist(), #mean of of elements by column
                    np.mean(array, axis = 1).tolist(), #mean of elements by row
                    np.mean(array)], #mean of all elements
            
            'variance': [np.var(array, axis = 0).tolist(), #var of of elements by column
                    np.var(array, axis = 1).tolist(), #var of elements by row
                    np.var(array.flatten())], #var of all elements
            
            'standard deviation': [np.std(array, axis = 0).tolist(), #std of of elements by column
                    np.std(array, axis = 1).tolist(), #std of elements by row
                    np.std(array.flatten())], #std of all elements

            'max': [np.max(array, axis = 0).tolist(), #max of of elements by column
                    np.max(array, axis = 1).tolist(), #max of elements by row
                    np.max(array.flatten())], #max of all elements

            'min': [np.min(array, axis = 0).tolist(), #min of of elements by column
                    np.min(array, axis = 1).tolist(), #min of elements by row
                    np.min(array.flatten())], #min of all elements

            'sum': [np.sum(array, axis = 0).tolist(), #sum of of elements by column
                    np.sum(array, axis = 1).tolist(), #sum of elements by row
                    np.sum(array.flatten())] #sum of all elements
        }
    else: 
        raise ValueError('List must contain nine numbers.')

    return calculations