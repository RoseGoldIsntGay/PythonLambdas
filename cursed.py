# Multiple expressions in one lambda
(
    lambda _=None: (
        print("I"),
        print("love"),
        print("Python!")
    )
)()

# Assign variables in lambda
(
    lambda _=None: (
        # globals is a dictionary that holds all global variables in script
        # .update replaces '='
        # {} anonymous dictionary where key is the variable's name and value is the variable's value
        globals().update({"num": 1}),
        print(num),
    )
)()

# If statement in lambda
(
    lambda _=None: (
        globals().update({"number": 0}),
        number == 0 and print("number is 0"),
        globals().update({"number": 14}),
        number == 0 and print("number is 0") or number == 7 and print("number is 7") or print("number is not 0 or 7")
    )
)()

# For loop in lambda
(
    lambda _=None: (
        # for i in range(10):
        #    print(i)
        [(lambda x: (
            print(x)
        ))(i) for i in range(10)]
    )
)()

# While loop in lambda (recursion)
(lambda _=None: (
    globals().update({"count": 0}),
    globals().update({"func": (lambda _=None: (
        # count += 1
        globals().update({"count": globals().get("count") + 1}),
        print(count),

        # if count < 10: 
        #    func()
        count < 10 and func()
    ))}),
    func()
))()
