import logging


def get_logger(name: str = "revenue_recovery"):
    """
    Creates a standardized logger for the project.
    """

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s - %(message)s"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


logger = get_logger()
