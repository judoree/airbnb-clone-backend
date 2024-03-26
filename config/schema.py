import strawberry


@strawberry.type
class Query:
    @strawberry.field
    def ping(self) -> str:  # -> str: 이것은 type annotarion 임
        return "pong"


schema = strawberry.Schema(query=Query)
