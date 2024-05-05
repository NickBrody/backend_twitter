from pydantic import BaseModel


class BaseTweet(BaseModel):
    """
    """
    content: str

class TweetIn(BaseTweet):
    ...


class TweetOut(BaseTweet):
    id: int

    class Config:
        from_attributes = True


# class BaseAllRecipe(BaseModel):
#     """
#     Базовый класс для всех рецептов
#     """
#     title: str
#     time: int
#     ingredients: str
#     description: str
#
#
# class AllRecipeIn(BaseAllRecipe):
#     ...
#
#
# class AllRecipeOut(BaseAllRecipe):
#     id: int
#
#     class Config:
#         orm_mode = True
