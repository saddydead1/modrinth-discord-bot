import httpx
import logging
import json
import os
from models.Version import Version


ID = os.environ.get('ID')

log = logging.getLogger(__name__)
url = f'https://api.modrinth.com/v2/project/{ID}/version'
versions = list

class Modrinth:
    async def request() -> None | Version:
        async with httpx.AsyncClient() as client:
            r = await client.get(url)
            j = json.loads(r.text)

            global versions
            if (list(map(lambda x: x['name'], j)) != versions):
                for i in list(map(lambda x: x['name'], j)):
                    if i not in versions:
                        for b in j:
                            if (b['name'] == i):
                                return Version(b['name'], b['version_number'], b['version_type'], b['changelog'])

                versions = list(map(lambda x: x['name'], j))

        
    async def update() -> None:
        async with httpx.AsyncClient() as client:
            r = await client.get(url)
            j = json.loads(r.text)

            global versions
            versions = list(map(lambda x: x['name'], j))


        
        

