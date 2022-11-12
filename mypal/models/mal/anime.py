from mypal.models.mal.common import AnimeBroadcast, AnimeSeason, AnimeStatistics, AnimeStudio, Picture, Ranking
from mypal.models.mypal.media import Media
from mypal.models.mypal.fields import AnimeField, MangaField
from mypal.utils.unpackers import unpack_payload, unpack_common

class Anime(Media):
    def __init__(self, payload: dict, required: list) -> None:
        self.id: int
        '''The ID of the anime'''
        self.title: str
        '''The title of the anime'''
        self.main_picture: Picture
        '''The main picture chosen for the anime'''
        super().__init__(payload, required)
        self.media_type: str = unpack_payload(payload, "media_type", required)
        '''The media type of the anime'''
        self.status: str = unpack_payload(payload, "status", required)
        '''Current status of the anime'''
        self.number_of_episodes: int = unpack_payload(payload, "num_episodes", required)
        '''Number of episodes the anime has. 0 if unknown'''
        self.start_season: AnimeSeason = unpack_payload(payload, "start_season", required, returnType=AnimeSeason)
        '''The season when the anime started'''
        self.broadcast: AnimeBroadcast = unpack_payload(payload, "broadcast", required, returnType=AnimeBroadcast)
        '''Information about when the episodes would broadcast'''
        self.source: str = unpack_payload(payload, "source", required)
        '''The type of source material that is being adapted'''
        self.average_episode_length: int = unpack_payload(payload, "average_episode_duration", required)
        self.age_rating: str = unpack_payload(payload, "rating", required)
        self.studios: list[AnimeStudio] = unpack_payload(payload, "studios", required, returnType=AnimeStudio, recursive=True)
        self.statistics: AnimeStatistics = unpack_payload(payload, "statistics", required, returnType=AnimeStatistics)
        self.related_anime: list[RelatedAnime] = unpack_payload(payload, "related_anime", required, returnType=RelatedAnime, recursive=True)
        self.related_manga: list[RelatedManga] = unpack_payload(payload, "related_manga", required, returnType=RelatedManga, recursive=True)
        self.recommendations: list[RecommendedAnime] = unpack_payload(payload, "recommendations", required, returnType=RecommendedAnime, recursive=True)

###This import has to be after the Anime class to avoid circular imports
from mypal.models.mal.manga import Manga

class AnimeRanking(Ranking):
    def __init__(self, payload: dict, required: list) -> None:
        super().__init__(payload)
        self.anime = Anime(payload, required)

class RelatedAnime:
    def __init__(self, payload: dict) -> None:
        self.relation_type: str = unpack_common(payload, "relation_type")
        self.formatted_relation_type: str = unpack_common(payload, "relation_type_formatted")
        self.anime: Anime = Anime(payload.get("node"), [AnimeField.DEFAULT])

class RelatedManga:
    def __init__(self, payload: dict) -> None:
        self.relation_type: str = unpack_common(payload, "relation_type")
        self.formatted_relation_type: str = unpack_common(payload, "relation_type_formatted")
        self.manga: Manga = Manga(payload.get("node"), MangaField.DEFAULT)

class RecommendedAnime:
    def __init__(self, payload: dict) -> None:
        self.number_of_recommendations: int = unpack_common(payload, "num_recommendations")
        self.anime: Anime = Anime(payload.get("node"), AnimeField.DEFAULT)