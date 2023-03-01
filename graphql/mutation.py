from graphene import Mutation, Int, String, Field
from type import User
from data import USERS

class CreateUser(Mutation):
    class Arguments:
        id = Int()
        name = String()
        username = String()
        email = String()
        phone = String()
        website = String()

    user = Field(User)

    def mutate(self, info, id, name, username, email, phone, website):
        user = User(id=id, name=name, username=username, email=email, phone=phone, website=website)
        return CreateUser(user=user)
