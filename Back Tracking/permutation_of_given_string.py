"""
Coplexity analysis:
time: O(n*n!) --> n iterations --> for every (n-1)! permutations
we know, O((n-1)!) = O(n!)

T(N)= N *(O(1) +T(N-1)+ O(1)) = N * N-1 * N-2 * .....
B(N*N!) 
#considering the fact that prining string of length N will take N time so N * N!
"""
def permutate(a, l, r):
    if l == r:
        print(a)
    else:
        for i in range(l,r+1):
            a[i], a[l] = a[l], a[i]
            permutate(a,l+1,r)
            a[i], a[l] = a[l], a[i]


if __name__ == "__main__":
    test_str = 'ABC'
    test_list = list(test_str)
    permutate(test_list,0,len(test_list) -1 )
