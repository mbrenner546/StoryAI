from datetime import datetime, date
from textwrap import dedent
from typing import List, Optional

import openai
import requests
from pydantic import BaseModel, Field, Required

from textwrap import dedent

from models.story_components import StoryComponent, Realism
from models.user_models import User


class Story(BaseModel):
    story: str


def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


class StoryBuilder(BaseModel):
    name: str
    birthdate: date
    randomness: int
    story_components: List[StoryComponent] = []

    def add_story_component(self, story_component: StoryComponent):
        self.story_components.append(story_component)

    def add_story_component(self, story_components: List[StoryComponent]):
        for story_component in story_components:
            self.story_components.append(story_component)

    def get_prompt(self):
        age = calculate_age(self.birthdate)
        prompt = f"""I want you to act as a storyteller. You will write a story based on information provided 
                        to you. You will adjust the story based on a degree of realism and drama You may also 
                        be given a genre. My first suggestion request is "I need help writing a story about {self.name} 
                        who is {age} years old. 
                        """
        for story_component in self.story_components:
            prompt += story_component.get_output()
        return prompt

    def generate_story(self) -> Story:
        prompt = self.get_prompt()
        openai.api_key = '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'
        max_tokens = 4097 - len(prompt)
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            temperature=self.randomness / 100,
            max_tokens=max_tokens
        )

        story = response['choices'][0]['text']
        print("PROMPT:", prompt)
        print("MAX_TOKENS:", max_tokens)
        print("STORY:", story)

        return Story(story=story)
