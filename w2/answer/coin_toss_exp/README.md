### Coin Toss Experiment

Understanding the motivation for the experiment:

> Abu:

Take the coin flipping example, with each of 1000 fair coins flipped 10 times, Hoeffding applies to each coin, right?
Now if we pikc "g" to be the coin that produced the most heads, we lose the Hoeffding guarantee because the small probability
of bad behavior for each coin accumulates into a not-so small probability of bad behavior for **some** coin(which we picked
deliberately because it behaved badly)

> Student:

I sort of understand your example because we pick the run of coin flipping that produces most heads, and so if we plot
the graph, the graph indicates that Hoeffding inequality doesn't aply. But if Hoeffding inequality is talking about
probability and so the reality might be off a bit.

> Abu:

It's a subtle point. There is "cherry picking" if we fish for a sample that has certain properties after many trials, instead
of having a sample that is fairly drawn from a fixed hypothesis.

Statements involving probability are tricky because they don't guarantee a particular outcome, just the likelihood of getting
that outcome. Therefore, changing the game to allow more trials or different conditions would change the probabilities.

Let me rephrase it. Let's say(like in Hoeffding) that a rare event has probability of at most 1% of happening. If we
make repeated independent trials looking for that event, each trial still gives a probability of at most 1% for that
event to happen. Now, if we actively search for the case when that rare event actually happened among these many trials, we
will succeed in finding it with probability much more than 1%.


> student

In my understanding: g is the final hypothesis that is known after the data set is generated(because the choice of the final
hypothesis is based on the specific dataset). Before the data set is generated, all the information that we know about g
is that g is one of the hypotheses in H(hence the M). h is a specific hypothesis that is an element of H, and I don't
think that we are selecting h, I think we are selecting g instead.

look at this post: book.caltech.edu/bookforum/showthread.php?p=12031#post12031

Why is hoeffding inequality about >

If your epsilon is too stringent, or you do not have enough samples. For the hoeffding inequality to give a 'sensible'
answer, you either need more training samples, or you need a less stringent epsilon

> Magon:

The main point of the exercise is to realize that if you pick a coin carefully based on the data of the flips(in this case
"carefully" means having minimum number of heads), then the distribution of the number of heads you see will not be
what you would expect if you tossed that *same* coin again. If you tossed that c_min again, you would expect to see
a binomial distribution for heads. But the distribution of c_min is clearly not binomial.

Learning: If you pick a hypothesis "carefully", say having minimum Ein, then the Ein you get will not necessarily reflect
the distribution of errors you get when you "toss that hypothesis again" -- i.e test it on new data.

### Specifics of the exercise, part C:

Fix epsilon to say 0.1

Now run the experiment, and compute '|u-v|'. Repeat.
Some of the time, '|u-v|' > epsilon. Compute the fraction of the time that
|u-v| > epsilon. You now have a pair:
(epsilon = 0.1, fraction of time|u-v|> epsilon)
Repeat the whole process for epsilon = 0.2,0.3,....and plot the fraction versus epsilon


For each run of the experiment, calculate the [fraction of heads]-0.5(the actual 'u' distribution of heads)
Compute the fraction of the time |u-v| > epsilon.

So for each coin(say there are 1000 coins), flip the coin 10 times. You will have some number of heads for that particular
coin. Calculate 0.5 minus the fraction of heads for that coin(maybe its .3). If epsilon is .2, and u is .5, that coins \
distribution of heads is within epsilon of u (0.5-0.2=0.3). Do this for each coin. So for each coin we have a pair, epsilon,
and that coin with respect to epsilon

Grant > You are about to engage in a betting game against your friend for high stakes, since your both bosses, you insist on
rollin dice like the playaaaazzzz you are...yeeeah booii. Being a wise better, you insist on testing the dice in question, hoping
to gain an edge over your oponent. you insist on rolling the 10 competition dice 10 times each. Since you want to roll snake eyes,
You carefully observe  2 of the dice roll 1's 8 out of 10 times. those two happen to be red in color. You make a mental note that
these are the dice for you. You see, at the world championships of dice, you are allowed to select your two dice from
a draw of 10.

The question is: are you a genius or a fool? And....where exactly do you draw the line? What are the possibilities?
Let's examine the possibilities:

a) THe dice are fair, and you are clearly mad.

b) The dice are loaded, in which case you are clearly a genius (how does this play into the idea of bad data?)

c) We are a simulation being conducted by aliens existing in a mother universe, and they have set it up so that
you will roll these two dice in a specific way, setting in motion ripples in our child universe that will have ramifications
in the year 3035 when they return to reveal themselves and welcome us when we shall have reached technological parity.

All of these situations, are probable, but some are far less probable than others.

What you have done is essentially cherry picked your dice, thinking that the two you picked will perform well in the competition.
In the likely event that they were fair dice, they will **most likely** not perform to your liking in
the competition. you will walk out of the competition with nothing more than the clothes on your back.

###Exercise 1-- modify the code to roll dice instead of toss a coin.

