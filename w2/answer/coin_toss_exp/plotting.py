import math
import matplotlib.pyplot as plt

def show_results(results):
    '''
       fig.add_subplot: arg1 is the number of rows
                        arg2 is the number of columns
                        arg3 is the individual plots order

       fig_obj.hist:    arg1 is the data to plot
                        arg2 is the number of bins to group the data in,
                        best to calculate this explicitly based on the data
                        arg3 is the color you would like the plot to appear in
    '''
    fig = plt.figure()

    a = fig.add_subplot(311)
    v1 = [result['v1'] for result in results]
    a.hist(v1, bins=sorted(set(v1)), color='blue')
    a.set_xlim([0, 1])
    a.set_title("picking the first #heads result from each trial")

    b = fig.add_subplot(312)
    v_rand = [result['v_rand'] for result in results]
    b.hist(v_rand, bins=sorted(set(v_rand)),  color='red')
    b.set_xlim([0, 1])
    b.set_title("picking a random #heads result from each trial")

    c = fig.add_subplot(313)
    c.hist([result['v_min'] for result in results], color='green')
    c.set_xlim([0, 1])
    c.set_title("picking the minimum #heads result from each trial")

    plt.tight_layout()
    plt.show()

def show_prob_bounds(N):
    if len(N) != 3:
        raise Exception("pass a list or tuple for N of length 3")

    error_range = [x * .01 for x in range(1, 31)]

    fig = plt.figure()
    a = fig.add_subplot(311)

    a.plot(error_range, [2 * math.e ** (-2 * error_term ** 2 * N[0]) for error_term in error_range])
    a.set_title("N=" + str(N[0]))

    b = fig.add_subplot(312)
    b.plot(error_range, [2 * math.e ** (-2 * error_term ** 2 * N[1]) for error_term in error_range])
    b.set_title("N=" + str(N[1]))

    b = fig.add_subplot(313)
    b.plot(error_range, [2 * math.e ** (-2 * error_term ** 2 * N[2]) for error_term in error_range])
    b.set_title("N=" + str(N[2]))

    plt.tight_layout()


''' results is 10000 coins, each flipped 10 times, fraction of heads '''
def show_bounds_vs_experiment(results, epsilon, u, times_coin_tossed):

    hoeffding = 2 * math.e ** (-2 * (epsilon ** 2) * times_coin_tossed)
    fig = plt.figure()

    a = fig.add_subplot(311)
    v1_vs_u = [abs(fraction_heads["v1"] - u) for fraction_heads in results]
    a.plot(v1_vs_u)
    a.set_title("|v1 - u|")

    print("Probability bound given by Hoeffding inequality for N=" + str(times_coin_tossed) + ": " + str(hoeffding))
    print("Percentage of times |v1 - u| is greater than epsilon: " +
          # create list of results where: fraction of heads > epsilon
          # divide the length of that list(num of items) by the length of results to get a percentage
          # we need to type cast the length to float so that division gives a decimal, then cast the whole
          # expression to a string so that we can print it
          str(float(len([fraction for fraction in v1_vs_u if round(fraction, 1) > epsilon]))/len(results)))

    b = fig.add_subplot(312)
    v_rand_vs_u = [abs(fraction_heads["v_rand"] - u) for fraction_heads in results]
    b.plot(v_rand_vs_u)
    b.set_title("|v_rand - u|")

    print("Percentage of times |v_rand - u| is greater than epsilon: " +
          str(float(len([fraction for fraction in v_rand_vs_u if round(fraction, 1) > epsilon]))/len(results)))

    c = fig.add_subplot(313)
    v_min_vs_u = [abs(fraction_heads["v_min"] - u) for fraction_heads in results]
    c.plot(v_min_vs_u)
    c.set_title("difference between epsilon and v_rand-u")

    print("Percentage of times |v_min - u| is greater than epsilon: " +
          str(float(len([fraction for fraction in v_min_vs_u if round(fraction, 1) > epsilon])) / len(results)))

    plt.tight_layout()
    plt.show()
