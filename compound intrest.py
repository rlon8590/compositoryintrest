def main():
    print("In 2 years at 5%%, $4000 will be %.2" % calculateFutureValue(4000, 5, 2))
    print("In 10 years at 5%%, $400 will be %.2" % calculateFutureValue(400, 2, 10))
    print("In 5 years at 5%%, $10000 will be %.2" % calculateFutureValue(10000, 7, 5))

def calculateFutureValue(balance, rate, year) :
    return balance * (1 + rate / 100) ** year