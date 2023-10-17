from os import mkdir
from os.path import exists
from pathlib import Path
from typing import Self


class LiteratureSearch:
    def __init__(self: Self) -> None:
        """
        __init__ is a function that initiates the object
        LiteratureSearch and initiates the global variable for the
        class.
        """

        self.HOME: str = Path.home()
        self.DEFAULT_PATH: str = (
                f"{self.HOME}/in_silico/literatures"
            )
        self.DEFAULT_ITER: int = 100

    def check_stat(
            self: Self,
            link: str
        ) -> int:
        """
        Checks the status of the given link using requests module.

        Inputs:
            link: str - the link to be checked.

        Returns:
            status_code: int - the status of checked link
        """

        pass

    def eval_stat(
            self: Self,
            status_code: int
        ) -> bool:
        """
        Evaluates the status code given as an input.

        Input:
            status_code: int - status of the checked link.

        Returns:
            link_status: bool - whether the link is accessible
                or not.
        """

        if status_code in [num for num in range(200)]:
            return True

        return False

    def def_val(
            self: Self,
            keywords: str,
            iterations: int,
            path: str
        ) -> int | tuple[list, int, str]:
        """
        sets the default value of the arguments of function.

        Inputs:
            keywords: arr - an array of keywords with different
                permutations.
            iterations: int - takes the number that defines the count
                of iteration per run of function.
            path: str - where to save the fetched literatures.

        returns:
            int - indicates the status of function after run
            keywords, iterations, path: tuple[
                    list,
                    int,
                    str
                ] - the assigned default values.
        """


        #* set default values
        if path is None:
            for _ in range(3):
                try:
                    if not exists(self.DEFAULT_PATH):
                        raise FileNotFoundError
                except (
                        NotADirectoryError,
                        PermissionError,
                        FileNotFoundError
                    ):
                    mkdir(self.DEFAULT_PATH)
                    continue
                except OSError:
                    return 0
                finally:
                    path = self.DEFAULT_PATH

        if iterations == 0:
            iterations = self.DEFAULT_ITER

        #! return if there is no keyword
        if not all(keywords):
            return 0

        return (keywords, iterations, path)

    def literature_search(
            self: Self,
            keywords: str = [],
            iterations: int = 0,
            path: str = None
        ) -> int:
        """
        literature_search() fetches the literature from databases
        such as pubmed and nih.

        Inputs:
            keywords: arr - an array of keywords with different
                permutations.
            iterations: int - takes the number that defines the count
                of iteration per run of function.
            path: str - where to save the fetched literatures.

        Returns:
            status_code: int - indicates the status of function after run
        """

        func_args: tuple[
                list,
                int,
                str
            ] | int = self.def_val(
                keywords,
                iterations,
                path
            )

        match func_args:
            case tuple():
                pass
            case 0, _:
                return 0





