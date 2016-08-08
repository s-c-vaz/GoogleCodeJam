'''
Created on 21-Jan-2016

@author: annervaz
'''

if __name__ == '__main__':
    
    
   testcases = int(raw_input())
   
   for testcase in xrange(1, testcases+1):

        T = int(raw_input())
        NA, NB = raw_input().split()
        NA = int(NA)
        NB = int(NB)
        departures_from_A = []
        arrivals_at_A = []
        departures_from_B = []
        arrivals_at_B = []
        trains_at_A = []
        trains_at_B = []
        for i in xrange(0,NA):
            departure,arrival = raw_input().split()
            departure_hour, departure_minute = map(lambda x:int(x),departure.split(':'))
            departures_from_A.append((departure_hour,departure_minute,-1))
            arrival_hour, arrival_minute = map(lambda x:int(x),arrival.split(':'))
            arrival_minute += T
            while arrival_minute > 60:
                arrival_minute -= 60
                arrival_hour += 1
            arrivals_at_B.append((arrival_hour,arrival_minute,1))
        for i in xrange(0,NB):
            departure,arrival = raw_input().split()
            departure_hour, departure_minute = map(lambda x:int(x),departure.split(':'))
            departures_from_B.append((departure_hour,departure_minute,-1))
            arrival_hour, arrival_minute = map(lambda x:int(x),arrival.split(':'))
            arrival_minute += T
            while arrival_minute > 60:
                arrival_minute -= 60
                arrival_hour += 1
            arrivals_at_A.append((arrival_hour,arrival_minute,1))
            
        trains_at_A.extend(departures_from_A)
        trains_at_A.extend(arrivals_at_A)
        trains_at_A.sort(key=lambda x: (x[0],x[1],-1*x[2]))
        trains_required_to_start_at_A = 0
        trains_A = 0
        for instance in trains_at_A:
            trains_A += instance[2]
            trains_required_to_start_at_A = min(trains_required_to_start_at_A,trains_A)
            
        trains_at_B.extend(departures_from_B)
        trains_at_B.extend(arrivals_at_B)
        trains_at_B.sort(key=lambda x: (x[0],x[1],-1*x[2]))
        trains_required_to_start_at_B = 0
        trains_B = 0
        for instance in trains_at_B:
            trains_B += instance[2]
            trains_required_to_start_at_B = min(trains_required_to_start_at_B,trains_B)
        print 'Case #'+ str(testcase) + ': ' + str(-1*trains_required_to_start_at_A) + ' ' + str(-1*trains_required_to_start_at_B)