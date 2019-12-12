import os
import asyncio
import aiohttp
from gidgethub.aiohttp import GitHubAPI

async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "jhbell", oauth_token=os.getenv("GH_AUTH"))
        await gh.post('repos/jhbell/github-bot-test/issues/1/reactions',
                data={
                    'content': 'rocket',
                },
                accept='application/vnd.github.squirrel-girl-preview')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
