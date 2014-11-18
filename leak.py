import multiprocessing

def score4abc(a,b):
  score = a,b
  return score

def wrapper_score4multi(args):
  return score4abc(*args)

def main(a,foo):
    for i in range(500):
        pool = multiprocessing.Pool(32)
        pool.map(wrapper_score4multi,[[a,b] for b in foo])
        pool.close()

main(3, range(1, 100))
