# --- Pack/Unpack ---

def morloc_packSet(xs):
    return set(xs)

# A set has no order, so the order of its elements is unspecified in every
# form (COLL-6). Its wire form is sorted anyway: @hash and @eq read the wire
# form, and equal sets must hash and compare equal in every language, however
# each was built. The key orders values Python cannot compare directly: None
# (an absent optional) before any value, as an empty optional sorts in C++,
# and tuples element by element.
def _morloc_set_key(x):
    if x is None:
        return (0,)
    if isinstance(x, tuple):
        return (1, tuple(_morloc_set_key(e) for e in x))
    return (1, x)


def morloc_unpackSet(s):
    return sorted(s, key=_morloc_set_key)

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

def morloc_mconcat_set(xss):
    return set().union(*xss)
