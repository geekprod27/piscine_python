def give_bmi(
        height: list[int | float], weight: list[int | float]
            ) -> list[int | float]:
    """
    Docstring for give_bmi

    :param height: Description
    :type height: list[int | float]
    :param weight: Description
    :type weight: list[int | float]
    :return: Description
    :rtype: list[int | float]
    """
    try:
        if len(height) != len(weight):
            raise ValueError("height and weight have not the same len")
        bmi = []
        for h, w in zip(height, weight):
            if not (
                isinstance(h, (int, float)) and isinstance(w, (int, float))
                    ):
                raise TypeError(
                    "height and weight must be list of integer or float"
                    )
            bmi.append(w / (h ** 2))
        return bmi
    except Exception as err:
        print(f"Error: {err}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Docstring for apply_limit

    :param bmi: Description
    :type bmi: list[int | float]
    :param limit: Description
    :type limit: int
    :return: Description
    :rtype: list[bool]
    """
    limits = []
    try:
        for b in bmi:
            if not isinstance(b, (int, float)):
                raise TypeError(
                    "bmi must be list of integer or float"
                    )
            limits.append(b > limit)
        return limits
    except Exception as err:
        print(f"Error: {err}")
        return []
