import coin_toss_p as p
import plotting as pl


a = p.run_experiment(num_flips=10, num_coins=1000, num_experiments=1000)
pl.show_results(results=a)
pl.show_bounds_vs_experiment(results=a, epsilon=0.3, u=0.5, times_coin_tossed=10)



