def get_ixes(a, b, parts):
    ixes = []
    first_elem = round((b - a) / parts + a, 2)

    ixes.append(first_elem)
    el = first_elem
    for _ in range(1, parts-1):
        el += first_elem
        ixes.append(round(el, 2))
    
    return ixes
