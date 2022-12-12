import sqlite3


def get_all(query: str):
    """

    :param query:
    :return:
    """
    with sqlite3.connect('netflix.db') as conn:
        conn.row_factory = sqlite3.Row
        result = []

        for item in conn.execute(query).fetchall():
            print(item)
            s = dict(item)

            result.append(s)

        return result


def get_one(query: str):
    """

    :param query:
    :return:
    """
    with sqlite3.connect('netflix.db') as conn:
        conn.row_factory = sqlite3.Row
        result = dict(conn.execute(query).fetchone())

        if result is None:
            return None
        else:
            return dict(result)


def search_by_cast(name1: str, name2: str):
    query = f"""
    SELECT * FROM netflix
    WHERE "cast" LIKE '%{name1}%' and "cast" LIKE '%{name2}%';
    """

    cast = []

    result = get_all(query)
    for item in result:
        if result is None:
            return None
        else:
            cast.append(item)
            return dict(cast)


def search_by_settings(type: str, release_year: str, listed_in):
    query = f"""
    SELECT * FROM netflix
    WHERE "type" LIKE '%{type}%' and "release_year" LIKE '%{release_year}%' and "listed_in" LIKE '%{listed_in}%';
    """

    res = []

    result = get_all(query)
    for item in result:
        if result is None:
            return None
        else:
            res.append(item)
            return res


search_by_cast('Rose McIver', 'Ben Lamb')