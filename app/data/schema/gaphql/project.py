# Created by Kelvin_Clark on 2/2/2022, 1:00 AM
import strawberry


@strawberry.type
class Project:
    id: int
    name: str
    description: str
