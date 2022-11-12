
class MISSING:
    '''
    A request for this field was made to MAL, but they didn't return it, or returned null
    '''
    def __repr__(self) -> str:
        return "A request for this field was made to MAL, but they didn't return it or returned null"

class UNKNOWN:
    '''
    There was no request for this field
    '''
    def __repr__(self) -> str:
        return "There was no request for this field"


################
# Common Enums #
################

class NSFWType:
    WHITE: str = "white"
    '''This work is safe for work'''
    GRAY: str = "gray"
    '''This work may not be safe for work'''
    BLACK: str = "black"
    '''This work is not safe for work'''

class MediaRankingType:
    ALL: str = "all"
    '''All Time'''
    BY_POPULARITY: str = "bypopularity"
    '''Most Popular'''
    FAVOURITE: str = "favourite"
    '''Most Favourited'''

class RelationType:
    SEQUEL: str = "sequel"
    '''A Sequel'''
    PREQUEL: str = "prequel"
    '''A Prequel'''
    ALTERNATIVE_SETTING: str = "alternative_setting"
    '''An Alternative Setting'''
    ALTERNATIVE_VERSION: str = "alternative_version"
    '''An Alternative Version'''
    SIDE_STORY: str = "side_story"
    '''A Side Story'''
    PARENT_STORY: str = "parent_story"
    '''A Parent Story'''
    SUMMARY: str = "summary"
    '''A Summary'''
    FULL_STORY: str = "full_story"
    '''A Full Story'''

###############
# Anime Enums #
###############

class AnimeType:
    UNKNOWN: str = "unknown"
    '''Unknown Anime Type'''
    TV: str = "tv"
    '''Anime TV Show'''
    OVA: str = "ova"
    '''Anime Original Video Animation'''
    MOVIE: str = "movie"
    '''Anime Movie'''
    SPECIAL: str = "special"
    '''Anime Movie'''
    ONA: str = "ona"
    '''Anime Original Net Animation'''
    MUSIC: str = "music"
    '''Music Anime'''

class AnimeStatusType:
    AIRING: str = "currently_airing"
    '''Currently Airing'''
    FINISHED: str = "finished_airing"
    '''Finished Airing'''
    NOT_AIRED: str = "not_yet_aired"
    '''Not Aired Yet'''

class SeasonType:
    SPRING: str = "spring"
    '''Spring Season months April, May, June'''
    SUMMER: str = "summer"
    '''Summer Season months July, August, September'''
    FALL: str = "fall"
    '''Fall Season months October, November, December'''
    AUTUMN: str = FALL
    '''Autumn Season months October, November, December (Ailias of FALL)'''
    WINTER: str = "winter"
    '''Winter Season months January, February, March'''

class AnimeSourceType:
    OTHER: str = "other"
    '''Other anime source'''
    ORIGINAL: str = "original"
    '''Anime original'''
    MANGA: str = "manga"
    '''Anime adapted from manga'''
    KOMA_MANGA_4: str = "4_koma_manga"
    '''Anime adapted from 4-panel manga'''
    WEB_MANGA: str = "web_manga"
    '''Anime adapted from web manga'''
    DIGITAL_MANGA: str = "digital_manga"
    '''Anime adapted from digital manga'''
    NOVEL: str = "novel"
    '''Anime adapted from a novel'''
    LIGHT_NOVEL: str = "light_novel"
    '''Anime adapted from a light novel'''
    VISUAL_NOVEL: str = "visual_novel"
    '''Anime adapted from a visual novel'''
    GAME: str = "game"
    '''Anime adapted from a game'''
    CARD_GAME: str = "card_game"
    '''Anime adapted from a card game'''
    BOOK: str = "book"
    '''Anime adapted from a book'''
    PICTURE_BOOK: str = "picture_book"
    '''Anime adapted from a picture book'''
    RADIO: str = "radio"
    '''Anime adapted from radio'''
    MUSIC: str = "music"
    '''Anime adapted from music'''

class AnimeRatingType:
    G: str = "g"
    '''G - All Ages'''
    PG: str = "pg"
    '''PG - Children'''
    PG_13: str = "pg_13"
    '''PG13 - Teens 13 and Older'''
    R: str = "r"
    '''R - 17+ (Violence & Profanity)'''
    R_PLUS: str = "r+"
    '''R+ - Profanity & Mild Nudity'''
    Rx: str = "rx"
    '''Rx - Hentai'''

class AnimeSortType:
    SCORE: str = "anime_score"
    '''Sort by Anime Score'''
    NUM_LIST_USERS: str = "anime_num_list_users"
    '''Sort by the number of users with this in their list'''

class AnimeRankingType(MediaRankingType):
    AIRING: str = "airing"
    '''Top Airing Anime'''
    UPCOMING: str = "upcoming"
    '''Top Upcoming Anime'''
    TV: str = "tv"
    '''Top Anime TV Series'''
    OVA: str = "ova"
    '''Top Anime OVA Series'''
    MOVIE: str = "movie"
    '''Top Anime Movies'''
    SPECIAL: str = "special"
    '''Top Abune Specials'''

###############
# Manga Enums #
###############

class MangaType:
    UNKNOWN: str = "unknown"
    '''Unknown Manga Type'''
    MANGA: str = "manga"
    '''Manga'''
    NOVEL: str = "novel"
    '''Novel'''
    ONE_SHOT: str = "one_shot"
    '''One-shot'''
    DOUJIN: str = "doujinshi"
    '''Doujinshi (Self-published)'''
    MANHWA: str = "manhwa"
    '''Manhwa (Korean Comic)'''
    MANHUA: str = "manhua"
    '''Manhua (Chinese Comic)'''
    OEL: str = "oel"
    '''OEL (Original English Language)'''

class MangaStatusType:
    FINISHED: str = "finished"
    '''Manga has finished publishing'''
    CURRENTLY_PUBLISHING: str = "currently_publishing"
    '''Manga is currently publishing'''
    NOT_PUBLISHING: str = "not_yet_published"
    '''Manga is not being published'''

class MangaRankingType(MediaRankingType):
    MANGA: str = "manga"
    '''Top Manga'''
    NOVELS: str = "novels"
    '''Top Novels'''
    ONE_SHOTS: str = "oneshots"
    '''Top One-shots'''
    DOUJIN: str = "doujin"
    '''Top Doujinshi'''
    MANHWA: str = "manhwa"
    '''Top Manhwa'''
    MANHUA: str = "manhua"
    '''Top Manhua'''