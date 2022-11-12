from mypal.utils.unpackers import unpack_common
from mypal.utils.datetime_converter import str_to_datetime
from datetime import datetime

## Common Models

class Ranking:
    def __init__(self, payload: dict) -> None:
        self.rank: int = unpack_common(payload.get('ranking', {}), "rank")
        self.revious_rank: int = unpack_common(payload.get('ranking', {}), "previous_rank")

class AlternativeTitles:
    '''
    Alternative Titles
    '''
    def __init__(self, payload: dict) -> None:
        self.synonyms: list[str] = unpack_common(payload, "synonyms")
        self.en: str = unpack_common(payload, "en")
        self.jp: str = unpack_common(payload, "jp")

class Picture:
    '''
    Defines a Picture, storing medium and ,if available, large URIs to the image
    '''
    def __init__(self, payload: dict) -> None:
        self.medium: str = unpack_common(payload, "medium")
        self.large: str = unpack_common(payload, "large")

class Genre:
    '''
    Defines a Genre for the media
    '''
    def __init__(self, payload: dict) -> None:
        self.id: int = unpack_common(payload, "id")
        self.name: str = unpack_common(payload, "name")

class UserListStatus:
    def __init__(self, payload: dict) -> None:
        self.status: str = unpack_common(payload, "status")
        self.score: int = unpack_common(payload, "score")
        self.number_of_episodes_watched: int = unpack_common(payload, "num_episodes_watched")
        self.is_rewatching: bool = unpack_common(payload, "is_rewatching")
        self.start_date: datetime.datetime = str_to_datetime(unpack_common(payload, "start_date"))
        self.finish_date: datetime.datetime = str_to_datetime(unpack_common(payload, "finish_date"))
        self.priority: int = unpack_common(payload, "priority")
        self.times_rewatched: int = unpack_common(payload, "num_times_rewatched")
        self.tags: list[str] = unpack_common(payload, "tags")
        self.comments: str = unpack_common(payload, "comments")
        self.updated_at: datetime.datetime = str_to_datetime(unpack_common(payload, "updated_at"))

### Anime Specific Models

class AnimeStudio:
    def __init__(self, payload: dict) -> None:
        self.id: int = unpack_common(payload, "id")
        self.name: str = unpack_common(payload, "name")

class AnimeSeason:
    def __init__(self, payload: dict) -> None:
        self.year: int = unpack_common(payload, "year")
        self.season: str = unpack_common(payload, "season")

class AnimeBroadcast:
    def __init__(self, payload: dict) -> None:
        self.day: str = unpack_common(payload, "day_of_the_week")
        ##This will need to be thrown into the str to datetime converter
        self.time = unpack_common(payload, "start_time")

class AnimeStatistics:
    def __init__(self, payload: dict) -> None:
        self.list_users: int = unpack_common(payload, "num_list_users")
        self.watching: int = unpack_common(payload.get('status', {}), "watching")
        self.completed: int = unpack_common(payload.get('status', {}), "completed")
        self.on_hold: int = unpack_common(payload.get('status', {}), "on_hold")
        self.dropped: int = unpack_common(payload.get('status', {}), "dropped")
        self.plan_to_watch: int = unpack_common(payload.get('status', {}), "plan_to_watch")


### Manga Specific Models

class MangaPerson:
    def __init__(self, payload: dict) -> None:
        self.id: int = unpack_common(payload.get('node', {}), "id")
        self.first_name: str = unpack_common(payload.get('node', {}), "first_name")
        self.last_name: str = unpack_common(payload.get('node', {}), "last_name")
        self.role: str = unpack_common(payload, "role")

class MangaSerialization:
    def __init__(self, payload: dict) -> None:
        self.id: int = unpack_common(payload.get('node', {}), "id")
        self.name: str = unpack_common(payload.get('node', {}), "name")
        self.role: str = unpack_common(payload, "role")