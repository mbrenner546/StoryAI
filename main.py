from typing import List, Union

import requests
from fastapi import FastAPI, Path, Body
from enum import Enum
from datetime import date
import inspect
from models.story import StoryBuilder
from models.story_components import *
from models.user_models import *

app = FastAPI()


# story = story.generate_story()


@app.get("/")
async def root():
    return {"message": "Welcome"}


@app.post("/story_generator/")
async def create_story(name: str,
                       birthdate: date = date(1999, 1, 1),
                       best_friend: BestFriend | BestFriend = Body(embed=True),
                       genre: Genre | Genre = Body(embed=True),
                       dramatic: DramaticFactor | DramaticFactor = Body(embed=True),
                       realism: Realism | Realism = Body(embed=True),
                       sport: Sport | Sport = Body(embed=True),
                       randomness: int = 50
                       ):
    story_builder = StoryBuilder(name=name, birthdate=birthdate, randomness=randomness)
    if best_friend.active:
        story_builder.add_story_component(best_friend)
    if genre.active:
        story_builder.add_story_component(genre)
    if dramatic.active:
        story_builder.add_story_component(dramatic)
    if realism.active:
        story_builder.add_story_component(realism)
    if sport.active:
        story_builder.add_story_component(sport)
    story = story_builder.generate_story()

    return story.story


@app.get("/")
async def get_story(story_id: int):
    return {'story': story_id}
