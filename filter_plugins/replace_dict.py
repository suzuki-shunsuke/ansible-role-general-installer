def replace_dict(src, dct):
    if isinstance(dct, dict):
        return reduce(lambda s, k: s.replace(k, dct[k]), dct, src)
    else:
        return reduce(lambda s, a: s.replace(a[0], a[1]), dct, src)


class FilterModule(object):
    def filters(self):
        return {
            "replace_dict": replace_dict}
