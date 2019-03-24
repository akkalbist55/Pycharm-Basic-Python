#First Program for coin flip in python
import random
import itertools

results = {
    'heads': 0,
    'tails': 0,
}
sides = list(results.keys())

for i in range(5):
    results[random.choice(sides)] += 1

print('Heads:', results['heads'])
print('Tails:', results['tails'])


#second way coin flip program
import random
def coinToss():
	head_count = 0;
	tail_count = 0;
	toss_count = 0;

	for x in range(1, 50):
		toss = round(random.random())
		if toss == 0:
			head_count += 1
			toss_count += 1
			print("AI-SIR-RUN#", toss_count , ": Toss-HEAD! -->" , head_count , "head(H)" , tail_count , "tail(T)")
		else:
			tail_count += 1
			toss_count += 1
			print("AI-SIR-RUN#", toss_count , ": Toss-TAIL! -->" , head_count , "head(H)" , tail_count , "tail(T)")

coinToss()


#Third way coin flip program
import random
coin = ('heads', 'tails')
heads, tails = 0, 0
games = 0
print('Hit x to exit')
while True:
    flip = random.choice(coin)
    your_choice = input('Type heads or tails')
    if your_choice == 'x' or your_choice == 'X':
        print("GAME OVER :(")
        print('Coin flipping stats:')
        print('Games played = {}'.format(games))
        print('heads = {}'.format(heads))
        print('tails = {}'.format(tails))
        break
    if your_choice == flip:
        print('Coin landed on {}. Yeah boi you win!'.
              format(flip))
        games += 1
    else:
        print("Uh oh. Coin landed on {}. Better luck next "
              "time".format(flip))
        games += 1
    if flip == 'heads':
        heads += 1
    elif flip == 'tails':
        tails += 1