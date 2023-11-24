def solution(data, ext, val_ext, sort_by):
    by = ["code", "date", "maximum", "remain"]

    return sorted(filter(lambda x: x[by.index(ext)] < val_ext, data), key=lambda x: x[by.index(sort_by)])
