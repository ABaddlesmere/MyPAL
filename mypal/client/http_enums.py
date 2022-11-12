class HTTP_ENUMS:
    __BASE: str = "https://api.myanimelist.net/v2"

    A_SEARCH: str = f"{__BASE}/anime"
    A_GET_DETAILS: str = f"{__BASE}/anime/id"
    A_RANKING: str = f"{__BASE}/anime/ranking"
    A_SEASONAL: str = f"{__BASE}/anime/seasonal/y/m"