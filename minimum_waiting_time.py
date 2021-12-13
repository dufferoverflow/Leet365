"""""

I am given an array of positive integers, where each integer represents the duration of a query that needs to be executed. 
Only one query can be executed at a time, but the queries can be executed in any order. 
I am asked to write a function that returns the minimum amount of total waiting time for all of the queries, and I am allowed to mutate the input array.

Suppose the input array is going to be [1, 3, 2]. The first query can be executed immediately, therefore the waiting time of the first query is 0. T
he second query have to wait until the first one finishes before it can execute, so the waiting time of the second query is going to be 1 second, the duration of the first query. 
The third query has to wait for both the first query and the second query to finish executing before it can start. 
Since the second query takes 3 seconds to execute, the waiting time of the third query is going to be 1 + 3 seconds. 

So if the queries are executed in that order, then the total awaiting time for all of the queries is going to be (0) + (1) + (1 + 3) = 5.

"""""


def minimumWaitingTime(queries):
    queries.sort() #fastest way to sort is always O(nlogn)
	
	total_wait = 0 
	for idx, duration in enumerate(queries):
		queries_left = len(queries) - (idx+1)
		total_wait += duration * queries_left
    return total_wait

