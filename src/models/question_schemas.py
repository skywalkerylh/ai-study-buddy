from typing import List
from pydantic import BaseModel,Field,validator


class MCQQuestion(BaseModel):
    """
    validate format of 多選題 questions
    """
    question: str = Field(description="The question text")

    options: List[str] = Field(description="List of 4 options")

    correct_answer: str = Field(description="The correct answer from the options")

    # when LLM return json object instead of text , try extracting question by key description
    @validator('question' , pre=True)
    def clean_question(cls,v):
        if isinstance(v,dict):
            return v.get('description' , str(v))
        return str(v)
    

class FillBlankQuestion(BaseModel):
    """
    validate format of 填空題 questions 
    """
    question: str = Field(description="The question text with '___' for the blank")

    answer : str = Field(description="The correct word or phrase for the blank")

    @validator('question' , pre=True)
    def clean_question(cls,v):
        if isinstance(v,dict):
            return v.get('description' , str(v))
        return str(v)
