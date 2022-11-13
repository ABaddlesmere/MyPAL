from mypal.models.mal.anime import Anime
from mypal.client.http import Router
from mypal.client.http_enums import HTTP_ENUMS
from mypal.models.mypal.enums import AnimeRankingType, AnimeSortType, SeasonType
from mypal.models.mypal.fields import AnimeField, MangaField
from mypal.utils.param_handlers import steralise, to_str
from mypal.models.mypal.pagination import Pagination

class Client:
    def __init__(self, clientID: str, **kwargs) -> None:
        self.__clientID = clientID
        if not kwargs.get("debugDisableRouterOnStartup", False):
            self.router = Router(clientID = clientID)
        self.defaults = {
            "nsfw": kwargs.get("default_nsfw", False),
            "limit": kwargs.get("default_limit", 20),
            "offset": kwargs.get("default_offset", 0),

        }
        self.anime_defaults = self.defaults.copy()
        self.anime_defaults["fields"] = kwargs.get("default_anime_fields", AnimeField.DEFAULT)
        self.manga_defaults = self.defaults.copy()
        self.manga_defaults["fields"] = kwargs.get("default_manga_fields", MangaField.DEFAULT)

    async def search_anime(
        self,
        query: str,
        fields: list[AnimeField]|AnimeField = None,
        limit: int = None,
        nsfw: bool = None,
        offset: int = None
        ) -> Pagination:
        
        params: dict = steralise(locals(), self.anime_defaults)
        params["q"] = params["query"]
        params.pop("query")

        router_payload = await self.router.GET(
            url=HTTP_ENUMS.A_SEARCH,
            params=to_str(params)
        )
        return Pagination(router_payload, Anime, params['fields'])


    async def get_anime_details(
        self,
        id: int,
        fields: list[AnimeField]|AnimeField = None,
        nsfw: bool = None,
        ) -> Anime:
        
        params: dict = steralise(locals(), self.anime_defaults)

        router_payload = await self.router.GET(
            url=HTTP_ENUMS.A_GET_DETAILS.replace("/id", f"/{id}"),
            params=to_str(params)
        )
        
        return Anime(router_payload, params['fields'])
    
    async def get_anime_season(
        self,
        season: SeasonType,
        year: int,
        fields: list[AnimeField]|AnimeField = None,
        nsfw: bool = None,
        sort: AnimeSortType = None,
        limit: int = None,
        offset: int = None,
        ) -> Pagination:
        print(locals())
        params: dict = steralise(locals(), self.anime_defaults, excludes=["season","year"])
        router_payload = await self.router.GET(
            url=HTTP_ENUMS.A_SEASONAL.replace("/y", f"/{year}").replace("/m", f"/{season}"),
            params=to_str(params)
        )

        return Pagination(router_payload, Anime, params['fields'])


    async def get_anime_ranking(
        self,
        ranking: AnimeRankingType,
        fields: list[AnimeField]|AnimeField = None,
        nsfw: bool = None,
        limit: int = None,
        offset: int = None
        ) -> Pagination:
        
        params: dict = steralise(locals(), self.anime_defaults)
        router_payload = await self.router.GET(
            url=HTTP_ENUMS.A_RANKING,
            params=to_str(params)
        )
        
        return Pagination(router_payload, Anime, params['fields'])
