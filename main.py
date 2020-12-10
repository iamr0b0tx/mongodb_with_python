from mongo_db import MongoDB


def main():
    # connect to mongodb
    mongodb = MongoDB("iamr0b0tx", "DJ0Qb8XqulWFUXQK", "Cluster0", "business")
    # mongodb = MongoDB("ds", "gg", "Cluster0", "business")

    # create businesses
    print(mongodb.create({'name': 'Kitchen', 'rating': 1, 'cuisine': 'Pizza'}))

    # read business
    print(mongodb.read({'rating': 1}))

    # update business
    print(mongodb.update({'rating': 1}, {'rating': 5}))

    # delete business
    print(mongodb.delete({'rating': 5}))


if __name__ == '__main__':
    main()
