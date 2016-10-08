from random import randint

# this function will return an 'h' or 't'
def flip_coin() :
    return randint( 0, 1 )
    # missing implementation of a function that has a 50/50 chance of
    # returning an 'h' for heads or a 't' for tails

# this function takes 3 inputs, and returns a results array containing structures representin
# v1, v_rand, and v_min
def run_experiment(num_flips,
                   num_coins,
                   num_experiments) :
    results = []
    for experiments in range( num_experiments ) :
        head_count_coins = []
    #missing outer loop for how many experiments we will conduct
        for coin in range(num_coins) :
            flips = [flip_coin() for i in range(num_flips)]
            head_count = sum( flips )
            head_percentage = sum( flips ) / float( num_flips )
            # missing count variable of the number of heads, how do we get the percent heads in 'flips'?
            head_count_coins.append( head_count )
            # head_count_coins.append( head_percentage )

        results.append({'v1': head_count_coins[0], # 'v1' represents picking the first coin
                        'v_rand': head_count_coins[randint(0, num_coins - 1)],
                        # missing variable 'v_rand' that represents picking a random coin
                        'v_min': min( head_count_coins )
                        # missing  variable'v_min' that represents picking the coin with the lowest distribution of heads
                        })
        head_count_coins = []

    return len( results )

print(run_experiment(10,1000,1000))
