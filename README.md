## Note: This project is in alpha

**Breaking changes can be made to `main` at any point.**

Missing features and documentation will be added overtime. 

# MyPAL

Welcome to MyPAL, a third party asynchronous python API wrapper for MyAnimeList. It aims to provide a simple to use service for accessing anime fro MAL.

## Features

MyPAL is in alpha. This means so features from the API may be missing, but that doesn't mean they won't be implemented! There is a [Roadmap](https://github.com/ABaddlesmere/MyPAL#roadmap) available to view what features will be implemented on the journey up to release 1.0

## How do I use MyPAL?

### Installing MyPAL
MyPAL is currently not available on PIP. You can install it through the following:
```
pip install git+https://github.com/ABaddlesmere/MyPAL
```

### Authentication
This current version of MyPAL only requires the Client ID to interact with the API. You can [create an ID here](https://myanimelist.net/apiconfig) by clicking `Create ID` and following the steps.

### An Example
Here is a basic example to get an anime with the ID of 1 and print it's title.
```python
from mypal import Client, enums
import asyncio

client = Client(CLIENT_ID)

async def main():
        anime = await client.get_anime_details(id=1)
        print(anime.title)

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())
```

## Roadmap
This is the roadmap for features leading up to the 1.0 release
### Planned
- [ ] client.http rewrite
- [ ] Replace errors, warnings and debug prints with logging
- [ ] Add basic documentation for models and client
### In Progress
- [ ] Add unit tests
- [x] Implement smart caching
### Completed
- [x] Manga Search
- [x] Get manga details
- [x] Get manga ranking
- [x] Make the use of enums consistent throught
- [x] Add rate limiter
