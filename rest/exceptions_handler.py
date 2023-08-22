from fastapi import HTTPException

class NotFoundError(HTTPException):
    def __init__(self, detail: str = {"message": "Item not found"}):
        super().__init__(status_code=404, detail=detail)

class BadRequestError(HTTPException):
    def __init__(self, detail: str = {"message": "Bad request"}):
        super().__init__(status_code=400, detail=detail)

class UnauthorizedError(HTTPException):
    def __init__(self, detail: str ={"message": "Unauthorized"}):
        super().__init__(status_code=401, detail=detail)

class ForbiddenError(HTTPException):
    def __init__(self, detail: str = {"message": "Forbidden"}):
        super().__init__(status_code=403, detail=detail)

class UnprocessableEntityError(HTTPException):
    def __init__(self, detail: str = {"message": "Unprocessable entity"}):
        super().__init__(status_code=422, detail=detail)

class InternalServerError(HTTPException):
    def __init__(self, detail: str = {"message": "Internal server error"}):
        super().__init__(status_code=500, detail=detail)
