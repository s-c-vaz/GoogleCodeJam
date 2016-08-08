if __name__ == '__main__':
    
    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):

        k = int(raw_input())
        tickets = {}
        for i in range(k):
            source = str(raw_input())
            destination = str(raw_input())
            tickets[source] = destination
            
        itinerary = []
        origin = list(set(tickets.keys()).difference(set(tickets.values())))[0]
        current_city = origin
        while current_city in tickets.keys():
            itinerary.append(current_city +'-'+tickets[current_city])
            current_city = tickets[current_city]

        print 'Case #'+ str(testcase) + ': ' + reduce(lambda x,y : x + ' ' + y, itinerary)