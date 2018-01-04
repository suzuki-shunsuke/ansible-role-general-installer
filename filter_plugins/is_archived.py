def is_archived(filename, suffixes):
    """
    """
    return any(filename.endswith(s) for s in suffixes)


class FilterModule(object):
    def filters(self):
        return {
            "is_archived": is_archived}
