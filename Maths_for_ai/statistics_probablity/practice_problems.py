#q1 mean, median , mode
data = [12, 15, 12, 18, 20, 15, 15]
def mean(data):
    return sum(data)/ len(data)
def median(data):
    sorted_data = sorted(data)
    mid = len(sorted_data) //2
    if len(sorted_data) % 2 ==0:
        return (sorted_data[mid-1] +sorted_data[mid]) / 2
    return sorted_data(mid)
def mode(data):
    counts = {}
    for value in data:
        if value in counts:
            counts[value] +=1
        else:
            counts[value] = 1
    max_count = max(counts.values())
    for value, count in counts.items():
        if count == max_count:
            return value    
#q2 standard deviation and variance
def variance(data):
    m = mean(data)
    squared_diffrences = [(x-m)**2 for x in data]
    return sum(squared_diffrences)/ len(data)
def std_dev(data):
    return variance(data) ** 0.5
print(f"mean: { mean(data)}")
print(f"median: {median(data)}")
print(f"mode: {mode(data)}")
print(f"variance: {variance(data)}")
print(f"standard deviation: {std_dev(data)}")
#q3 A bag has 5 red balls and 3 blue balls. What's the probability of picking a red ball? What's the probability of picking two red balls in a row without replacement
p_first_red = 5/8
p_second_red_after_first = 4/7
p_of_both_red = p_first_red * p_second_red_after_first
print(p_of_both_red)
#q4 Two coins, "at least one head"
p_no_head = 0.5*0.5
p_atleast_one_head = 1-p_no_head
print(p_atleast_one_head)
#q5 Bayes' theorem, the disease test (the important one)
p_disease = 0.01
p_positvie_given_disease = 0.95
p_positive = 0.0585
p_disease_given_positive = (p_positvie_given_disease *p_disease) /p_positive
print(p_disease_given_positive)