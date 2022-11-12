class AnimeField:
    '''
    All fields currently available for anime
    '''
    ID: str = "id"
    '''ID of the anime'''
    TITLE: str = "title"
    '''Title of the anime'''
    MAIN_PICTURE: str = "main_picture"
    '''Main picture representing the anime'''
    ALTERNATIVE_TITLES: str = "alternative_titles"
    '''Alternative titles for the anime'''
    START_DATE: str = "start_date"
    '''Start date of the anime'''
    END_DATE: str = "end_date"
    '''End date of the anime'''
    SYNOPSIS: str = "synopsis"
    '''Synopsis of the anime'''
    MEAN: str = "mean"
    '''Mean score for the anime'''
    RANK: str = "rank"
    '''Overall ranking of the anime'''
    POPULARITY: str = "popularity"
    '''Popularity score of the anime'''
    LISTED_USERS: str = "num_list_users"
    '''Number of users with the anime in their list'''
    SCORED_USERS: str = "num_scoring_users"
    '''Number of users who have scored the anime'''
    NSFW: str = "nsfw"
    '''NSFW rating of the anime'''
    GENRES: str = "genres"
    '''Genres that the anime fall under'''
    CREATED_AT: str = "created_at"
    '''When the MAL page was created for the anime'''
    UPDATED_AT: str = "updated_at"
    '''When the MAL page was last updated for the anime'''
    MEDIA_TYPE: str = "media_type"
    '''What type of media the anime is'''
    STATUS: str = "status"
    '''What the current status of the anime is'''
    MY_LIST_STATUS: str = "my_list_status"
    '''The statistics of the anime in your list'''
    NUMBER_OF_EPISODES: str = "num_episodes"
    '''The number of episodes that the anime has'''
    START_SEASON: str = "start_season"
    '''What season the anime was released in'''
    BROADCAST: str = "broadcast"
    '''When each episode of the anime is broadcasted'''
    SOURCE: str = "source"
    '''The source that the anime is adapting from'''
    AVERAGE_EPISODE_LENGTH: str = "average_episode_duration"
    '''Average length of each episode (in seconds)'''
    AGE_RATING: str = "rating"
    '''The age rating of the anime'''
    STUDIOS: str = "studios"
    '''Studio(s) that worked on the anime'''
    PICTURES: str = "pictures"
    '''Other pictures from the anime'''
    BACKGROUND: str = "background"
    '''Background information about the anime'''
    RELATED_ANIME: str = "related_anime"
    '''A list of related anime'''
    RELATED_MANGA: str = "related_manga"
    '''A list of related manga'''
    RECOMMENDATIONS: str = "recommendations"
    '''A list of recommendations'''
    STATISTICS: str = "statistics"
    '''Statistics for this anime'''
    
    ##These are not yet documents in the offical MAL V2 docs
    NUMBER_OF_FAVOURITES: str = "num_favourites"
    '''Number of favourites that the anime has'''
    OPENING_THEMES: str = "opening_themes"
    '''A list of the opening themes in the anime'''
    ENDING_THEMES: str = "ending_themes"
    '''A list of the ending themes in the anime'''
    
    ##Misc
    ALL: list = [
        ID,
        TITLE,
        MAIN_PICTURE,
        ALTERNATIVE_TITLES,
        START_DATE,
        END_DATE,
        SYNOPSIS,
        MEAN,
        RANK,
        POPULARITY,
        LISTED_USERS,
        SCORED_USERS,
        NSFW,
        GENRES,
        CREATED_AT,
        UPDATED_AT,
        MEDIA_TYPE,
        STATUS,
        MY_LIST_STATUS,
        NUMBER_OF_EPISODES,
        START_SEASON,
        BROADCAST,
        SOURCE,
        AVERAGE_EPISODE_LENGTH,
        STUDIOS,
        PICTURES,
        BACKGROUND,
        RELATED_ANIME,
        RELATED_MANGA,
        RECOMMENDATIONS,
        STATISTICS,
        NUMBER_OF_FAVOURITES,
        OPENING_THEMES,
        ENDING_THEMES
    ]
    '''All anime fields will be returned'''
    DEFAULT = [
        ID,
        TITLE,
        MAIN_PICTURE
    ]
    '''Default fields if none are specified'''

class MangaField:
    '''
    All fields currently available for manga
    '''
    ID: str = "id"
    '''ID of the anime'''
    TITLE: str = "title"
    '''Title of the anime'''
    MAIN_PICTURE: str = "main_picture"
    '''Main picture representing the anime'''
    ALTERNATIVE_TITLES: str = "alternative_titles"
    '''Alternative titles for the anime'''
    START_DATE: str = "start_date"
    '''Start date of the anime'''
    END_DATE: str = "end_date"
    '''End date of the anime'''
    SYNOPSIS: str = "synopsis"
    '''Synopsis of the anime'''
    MEAN: str = "mean"
    '''Mean score for the anime'''
    RANK: str = "rank"
    '''Overall ranking of the anime'''
    POPULARITY: str = "popularity"
    '''Popularity score of the anime'''
    LISTED_USERS: str = "num_list_users"
    '''Number of users with the anime in their list'''
    SCORED_USERS: str = "num_scoring_users"
    '''Number of users who have scored the anime'''
    NSFW: str = "nsfw"
    '''NSFW rating of the anime'''
    GENRES: str = "genres"
    '''Genres that the anime fall under'''
    CREATED_AT: str = "created_at"
    '''When the MAL page was created for the anime'''
    UPDATED_AT: str = "updated_at"
    '''When the MAL page was last updated for the anime'''
    MEDIA_TYPE: str = "media_type"
    '''What type of media the anime is'''
    STATUS: str = "status"
    '''What the current status of the anime is'''
    MY_LIST_STATUS: str = "my_list_status"
    '''The statistics of the anime in your list'''
    NUMBER_OF_VOLUMES: str = "num_volumes"
    '''Number of volumes that the manga has'''
    NUMBER_OF_CHAPTERS: str = "num_chapters"
    '''Number of chapters the manga has'''
    AUTHORS: str = "authors"
    '''A list of authors that worked on the manga'''
    PICTURES: str = "pictures"
    '''Other pictures from the anime'''
    BACKGROUND: str = "background"
    '''Background information about the anime'''
    RELATED_ANIME: str = "related_anime"
    '''A list of related anime'''
    RELATED_MANGA: str = "related_manga"
    '''A list of related manga'''
    RECOMMENDATIONS: str = "recommendations"
    '''A list of recommendations'''
    SERIALIZATION: str = "serialization"
    '''A list of serialization companies'''
    
    ##These are not yet documents in the offical MAL V2 docs
    NUMBER_OF_FAVOURITES: str = "num_favourites"
    '''Number of favourites that the anime has'''
    
    ##Misc
    ALL = [
        ID,
        TITLE,
        MAIN_PICTURE,
        ALTERNATIVE_TITLES,
        START_DATE,
        END_DATE,
        SYNOPSIS,
        MEAN,
        RANK,
        POPULARITY,
        LISTED_USERS,
        SCORED_USERS,
        NSFW,
        GENRES,
        CREATED_AT,
        UPDATED_AT,
        MEDIA_TYPE,
        STATUS,
        NUMBER_OF_VOLUMES,
        NUMBER_OF_CHAPTERS,
        AUTHORS,
        PICTURES,
        BACKGROUND,
        RELATED_ANIME,
        RELATED_MANGA,
        RECOMMENDATIONS,
        SERIALIZATION,
        NUMBER_OF_FAVOURITES
    ]
    '''All manga fields will be returned'''
    DEFAULT = [
        ID,
        TITLE,
        MAIN_PICTURE
    ]
    '''Default fields if none are specified'''
