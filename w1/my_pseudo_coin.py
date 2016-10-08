import numpy as np
import pandas as pd
# from random import shuffle


tableA = pd.read_excel( './coin_data/coin_data_a.xlsx', header=None )
tableB = pd.read_excel( './coin_data/coin_data_b.xlsx', header=None )
print tableA
print tableB

weights = [1, 2, 3]
misclassified = 1

# while misclassified :
for index, col in tableA.iterrows() :
  print "index: " + str( index )
  print "col: \n" + str( col )

  # vector = 0
  # for row in tableA[col] :
  #   print "row: " + str( row )
  #   row = int( row )
  #   vector = vector + weights[row] * coin.ix( row )

  # print vector
# misclassified = 0
    # if vector == y :

    # elif vector !== y :
    #   weights = weights - coin
      # start over from all the coins
