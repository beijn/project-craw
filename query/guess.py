from lib.Chain import Chain

from pydantic import BaseModel, Field


instructions = """Answer the user's Query to your best knowledge.
"""

class Output(BaseModel):
    trust  : str  = Field(description="How much you are sure about the answer. If you blindly guessed, state it here.")
    answer : str  = Field(description='The answer guessed from inside the model.')



chain = Chain('guess', instructions, Output)