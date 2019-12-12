import os
import asyncio
import aiohttp
from gidgethub.aiohttp import GitHubAPI

async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "jhbell", oauth_token=os.getenv("GH_AUTH"))
        await gh.post('repos/jhbell/github-bot-test/issues',
                data={
                    'title': 'Magically created issue',
                    'body': 'This issue was created from the CLI!',
                })

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
