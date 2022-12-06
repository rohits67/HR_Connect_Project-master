from resources.base import ResourceBase
from utils.fetch_data import hit_url


class Planet(ResourceBase):
    """
    Planet class related functionality
    """

    def __init__(self) -> None:
        super().__init__()
        self.__relative_url = "/api/planet"

    @property
    def relative_url(self):
        return self.__relative_url

    @relative_url.setter
    def relative_url(self, new_url_):
        self.__relative_url = new_url_

    def get_count(self):
        complete_url = self.home_url + self.__relative_url
        response = hit_url(complete_url)
        data = response.json()
        count = data.get("count")
        return count




if __name__ == "__main__":
    p = Planet()
    url = p.relative_url
    print(url)

