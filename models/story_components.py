from pydantic import BaseModel


class StoryComponent(BaseModel):
    active: bool = False

    def get_output(self):
        return ''


class Realism(StoryComponent):
    scale: int = 100
    type: str = 'Realism'

    def get_output(self):
        if self.scale > 75:
            return """Please make the story very realistic."""
        if self.scale > 50:
            return """Please make the story somewhat unrealistic."""
        else:
            return """Please make the story extremely unrealistic."""


class DramaticFactor(StoryComponent):
    scale: int = 50
    type: str = 'DramaticFactor'

    def get_output(self):
        if self.scale > 75:
            return """Please make the story as dramatic as possible."""
        if self.scale > 50:
            return """Please make the story extremely dramatic."""
        else:
            return """Please make the story dramatic."""


class Sport(StoryComponent):
    sport: str
    years: int
    type: str = 'Sport'

    def get_output(self):
        prompt = f""""
        He played {self.sport} for {self.years} years.          
        """
        return prompt


class BestFriend(StoryComponent):
    name: str
    reason: str
    childhood_spot: str
    type: str = 'BestFriend'

    def get_output(self):
        prompt = f""""
        His Best Friend is named {self.name}. They are best friends because {self.reason}. 
        They used to hang out at {self.childhood_spot} 
        """
        return prompt


class Genre(StoryComponent):
    genre: str
    type: str = 'Genre'

    def get_output(self):
        prompt = f""""
        Make the Genre {self.genre}
        """
        return prompt
