from mypal.models.mypal.media import Media
from mypal.models.mypal.fields import AnimeField, MangaField
from mypal.models.mal.anime import Anime
from mypal.models.mal.manga import Manga

class Pagination:
    def __init__(self, data: dict, NodeType: Anime|Manga, fields: list[AnimeField]|list[MangaField]|AnimeField|MangaField):
        self.next: str = data['paging'].get("next", None)
        self.previous: str = data['paging'].get("previous", None)
        self.__nodes: list[Media] = []

        #Paginate nodes
        for node in data['data']:
            self.nodes.append(NodeType(node['node'], fields))

    @property
    def node(self):
        '''
        Returns the first node in the pagination as its node type
        '''
        return self.__nodes[0]
    
    @property
    def nodes(self):
        '''
        Returns all nodes in the pagination as a list
        '''
        return self.__nodes

    def __repr__(self) -> str:
        return f"Pagination object with {len(self.nodes)} nodes ; next URL: {self.next} ; previous URL: {self.previous}"

    def __str__(self) -> str:
        return self.__repr__()