from mypal.models.mal.common import MangaPerson, MangaSerialization, Ranking
from mypal.models.mypal.media import Media
from mypal.utils.unpackers import unpack_payload, unpack_common
from mypal.models.mypal.fields import AnimeField, MangaField


class Manga(Media):
    def __init__(self, payload: dict, required: list) -> None:
        super().__init__(payload, required)
        self.media_type: str = unpack_payload(payload, "media_type", required)
        '''Media type of the manga'''
        self.status: str = unpack_payload(payload, "status", required)
        '''Manga status'''
        self.number_of_volumes: int = unpack_payload(payload, "num_volumes", required)
        '''Number of volumes the manga has'''
        self.number_of_chapters: int = unpack_payload(payload, "num_chapters", required)
        '''Number of chapters the manga has'''
        self.authors: list[MangaPerson] = unpack_payload(payload, "authors", required, returnType=MangaPerson, recursive=True)
        '''A list of people who worked on the manga and their respective roll'''
        self.serialization: list[MangaSerialization] = unpack_payload(payload, "serialization", required, returnType=MangaSerialization, recursive=True)
        '''A list of serializers'''
        self.related_anime: list[RelatedAnime] = unpack_payload(payload, "related_anime", required, returnType=RelatedAnime, recursive=True)
        self.related_manga: list[RelatedManga] = unpack_payload(payload, "related_manga", required, returnType=RelatedManga, recursive=True)
        self.recommendations: list[RecommendedManga] = unpack_payload(payload, "recommendations", required, returnType=RecommendedManga, recursive=True)


###This import has to be AFTER the Manga class to avoid circular imports
from mypal.models.mal.anime import Anime

class MangaRanking(Ranking):
    def __init__(self, payload: dict, required: list) -> None:
        super().__init__(payload)
        self.manga = Manga(payload, required)

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

class RecommendedManga:
    def __init__(self, payload: dict) -> None:
        self.number_of_recommendations: int = unpack_common(payload, "num_recommendations")
        self.manga: Manga = Manga(payload.get("node"), MangaField.DEFAULT)