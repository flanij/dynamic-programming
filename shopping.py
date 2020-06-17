from knapSack import knapSack

with open("shopping.txt") as inFile, open("results.txt", "w") as outFile:
    # T test cases
    # T (1 =< T =< 100) is given on the first line of the input file.
    T = int(inFile.readline())
    for test_case in range(T):
        # Each test case begins with a line containing a single integer number N that indicates the number
        # of items (1 =< N =< 100) in that test case
        N = int(inFile.readline())
        # Followed by N lines, each containing two integers: P and W. The first integer (1 =< P =< 5000)
        # corresponds to the price of object and the second integer (1 =< W =< 100) corresponds to the
        # weight of object. 
        P = []
        W = []
        for _ in range(N):
            PW = inFile.readline().split(" ")
            P.append(int(PW[0]))
            W.append(int(PW[1]))
        # The next line contains one integer (1 =< F =< 30) which is the number of people in that family. 
        F = int(inFile.readline())

        total_price = 0
        member_items = []
        # The next F lines contains the maximum weight (1 =< M =< 200) that can be carried by the 
        # ith person in the family (1 =< i =< F). 
        for i in range(F):
            carry_weight = int(inFile.readline())
            (price, items) = knapSack(P, W, carry_weight)
            total_price  += price
            items.sort()
            member_items.append(items)

        outFile.write("Test Case " + str(test_case+1) +"\n")
        outFile.write("Total Price " + str(total_price) +"\n")
        outFile.write("Member Items:\n")
        
        for i in range(F):
            outFile.write("{}: {}\n".format(i+1, " ".join(str(_+1) for _ in member_items[i])))

        outFile.write("\n")
