# Computes an approximation of Pi by summing up
# a series of terms.  The more terms, the closer
# the approximation.
# Based on a variation of the Gregory-Leibniz series approximation
import threading
import concurrent.futures

def funct( x ):
    """
    The function being integrated, and which returns
    an approximation of Pi when summed up over an interval
    of integers.
    """
    return 4.0 / ( 1 + x*x )

def main():
    """
    Gets a number of terms from the user, then sums
    up the series and prints the resulting sum, which
    should approximate Pi.
    """

    # get the number of terms
    N = int( input( "> " ) )

    sum = 0.0          # where we sum up the individual
                       # intervals
    deltaX = 1.0 / N   # the interval
    
    def with_threads(deltaX, N, sum):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = [executor.submit(funct,i*deltaX) for i in range(N)]
            for f in concurrent.futures.as_completed(results):
                sum += f.result()

    # display results
    print( "sum = %1.9f" % ( sum * deltaX ) )

main()