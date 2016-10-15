## Extending the Perceptron Algorithm

Our task now is to extend the perceptron algorithm to the case of data that is not fully linearly separable. We'll
call this algorithm the 'pocket' algorithm because we will always keep our best guess for the weights in our *pocket*.

Below is the core of the perceptron algorithm for reference

```python

# it is assumed that you have your correct classifications in 'y',
# the predictors in 'x' (plus the addition of a column of 1's),
# and the weights in w matching the length of x

misclassified = 1

while misclassified != 0:

    misclassified = 0

    # iterate through all the rows of x
    for index, row in x.iterrows():

        y_hat = np.dot(w, row.T, out=None)


        if np.sign(y[index]) != np.sign(y_hat):


            w = np.add(w, y[index]*row.values)

```

For the pocket algorithm we will be working with *hand written digit features*. That is we will be attempting to classify
hand written digits. We will focus on the two digits **1** and **5** to make the problem analogous to the binary classification
of the standard perceptron.

The zip file *pocket-starter.zip* contains a dataset that includes many examples of all the digits, and their corresponding features.
It's worth taking a second to emphasize the *central importance* of *features* to machine learning. What the data set
*digits_training_features.csv* represents is a distillation of all raw pixel data in the original images(say 256x256), into a vector
we'll call x, of the length 2. The 2 columns of x represent the intensity, and symmetry in each image.

Again, it is worth **really thinking hard** about how important this **feature extraction** is to the process of machine learning.

> "With the right features...we can conquer the world"....said somebody working in machine learning


### Plan of attack

To construct the pocket algorithm we will need to do a few things:

* Read in the file *digits_training_features.csv* using a Pandas DataFrame; into a variable named: *digits*
* Extract from *digits* only those rows corresponding to the digits *1* or *5*;into a variable named: *classification_targets*

Your code to do this extraction will look something like the following, where we reset the indexes of the new data frame

```python
# your code must extract rows where in column 0 are equal to '1' or '5'
classification_targets = digits[ "code goes here to index into column 0 and grab correct rows"].reset_index(drop=True)
```
* We then need to create our scalar column and add it to *classification_targets*
* Modify the perceptron to run for 250 iterations, as missclassified points no longer
makes sense as a flag(there will always be misclassified points)
* Each iteration check the weight vector against *all rows of x*, see how many are missclassified; did our w do better
than our last w? If so, keep this w in our pocket as the best so far.
* Print out how many misclassified points in total there are on each iteration so you can monitor the algorithms progress


