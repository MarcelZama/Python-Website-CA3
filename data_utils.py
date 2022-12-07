import DBcm

config = {
    "user": "swimuser",
    "password": "swimpasswd",
    "host": "localhost",
    "database": "swimdataDB",
}


def get_swimmers_list():
    SQL = "select name from swimmers"
    with DBcm.UseDatabase(config) as db:
        db.execute(SQL)
        results = db.fetchall()  # a list of tuples.
    names = [t[0] for t in results]  # a list of names.
    return names


def get_swimmer_events(name):
    SQL = """ 
        select distinct strokes.distance, strokes.stroke
        from swimmers, strokes, times
        where times.swimmer_id = swimmers.id and
        times.stroke_id = strokes.id and
        swimmers.name = %s;
    """
    with DBcm.UseDatabase(config) as db:
        db.execute(SQL, (name,))
        results = db.fetchall()  # a list of tuples.
    events = [t[0] + "-" + t[1] for t in results]  # a list of swimming events.
    return events
