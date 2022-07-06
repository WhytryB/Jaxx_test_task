from app.crud.base import CRUDBase
from app.models.visitor import Visitor
from app.schemas.visitor import VisitorCreate


class CRUDRecipe(CRUDBase[Visitor, VisitorCreate]):
    pass


visitor = CRUDRecipe(Visitor)
