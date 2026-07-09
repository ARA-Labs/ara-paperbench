I got loss 6.1 after 3 hours of baselining (included implementing loss function)

Unigrams get 7.58 loss

bibigram got 5.75 cheating, 5.83 non cheating

conv1d got 5.25



conv1d + bigrams got 4.6 loss

gpt-2 small approximation with 20 approximation steps got 2.3 "mfu" based on a100 running on h100. 
a smaller gpt-2 configuration got 1.88 "mfu" vs 43.9 "mfu" without approximations, or 23x slowdown

Concerningly, loss didn't go down in the approximated version over that time

baseline score is 7.636
Baseline solution is a fully connected MLP that is very bad, doesn't perform better than unigrams

a concern: I have thought about limited architecture primitives stuff unusually much from the polynomials work at redwood research, and therefore are underestimating its difficulty