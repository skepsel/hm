def filter_by_state(slovari: list[dict], state: str = "EXECUTED"):
    result = []
    for i in slovari:
        if i['state'] == state:
            result.append(i)
    return result


def sort_by_date(slovari: list[dict], reverse: bool = True):
    return sorted(slovari, key=lambda time: time["date"], reverse=(reverse == True))
