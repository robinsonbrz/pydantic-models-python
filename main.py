import json
from typing import List, Optional

import pydantic

import aux_functions


class ISBN10FormatError(Exception):
    """Custom error that is raised when ISBN10 doesn't have the right format."""
    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)

class Book(pydantic.BaseModel):
    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]
    
    # decorator for pydantic validator
    @pydantic.validator("isbn_10")
    @classmethod
    # isbn_10 must be 10 chars of length
    # the sum of the digits must be divisible by 11
    def isbn_10_valid(cls, value) -> None:
        """Validator to check whether ISBN10 is valid"""
        # list comprehension to validate the valid chars before calculate
        chars = [c for c in value if c in "0123456789Xx"]
        if len(chars) != 10:
            raise ISBN10FormatError(value=value, message="ISBN10 should be 10 digits.")

        def char_to_int(char: str) -> int:
            if char in "Xx":
                return 10
            return int(char)
        # the sum must be divisible by 11
        if sum((10 - i) * char_to_int(x) for i, x in enumerate(chars)) % 11 != 0:
            raise ISBN10FormatError(
                value=value, message="ISBN10 digit sum should be divisible by 11."
            )
        return value



def main() -> None:
    '''Main function'''

    # Read JSON file
    with open('./data.json') as file:
        data = json.load(file)
        # aux_functions.list_titles(data)
        # aux_functions.list_keys_values(data)
        # print(type(data[0]))
        # print(data[0])
        
        # list of books created using list comprehension
        # unpacking using keyargs**item right value to the right atribute from the Book class
        books: List[Book] = [Book(**item) for item in data]
        print("\n\n", type(books))
        # similar to data classes pydantic gives several methods to access data
        # first data
        print(books[0])

        # with pydantic you have facilitator for the fields
        # pydantic object suggest the name of the fields
        # in this case books[0] when you type . it suggests the fields
        # it doesnt happen in json

        # pydantic also helps to validate your data
        # @pydantic.validator("isbn_10")



if __name__=='__main__':
    main()
