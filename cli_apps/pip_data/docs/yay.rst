Yay Modules
===========

Introduction
------------
This is the part of the app where we treat *Arch's* packages information. It's a more streamlined version of *Pip's*, as we have the benefit of having done it already. The objective is to update *Pip's* modules to follow what's been done in *Yay*, but not today.
We've done away with the *package_folder* and *results* directories, by keeping everything inside lists that encompass all information. It makes for a more tight and manageable codebase.

Main
----
.. automodule:: cli_apps.yay_data.main
.. autofunction:: main

Lists
-----
.. automodule:: cli_apps.yay_data.lists
.. autoclass:: Lists

    .. automethod:: yay_lst
    .. automethod:: db_lst
    .. automethod:: yay_names

Project Creation
-----------------
.. automodule:: cli_apps.yay_data.tags.project_creation
.. autofunction:: project_creation
.. autofunction:: settings_definition
.. autofunction:: null_entries
.. autofunction:: xorg_urls
.. autofunction:: alternative_urls
.. autofunction:: name_change
.. autofunction:: spider

Spider Runner
-------------
.. automodule:: cli_apps.yay_data.tags.spider_runner
.. autofunction:: spider_runner

Keyword Creator
---------------
.. automodule:: cli_apps.yay_data.tags.kwd_creator
.. autofunction:: csv_cleaner
.. autofunction:: kwd_creator

Database Uploader
-----------------
.. automodule:: cli_apps.yay_data.db_upld
.. autofunction:: kwd_collector
.. autofunction:: db_upload

Delete
------
.. automodule:: cli_apps.yay_data.delete
.. autofunction:: delete

Cron
----
.. automodule:: cli_apps.yay_data.cront
.. autofunction:: crons

