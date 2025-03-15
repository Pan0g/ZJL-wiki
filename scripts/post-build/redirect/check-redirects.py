from glob import iglob


def getUriSet(root: str):
    rootstr = f"./{root}/"
    return set([path[len(rootstr):] for path in iglob(f"{rootstr}**/*.html", recursive=True)])


oldSet = getUriSet("old-site")
newSet = getUriSet("site")
if not newSet.issuperset(oldSet):
    print(f"Some pages are missing in new site, please update docs/_redirects")
    for p in oldSet - newSet:
        print(p)
    exit(1)
