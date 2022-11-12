from mypal.models.mal.common import AlternativeTitles, Genre, Picture
from mypal.utils.unpackers import unpack_payload
from mypal.utils.datetime_converter import str_to_datetime
import datetime

class Media:
    '''
    The base class for mal.Anime and mal.Manga
    '''
    def __init__(self, payload: dict, requested: list) -> None:
        
        self.id: int = unpack_payload(payload, "id", requested)
        '''Media ID'''
        self.title: str = unpack_payload(payload, "title", requested)
        '''Media Title'''
        self.main_picture: Picture = unpack_payload(payload, "main_picture", requested, Picture)
        '''That main picture for the media'''
        self.alternative_titles: AlternativeTitles = unpack_payload(payload, "alternative_titles", requested, returnType=AlternativeTitles)
        ''''''
        self.start_date: datetime.datetime = str_to_datetime(unpack_payload(payload, "start_date", requested))
        '''The date when the media started'''
        self.end_date: datetime.datetime = str_to_datetime(unpack_payload(payload, "end_date", requested))
        '''The date when the media finished'''
        self.synopsis: str = unpack_payload(payload, "synopsis", requested)
        '''The synopsis for the media'''
        self.mean: float = unpack_payload(payload, "mean", requested)
        '''The mean score for the media'''
        self.rank: int = unpack_payload(payload, "rank", requested)
        '''The rank for the media'''
        self.popularity: int = unpack_payload(payload, "popularity", requested)
        '''The popularity score for the media'''
        self.list_users: int = unpack_payload(payload, "num_list_users", requested)
        '''The number of users with this media in their list'''
        self.scored_users: int = unpack_payload(payload, "num_scoring_users", requested)
        '''The number of users who have scored this media'''
        self.nsfw: str = unpack_payload(payload, "nsfw", requested)
        '''The NSFW ranking of this media
            ---
            white - Safe For Work
            gray - May not be Safe For Work
            black - Not Safe For Work
        
        '''
        self.genres: list[Genre] = unpack_payload(payload, "genres", requested, returnType=Genre, recursive=True)
        '''List of genres that the media falls under'''
        self.created_at: datetime.datetime = str_to_datetime(unpack_payload(payload, "created_at", requested))
        '''The time at which the media's MAL page was created'''
        self.updated_at: datetime.datetime = str_to_datetime(unpack_payload(payload, "updated_at", requested))
        '''The time at which the media's MAL page was last updated'''
        self.pictures: list[Picture] = unpack_payload(payload, "pictures", requested, returnType=Picture, recursive=True)
        '''A list of pictures for this media'''
        self.background: str = unpack_payload(payload, "background", requested)
        '''The background for this media'''
        self.favourites: int = unpack_payload(payload, "num_favourites", requested)
        '''Number of favourites this has'''

