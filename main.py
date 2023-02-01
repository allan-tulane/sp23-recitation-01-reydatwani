"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1

def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
	### TODO
  middle = (left + right) // 2
  if (left > right):
    return -1
  if (mylist[middle] == key):
    return middle
  elif (mylist[middle] > key):
    return _binary_search(mylist, key, left, middle - 1)
  else:
    return _binary_search(mylist, key, middle + 1, right)
	###

def test_binary_search():
  assert binary_search([1,2,3,4,5], 5) == 4
  assert binary_search([1,2,3,4,5], 1) == 0
  assert binary_search([1,2,3,4,5], 6) == -1
  assert binary_search([1,2,3,4,5], 4) == 3
  assert binary_search([1,2,3,4,5], 7) == -1


def time_search(search_fn, mylist, key):
	### TODO
  start = time.time()
  search_fn(mylist, key)
  end = time.time()
  return (end - start) * 1000
	###

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	### TODO
  results = []
  for n in [int(x) for x in sizes]:
    linear_time = time_search(linear_search, range(n), -1)
    binary_time = time_search(binary_search, range(n), -1)
    results.append([n, linear_time, binary_time])
  return results
	###

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1

print_results(compare_search())