# import statements go below
import pandas as pd
import numpy as np
# import pocket_plot as pl

# read in the digits data from 'digits_training_features.csv'
digits = pd.read_csv( "digits_training_features.csv", header=None )

# we actually only want to do binary classification at this stage
# so we'll take only the rows from digits that correspond
# to '1' or '5'(these values are in column 0, and represent our 'y')
digits[[0]].astype(int)
classification_targets = digits[digits.loc[:, 0].isin([1, 5])].reset_index(drop=True)

# this will allow us to match the three columns our weight vector will have
scalar = pd.Series([1] * len(classification_targets), name='scalar')

# create our x vector with the added scalar column by concatenation,
x = pd.concat( [scalar, classification_targets], axis=1 )

# the first column of classification_targets are the actual numeric digits themselves
y = classification_targets.loc[:, 0]

# we have a problem...our 'y' is currently either '1' or '5', not '1' or '-1' that we need
# we must remedy that situation by converting this columns values to the '1' or '-1' that we need
y = y.apply( lambda digit: -1 if digit == 5 else digit )

# set the weight values to an initial random value, along with 'w_save' which is the weight vector
# representing
w = w_save = pd.DataFrame(np.random.randn(1, x.shape[1]))

# what follows should be the pocket algorithm, use the perceptron as a guide but think
# carefully about the modifications that will be needed for it to function correctly

# initialize a flag to tell us whether or not we have a missclassified point
misclassified = 1
while misclassified != 0 :
    misclassified = 0

    # iterate through all the rows of x
    for index, row in x.iterrows() :

        # [1, 2, 3].T  => [ 1,
        #                   2,
        #                   3,]
        y_hat = np.dot( w, row.T, out=None )

        # here we will check that the signs of our actual data(in 'y') match the result
        # of our multiplication of the weight vector 'w' and our row, which is a row from 'x' our
        # data set.
        if np.sign( y[index] ) != np.sign( y_hat ) :
            # we adjust our weight vector 'w' by adding the result of y[index]*row to 'w'
            w = np.add( w, y[index]*row.values )
            # keep track of how many points are missclassified
            misclassified += 1

print w

pl.pla_plot( w )
