import orm
from models import User, Blog, Comment
import asyncio

async def test(loop):
    await orm.create_pool(loop, user='seaha',password='password', db='awesome')
    u = User(name='Test', email='test@example.com', passwd='12345678', image='about:blank')
    await u.save()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    print('test finished.')