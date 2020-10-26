import conf
import sheets
import random
import time
from joblib import Parallel, delayed

def uniform():
    return random.random()

def copy_list(l):
    return list[:]

def random_votes():
    return [uniform() for _ in range(conf.N_STATES)]

def change_1_vote(l):
    c = random.randrange(conf.N_STATES)
    return [uniform() if i == c else x for i, x in enumerate(l)]

def radicalize(l):
    return [
        x ** (uniform() * .5) if x >= .5 else x ** (uniform() * 2)
        for x in l
    ]

def moderatize(l):
    return [
        x ** (uniform() * 2) if x >= .5 else x ** (uniform() * .5) 
        for x in l
    ]

def jitter(l):
    return [max(0.0, min(1.0, x + (.01 * uniform()))) for x in l]

def offspring(S1):
    S2 = random.sample(S1, k = len(S1))
    return [
        [
            x1 if uniform() >= .5 else x2
            for x1, x2 in zip(s1, s2)
        ] for s1, s2 in zip(S1, S2)
    ]


def gen_new_solutions(solution):
    return [
        solution,
        random_votes(),
        change_1_vote(solution),
        radicalize(solution),
        moderatize(solution),
        jitter(solution)
    ]

def find_winner(ec, pop):
    def f(votes):
        vote_tally = 0
        plus_pop = 0
        minus_pop = 0

        for v, e, p in zip(votes, ec, pop):
            plus_pop += v * p
            minus_pop += (1 - v) * p

            if v >= .5:
                vote_tally += e
            else:
                vote_tally -= e

        return vote_tally, plus_pop, minus_pop
    return f

def score(vote_tally, plus_pop, minus_pop):
    if vote_tally == 0:
        return min(plus_pop, minus_pop) / total_pop
    elif vote_tally > 0:
        return plus_pop / total_pop
    elif vote_tally < 0:
        return minus_pop / total_pop
    else:
        raise Exception("OnNo.jpg")

def unbounded(S):
    return [y for s in S for y in s if not (0.0 <= y <= 1.0)]

def is_winner(vote, vote_tally, plus_pop, minus_pop):
    plus_voter = vote >= .5
    plus_won = vote_tally > 0 or (vote_tally == 0 and plus_pop < minus_pop)

    return plus_voter == plus_won


if __name__ == '__main__':
    merged = sheets.read_google_sheet(conf.G_SHEET_KEY, 'Joined')
    print(merged)
    
    ec = merged['Unnamed: 2'].tolist()
    total_votes = sum(ec)

    # pop = [int(x.replace(',', '')) + 1 for x in merged['2019'].tolist()]
    pop = merged['Registered'].astype(int).tolist()
    total_pop = sum(pop)
    
    names = merged['State'].tolist()

    f_win = find_winner(ec, pop)

    S = [random_votes() for _ in range(conf.N_SOLUTIONS)]

    while True:
        t_start = time.time()

        s_stacked = Parallel(n_jobs=-1)(delayed(gen_new_solutions)(x) for x in S)
        s_flat = [y for x in s_stacked for y in x]
        s_all = s_flat + offspring(s_flat)
        
        ub = unbounded(s_all)
        if ub:
            raise Exception('Generated a bad solution')
            for u in ub:
                print(u)

        S = sorted(
            s_all,
            key=lambda x: score(*f_win(x))
        )[:conf.N_SOLUTIONS]

        t_stop = time.time()

        winning_votes = S[0]
        vote_tally, plus_pop, minus_pop = f_win(winning_votes)
        winning_score = score(vote_tally, plus_pop, minus_pop) * 100
        winning_pop = min(plus_pop, minus_pop)

        winners = []
        losers = []
        winning_ec = 0
        for s, v, e, p in zip(names, winning_votes, ec, pop):
            if is_winner(v, vote_tally, plus_pop, minus_pop):
                winners.append([s, v, e, p])
                winning_ec += e
            else:
                losers.append([s, v, e, p])

        print('{} / {} ~= {:0.2f}% of the population with {} EC votes, {:0.2f} seconds'.format(
            int(winning_pop), total_pop, winning_score, winning_ec, t_stop - t_start
        ))
        print("WINNERS:")
        for w in sorted(winners, key=lambda x: x[0]):
            print(w)

        print("LOSERS:")
        for l in sorted(losers, key=lambda x: x[0]):
            print(l)


        print()

