# example of program that calculates the median number of unique words per tweet.import collectionsimport sys# file handlinginput_file = sys.argv[1]out_file = sys.argv[2] words = collections.Counter()number = []# input_file = "./tweet_input/tweets.txt"def median(lst):    even = (0 if len(lst) % 2 else 1) + 1    half = (len(lst) - 1) / 2    return sum(sorted(lst)[half:half + even]) / float(even)def is_even(x):    return x % 2 == 0def avg(l):    return sum(l)/float(len(l)) if len(l) > 0 else float('nan')for line in open(input_file):    num = len(set(line.split()))    number.append( num )# print numbernth = len(number)# print output to filef = open(out_file, 'w')for i in range(1, nth):    ith_list = number[:i]    if is_even(len(ith_list)):        a = len(ith_list)/2        sorted_list = sorted(ith_list)[a-1:a+1]        y = avg(sorted_list)    else:        y = sorted(ith_list)[len(ith_list)//2]    f.write("{}\n".format(y))f.close()