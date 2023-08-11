"""
Module Docstring
"""
# import snoop
from ScrapeSearchEngine.ScrapeSearchEngine import Startpage

# from snoop import pp


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def websrch(entry: str) -> list[str]:
    """
    Web-searches for packages without url's.
    The next function will look for empty
    fields. If the field is 'url', this
    function it's used.
    """
    userAgent: str = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    # List of url's that usually appear in documentation but are dead links or link to internal pages.
    donts: list[str] = [
        "https://pagure.io",
        "http://www.voidspace.org.uk",
        "https://ieee1394.wiki.kernel.org",
        "https://sf.net",
        "/",
    ]
    # Words that, if inside an url, indicate site's that you can't take meaningful information.
    ins: list[str] = ["sourceforge", "canonware"]

    # Search string.
    name: str = f"{entry} python"
    # Command to make a search in 'Startpage'.
    startpage = Startpage(name, userAgent)

    # From the the default ten links found by 'startpage', if there's one from 'Github', use it and stop
    # searching. If it can't find nothing from 'Github', try from 'Pypi' and stop execution if found.
    # Finally, if the two former requisites are not met, use a link where the package name string is on the
    # link, provided the link is not on the 'donts' list, and that it none of the words in 'ins'.
    url: list[str] = []
    for s in startpage:
        if s.startswith("https://github.com"):
            url.append(s)
            break
        elif s.startswith("https://pypi.org"):
            url.append(s)
            break
        elif entry in s:
            if all(s.startswith(d) is False for d in donts):
                # This expression was written just like the above, like this:
                # 'if all(i in s is False for i in ins)'
                # evaluated to 'False' and would not go into the loop. I had
                # to change it so it would return 'True' for it to work..
                if all(i not in s for i in ins):
                    url.append(s)
                    break

    return url


if __name__ == "__main__":
    websrch()  # type: ignore[call-arg]
