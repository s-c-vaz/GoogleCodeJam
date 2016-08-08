import copy




if __name__ == '__main__':

    testcases = int(raw_input())
    for testcase in xrange(1, testcases+1):

        store_credit = int(raw_input())
        item_count = int(raw_input())
        items = raw_input().split()
        items = map(lambda x: int(x), items) 
        items_with_index = []
        for i in xrange(len(items)):
            items_with_index.append((items[i],i))
        items_with_index.sort(key=lambda x:x[0])
        i = 0
        j = len(items)-1
        while i < j:
            current_sum = items_with_index[i][0] + items_with_index[j][0]
            if current_sum == store_credit:
                break
            elif current_sum < store_credit:
                i += 1
            elif current_sum > store_credit:
                j -= 1
                
        result = [items_with_index[i][1]+1,items_with_index[j][1]+1]
        result.sort()
        print 'Case #'+ str(testcase) + ': ' + str(result[0]) + ' ' + str(result[1])
                
