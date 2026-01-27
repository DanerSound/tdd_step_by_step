def toamericanunit( unitMeters):

    if isinstance(unitMeters, int) or isinstance(unitMeters,float):
        if unitMeters < 0:
            raise ValueError(" the input must be positive")

        collection = {
            "feet": unitMeters * 3.28084,
            "yards": unitMeters * 1.09361,
            "miles": unitMeters * 0.000621371,
        }
        return collection
    else:
        raise ValueError(" the input must be iterable")
