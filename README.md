# python_AlgorithmicComplexity

## Make sure your python Environment includes:

- numpy
- unittest
- timer
- matplotlib

## To test speed of functions:

- Add method names to list in Graph_Plotter file under
  `if __name__ == '__main__':`
- Set Upper range (max sized array to test)
- set increments (increase of number in array from one array to the next till upper range reached)
- Set limit (randomises each array point between 1 --> limit)
- Run:
  `$ python3 graph_plotter.py`
- Graph will pop up plotting the time taken for each method to complete action on range of array sizes specified above

### Information from Alice Lieutier

Look up DIVIDE AND CONQUER and recursive strategies
--> three stages to split problem into

1. TRIVIAL: If solution is trivial then return solution

2. DIVIDE: Else Divide input into Input 1, Input 2
   3)COMBINE: return combined(sol1, sol2)

Look up Quicksort and Mergesort (use divide and combine stages differently in sorting)

For shuffle: USE SWAP IN FUNCTION: Take first Item and swap with random integer, comb thru whole ARRAY
