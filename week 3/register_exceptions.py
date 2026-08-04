from email import message
from ssl import CertificateError

from fastapi import FastAPI
from exception_handling import (
    LoginFailed,
    SignOutFailed,
    SignupFailed,
    EmailAlreadyRegistered,
    AccessTokenNotProvided,
    UserNotFound,
    create_exception_handler
)

def register_exception_handlers(
    app: FastAPI
):
    app.add_exception_handler(
        EmailAlreadyRegistered,
        create_exception_handler(
            409,
            {
                "success": False,
                "message": "Email is already registered"
            }
        )
    )

    app.add_exception_handler(
        SignupFailed,
        create_exception_handler(
            503,
            {
                "success": False,
                "message": "Signup service is currently unavailable"
            }
        )
    )

    app.add_exception_handler(
        LoginFailed,
        create_exception_handler(
            401,
            {
                "success":False,
                "message": "invalid login credentials"
            }
        )
    )

    app.add_exception_handler(
        AccessTokenNotProvided,
        create_exception_handler(
            401,
            {
                "success":False,
                "message": "access token required"
            }
        )
    )

    app.add_exception_handler(
        UserNotFound,
        create_exception_handler(
            401,
            {
                "success":False,
                "message": "provided access token is incorrect"
            }
        )
    )

    app.add_exception_handler(
        SignOutFailed,
        create_exception_handler(
            500,
            {
                "success":False,
                "message":"error in logging client out"
            }
        )
    )

