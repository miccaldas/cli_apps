Tagging Modules
===============

Introduction
------------
Getting good quality tags for the *cli_apps* database is always a problem. Due to its size, it's not feasible that they're produced in a non-automated way. In our
last update, there were more than a hundred new packages in the database, from *Pip* alone!  

So there's always a concern on how to turn this application searchable. Quality that, if it's lacking, defeats its all purpose.  

I've been experimenting with different sources of text, that would could be mined for keywords. In the beginning I used the *presentation* field in *Pacman*, or the *Summary* in *Pip*. But these are very limited bases to go on. Surely a longer, richer text source would yield better results.  
That brought me to the idea of scraping the *Github* or documentation pages of these packages, in order to gain some more insight. The URL's are generally available through *Pacman* and *Pip*, so that's not too difficult.
All this said, this is my current procedure:

1. Gather information. With:

   .. code-block:: python
        
        Pip show <package_name>

        sudo Pacman -Qi <package_name>

for *Pip's* and *Pacman's* packages.

2. From the resulting information, we cull these points:

2.1. Name of Package.

2.2. Description.

2.3. URL for documentation.

With this information, I set about to extract the keywords. For a keyword extractor I'm using `Keybert <https://github.com/MaartenGr/KeyBERT>`_, a simple and minimal keyword tool, with which I've been having the best results from of all that I tried.
I'm also using `Thefuzz <https://github.com/seatgeek/thefuzz>`_, a string matching tool, to weed out very similar results. *KeyBERT* has, theoritically, the tools to do the same. But when I tried them, the results were very bad. It's something I'll have to revisit shortly.
With all this done, it's just a matter of uploading to the database and, although I'm much happier than I previously was, there's still a lot of work to be done in this regard. Probably what's needed is multi-page thourough scrape of all available pages, so as to have an even bigger base. Maybe use a more beefy model. Something that'll have to train ... I don't know.

Still a work in progress!

Tagging Structure
---------------------

.. image:: workflow.png

Project Creation
----------------

.. automodule:: cli_apps.pip_data.tags.project_creation
.. autofunction:: project_creation
.. autofunction:: settings_definition
.. autofunction:: spider
.. autofunction:: name_change
.. autofunction:: xorg_urls

Spider Runner
-------------

.. automodule:: cli_apps.pip_data.tags.spider_runner
.. autofunction:: spider_runner

Keyword Creator
----------------

.. automodule:: cli_apps.pip_data.tags.kwd_creator
.. autofunction:: csv_cleaner
.. autofunction:: kwd_creator

Keyword Uploader
-----------------

.. automodule:: cli_apps.newtags.yay_newtags.kwd_uploader
.. autofunction:: kwd_uploader


