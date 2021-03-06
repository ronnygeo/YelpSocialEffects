from pymongo import MongoClient, DESCENDING, ASCENDING

client = MongoClient()

db = client['yelp']
user_collection = db.user
user_friends_collection = db.user_friends_limited
review_collection = db.review
business_collection = db.business
tip_collection = db.tip
review_user_business_collection = db.review_user_business

database = db.user_review_friends

def getUsersFromUserFriends(count=None):
    """
    :param count:
    :return: All the users in the mongo database.
    Returns all the users in the dataset. If a count is included results will be limited, otherwise returns all.
    """
    if count == None:
        return user_friends_collection.find().sort('count', DESCENDING).batch_size(10)
    else:
        # print count
        return user_friends_collection.find().sort('count', DESCENDING).limit(count).batch_size(10)

def getFriendsOfUser(userId):
    return user_friends_collection.findOne({"userId": userId})

def getUsersFromUserFriendsAsc(count=None):
    """
    :param count:
    :return: All the users in the mongo database.
    Returns all the users in the dataset. If a count is included results will be limited, otherwise returns all.
    """
    if count == None:
        return user_friends_collection.find().batch_size(50)
    else:
        return user_friends_collection.find().sort('count', ASCENDING).limit(count).batch_size(50)


def getUsers(count=None):
    """
    :param count:
    :return: All the users in the mongo database.
    Returns all the users in the dataset. If a count is included results will be limited, otherwise returns all.
    """
    if count == None:
        return user_collection.find().batch_size(50)
    else:
        return user_collection.find().limit(count)


def findUser(userId):
    """
    :param userId:
    :return: The user obj
     Finds a particular user from a dataset.
    """
    return user_collection.find_one({"user_id": userId})

def findReviews(userId, count=None):
    """
    :param userId:
    :return: all the reviews of the user
     Returns all the reviews created by the user.
    """
    if count == None:
        return review_collection.find({"user_id": userId})
    else:
        return review_collection.find({"user_id": userId}).limit(count)


def findBusiness(businessId):
    """
    :param businessId:
    :return: business Object
     Returns the particular business object from the database.
    """
    return business_collection.find_one({"business_id": businessId})

def findReviewUserBusinessByUserId(userId, count=None):
    if count == None:
        return database.find_one({"_id": userId})["reviews"]
    # else:
    #     return database.find({"user_id": userId})[].limit(count)

#
# def test():
#     for movie in movie_collection.find():
#         for r in ratings_collection.find({"movieId": movie["movieId"]}):
#             print movie, r
#             break
#         for t in tags_collection.find({"movieId": movie["movieId"]}):
#             print t
#             break
#         for l in links_collection.find({"movieId": movie["movieId"]}):
#             print l
#             break
#         break

# print ratings_collection.find({"userId": 295}).count()



# for rating in ratings_collection.find():
#	print rating["movieId"]
