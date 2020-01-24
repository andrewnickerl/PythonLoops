def main():
    x = 0

    while x < 5:
        print(x)
        x = x+1

    for x in range(5,10): #note format difference from for(int i = 0, i < 10, i++)--python uses range iteration instead
        print(x)

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    for d in days: #Python for loops don't have to specifically iterate over numbers specifically
        print(d)

    for x in range(5,10):
        if(x==7): break #ends iteration to "break out" of loop when a condition is met
        print(x)

    for x in range(5,10):
        if(x%2 == 0): continue #skips that iteration of the loop when a contition is met
        print(x)

    for i,d in enumerate(days): #loops over days[] but returns index of value in the array as well as the value itself
        print (i,d)

if __name__ == "__main__":
    main()