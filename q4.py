def age_check(func):
    def wrapper(age):
        if age < 18:
            raise ValueError("Age must be greater or equal to 18")
        func(age)

    return wrapper

@age_check
def can_vote(age):
    print("Yes you can Vote ")

age = int(input("Enter your age: "))

can_vote(age)