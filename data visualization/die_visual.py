from die import Die
import pygal

# create D6
die_1 = Die()
die_2 = Die(10)

# roll die, save results in a list
results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analysis result
frequencies = []
max_resulets = die_1.num_sides + die_2.num_sides
for value in range(1, max_resulets+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# visual results
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
hist.x_lables = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')
