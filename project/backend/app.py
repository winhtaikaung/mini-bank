import asyncio
from datetime import datetime, timedelta
import uuid
import jwt
import tornado
from api.auth.auth_handler import MainHandler, LoginHandler, LogoutHandler, RefreshTokenHandler, RegisterHandler

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/register", RegisterHandler),
        (r"/login", LoginHandler),
        (r"/logout", LogoutHandler),
        (r"/refresh", RefreshTokenHandler),
    ], debug=True)


async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
