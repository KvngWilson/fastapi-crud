from fastapi import FastAPI, HTTPException, Header, status
from starlette.middleware.authentication import AuthenticationMiddleware
from app.core.middleware.jwt_auth_backend import JWTAuthBackend
from app.core.exception_handlers import (
  http_exception_handler,
  general_exception_handler,
  on_auth_error,
)

app = FastAPI(
  title= "Project Name",
  description= "Project Description",
  version= "0.1.0",
)

# Middleware setup
app.add_middleware(AuthenticationMiddleware, backend=JWTAuthBackend(), on_error=on_auth_error)

# Register custom exception handlers
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

# Importing routers
app.include_router(router)