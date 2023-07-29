"""
Where we'll automate the process of choosing the best
links to direct to the spiders.
"""
# import os
# import subprocess
import pickle
from urllib.parse import urlparse

import snoop
from snoop import pp

from add_delete_criteria import add_delete_criteria


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])

with open("lists/pref_netloc.bin", "rb") as f:
    pref = pickle.load(f)

with open("lists/avoid_netloc.bin", "rb") as g:
    avd = pickle.load(g)


@snoop
def choices_pref_criteria():
    """
    We run the data agains our preferential
    criteria in terms of information source
    quality, and choose the ones that had
    positive results, in a new list.
    """
    choices = []
    epref = list(enumerate(pref))

    with open("app_data/0_50.bin", "rb") as h:
        split = pickle.load(h)

    # 's' is a tuple composed at index 0, by the
    # app name and at index 1 by a list of links.
    for s in split:
        # for link in list of links...
        for m in s[1]:
            # We'll parse the url to its constituints.
            ul = urlparse(m)
            # Enumerated is a better version of 'range(len())'.
            # 'pref' is a list of preffered site's.
            for i, t in enumerate(pref):
                # urlparse's site name, (netloc) is just the name
                # without 'https://' (named 'scheme' in urlparse),
                # or the path that follows. As the 'pref' values
                # have scheme values on them, we need to take them
                # out, stripping it from the begining of the string.
                if ul.netloc == pref[i][8:]:
                    # If the link is in the preffered list, we copy
                    # it as a app-name, link tuple, to another list.
                    choices.append((s[0], m))
    # We need to keep count of those that don't make the 'choice' list.
    # We still have to find information onthem. Just not this way. We'll
    # create a list that'll be 'split' minus 'choice'. We'll keep it
    # around, everytime we loose entries due to criteria.
    leftbehind = []
    nms = [a for a, b in choices]
    for i in split:
        print(i[0])
        if i[0] not in nms:
            leftbehind.append(i)

    with open("nms.bin", "wb") as d:
        pickle.dump(nms, d)

    with open("leftbehind.bin", "wb") as e:
        pickle.dump(leftbehind, e)

    with open("choices.bin", "wb") as c:
        pickle.dump(choices, c)


@snoop
def plural_entries_organization():
    """
    'choices' produces more than one result per app.
     Here we'll aggregate all results of the same program
     in sublists into a list 'plural'
    """
    with open("choices.bin", "rb") as f:
        choices = pickle.load(f)

    gits = []
    temp = []

    # We manually noticed that all Github results for this cohort are shitty.
    # We'll pull all results of github that are related to 'issues' or that
    # don't have the app's name in the url. This last one is risky as the
    # executable might be inside a package with another name, but we have to
    # have some sort of criteria.
    for c in choices:
        uc = urlparse(c[1])
        if uc.netloc == "github.com":
            if "issues" not in uc.path:
                if c[0] in uc.path:
                    gits.append(c)
    # We create a new lists with all entries of 'choice' that didn't have 'github'
    # on their links. The idea is to merge this list with the 'gits' list.
    for c in choices:
        uc = urlparse(c[1])
        if uc.netloc != "github.com":
            temp.append(c)
    temp += gits
    # As to be expected, 'choices' produced more than one aproved link per program.
    # To organize the information, we'll collect all links for a program in one sublist.
    per_name = []
    # The program names are at index 0 in a tuple. We gather the names to facilitate the
    # creation of sublists with the criteria that the entries must have the same app name.
    appnames = [v[0] for v in temp]
    # Although this gives us the names, it gives us all entries index 0 content, which means
    # that we have several entries with the same app name. We'll use set() to cull it to just
    # entry per app.
    sapp = set(appnames)
    # I'm not very confortable with sets. Best to turn it back to a list.
    apps = list(sapp)
    # For each entry in the app names list; look for tuples in 'temp' that have the same name in
    # position 0.
    for app in sapp:
        sublst = [e for e in temp if e[0] == app]
        per_name.append(sublst)
    # For the apps that have more than one link, we'll have to choose one. To start we isolate
    # the entries with more than one link in a list.
    plural = []
    for i, t in enumerate(per_name):
        if len(per_name[i]) > 1:
            plural.append(t)
    # These are the apps left behind. Kept here.
    individual = [i for i in per_name if i not in plural]

    with open("plural.bin", "wb") as v:
        pickle.dump(plural, v)

    with open("individual.bin", "wb") as g:
        pickle.dump(plural, g)


@snoop
def get_index_positions():
    """
    Calculates the index value where the app's name
    appears in the link.
    We're going to see how near the start in link is
    the mention of the program. The reasoning that
    closeness to the site's name indicates that is an
    important part of the site. We'll do this using
    the string method find(). It looks for a substring
    in a string and if it finds it, it'll output the
    index number where it started.
    If it doesn't find it, outputs '-1'.
    """
    with open("plural.bin", "rb") as f:
        plural = pickle.load(f)
    spl_paths = []
    for p in plural:
        tmp = []
        for u, v in enumerate(p):
            loc = v[1].find(v[0])
            # This code shows how you append an element to a tuple.
            loctup = v + (loc,)
            tmp.append(loctup)
        spl_paths.append(tmp)

    with open("indexes.bin", "wb") as g:
        pickle.dump(spl_paths, g)


@snoop
def no_null_results():
    """
    We'll go through the index values in each app
    and remove those that don't have the app name
    in the path.
    """
    with open("indexes.bin", "rb") as f:
        idxs = pickle.load(f)

    for sublst in idxs:
        tmp = []
        if len(sublst) > 1:
            for i, t in enumerate(sublst):
                if t[2] == -1:
                    sublst.remove(t)

    with open("nonulls.bin", "wb") as g:
        pickle.dump(idxs, g)


@snoop
def finalists():
    """
    We'll ee wgo, etween those with still more
    than one path to an app, the one
    with the lowest index for name reference.
    """
    with open("nonulls.bin", "rb") as f:
        nulls = pickle.load(f)

    with open("nms.bin", "rb") as d:
        nms = pickle.load(d)

    # We'll begin by taking out entries that don't have the
    # app name in the path. It doesn't mean they aren't good
    # links, it's just not what we are to deal. We'll keep
    # them in a list to, later, check if there's anything
    # interesting here.
    no_mention = []
    for n in nulls:
        for t in n:
            if t[-1] == -1:
                no_mention.append(t)
    null = [i for i in nulls if i not in no_mention]
    # Now we take out entries with just one link, as there's
    # nothing to compare. As before, these links may be useful
    # so we'll keep them in a list.
    oneelement = [g for g in null if len(g) <= 1]
    with open("oneelement.bin", "wb") as g:
        pickle.dump(oneelement, g)
    # Deleting from the current list the 'onelement' elements.
    hard = [h for h in nulls if h not in oneelement]
    # From these few that still have more than one link to their
    # name, we'll find the min() value and keep that link.
    mins = []
    for h in hard:
        for t in h:
            if t[-1] != -1:
                idlst = [t[-1] for t in h]
                if min(idlst) in t:
                    mins.append(t)
    # We subtract to those initially slated for this process, the ones
    # that ended it sucessfully. This list is our next concern.
    overs = [h for h in nms if h not in mins]

    with open("overs.bin", "wb") as i:
        pickle.dump(overs, i)

    with open("finalists.bin", "wb") as j:
        pickle.dump(mins, j)


if __name__ == "__main__":
    # choices_pref_criteria()
    # plural_entries_organization()
    # # get_index_positions()
    # no_null_results()
    # finalists()
    print(pref)
