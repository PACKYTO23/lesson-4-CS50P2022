# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("x is not an integer.")
#     else:
#         break

# print(f"x is {x}")


def main():
    x = get_int("What's x? ")
    print(f"x is {x}.")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


# # # Different possibilities of the get_int() function.

# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer.")


# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#             return x
#         except ValueError:
#             print("x is not an integer.")


# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer.")
#         else:
#             return x


# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer.")
#         else:
#             break
#     return x


main()
