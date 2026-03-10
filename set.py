# --- Pack/Unpack ---

def morloc_packSet(xs):
    return set(xs)

def morloc_unpackSet(s):
    return list(s)

# --- Construction ---

def morloc_singleton(x):
    return {x}

def morloc_fromList(xs):
    return set(xs)

def morloc_toList(s):
    return list(s)

# --- Query ---

def morloc_member(x, s):
    return x in s

def morloc_size(s):
    return len(s)

# --- Modify ---

def morloc_insertSet(x, s):
    return s | {x}

def morloc_deleteSet(x, s):
    return s - {x}

# --- Set Operations ---

def morloc_union(a, b):
    return a | b

def morloc_intersection(a, b):
    return a & b

def morloc_difference(a, b):
    return a - b

def morloc_symmetricDifference(a, b):
    return a ^ b

# --- Predicates ---

def morloc_isSubset(a, b):
    return a <= b

def morloc_isDisjoint(a, b):
    return a.isdisjoint(b)

# --- Transform ---

def morloc_filterSet(f, s):
    return {x for x in s if f(x)}

def morloc_mapSet(f, s):
    return {f(x) for x in s}

# --- Foldable ---

def morloc_fold_set(f, init, s):
    acc = init
    for x in s:
        acc = f(acc, x)
    return acc

def morloc_fold1_set(f, s):
    it = iter(s)
    try:
        acc = next(it)
    except StopIteration:
        raise RuntimeError("fold1 on empty set")
    for x in it:
        acc = f(acc, x)
    return acc

def morloc_safeFold1_set(f, s):
    it = iter(s)
    try:
        acc = next(it)
    except StopIteration:
        return None
    for x in it:
        acc = f(acc, x)
    return acc

# --- Monoid ---

def morloc_emptySet():
    return set()
