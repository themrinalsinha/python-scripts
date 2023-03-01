from graphene import ObjectType
from data import USERS

class Query(ObjectType):
    def resolve_users(self, info):
        return USERS

    def resolve_user(self, info, id):
        return list(filter(lambda user: user['id'] == id, USERS))[0]

    def resolve_user_by_name(self, info, name):
        return list(filter(lambda user: user['name'] == name, USERS))[0]
