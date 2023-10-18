import logging
from typing import Optional, Self

from rich.logging import RichHandler


class Logger:
    """logger."""

    def __init__(
            self: Self,
            filename_: Optional[str] = None
        ) -> None:
        """initiate the logger."""

        logging.basicConfig(
            format="%(message)s",
            level=logging.INFO,
            datefmt="[%X]",
            handlers=[RichHandler()]
        ) #* logging configuration

        RichHandler.KEYWORDS: list[str] = [
                "!>>",
                "+>>",
                "[!]",
                "[>]",
                "[=]"
            ]
        self.log: object = logging.getLogger("rich")

        if filename_ is None:
            file_log: object = (
                    logging
                        .FileHandler(
                            filename="iota-2.log"
                        )
                )
        else:
            file_log: object = (
                    logging
                        .FileHandler(
                            filename=filename_
                        )
                )

        file_log.setLevel(logging.INFO)
        file_log.setFormatter(
            (
                logging
                    .Formatter(
                        "%(levelname)s %(message)s"
                    )
            )
        )
        self.log.addHandler(file_log)

    def logger(
            self: Self,
            exception_: str,
            msg: str,
            err: Optional[str] = None,
            pinfo: Optional[str] = None,
            minfo: Optional[str] = None,
            info: Optional[str] = None
        ) -> None:
        """Log the proccesses using passed message and exception_ variable.

        Inputs:
            exception_: str, determines what type of log level to use
                (a.) "error" for major error that crashed the program
                (b.) "Finfo" for failed subprocesses
                (c.) "subinfo" to simply log the happening subprocesses
                (d.) "proc_info" for major processes
                (e.) "info" for information about the process
            message: str, message to be logged.

        Output:
            None.
        """

        match exception_:
            case "E": # for major error
                self.log.error(
                    f"[!] [Err: {err}] {msg}, aborting."
                )
            case "F":
                # for failed proc, but handled by exception
                self.log.warning(
                    (
                        f"!>> [Encountered: {err}] "
                        "{message}, proceeding ..."
                    )
                )
            case "S": # normal subprocess information
                self.log.info(
                    f"+>> [{pinfo}] {msg} ..."
                )
            case "P": # for major processes
                self.log.info(
                    f"[>] [Success: {minfo}] {msg} ..."
                )
            case "I": # to print information in the terminal
                self.log.info(
                    f"[=] [{info}] {msg}."
                )
