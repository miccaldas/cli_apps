Pip Modules
===========


Introduction
------------
This is the place where we update and maintain all the database entries that come from *Pip*. We have the usual CRUD functionalities, we even had a bespoke app to access the db once. But it soon turned obvious that most of the interactiosn would be autommatic, and there was no reason to maintain an app that nobody used. Not even me. The main tasks here is information sourcing, data cleaning and database upkeep. Quite possibly in that order. But the module's presentation will clear up what we do here.

Initiation Scripts
------------------

.. automodule:: cli_apps.pip_data.initiation_scripts
.. autofunction:: initiation_scripts

Query Builder
-------------

.. automodule:: cli_apps.pip_data.query_builder
.. autofunction:: query_builder

Extract File Info
------------------

.. automodule:: cli_apps.pip_data.extract_file_info
.. autofunction:: extract_file_info

Pip's Project Creation
----------------------
.. automodule:: cli_apps.pip_data.tags.project_creation
.. autofunction:: project_creation
.. autofunction:: settings_definition
.. autofunction:: xorg_urls
.. autofunction:: name_change
.. autofunction:: spider

Pip's Keyword Creation
----------------------
.. automodule:: cli_apps.pip_data.tags.kwd_creator
.. autofunction:: csv_cleaner
.. autofunction:: kwd_creator

Pip's Spider Runner
-------------------
.. automodule:: cli_apps.pip_data.tags.spider_runner
.. autofunction:: spider_runner

Database Upload
---------------

.. automodule:: cli_apps.pip_data.db_upld
.. autofunction:: kwd_collector
.. autofunction:: db_upload

Delete
------

.. automodule:: cli_apps.pip_data.delete
.. autofunction:: delete

Cron
----

.. automodule:: cli_apps.pip_data.cron
.. autofunction:: cron

App Reminder
------------

.. automodule:: cli_apps.pip_data.app_reminder
.. autofunction:: app_reminder
