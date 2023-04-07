.. CliApps documentation master file, created by
   sphinx-quickstart on Tue Apr  4 19:52:06 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Cli Apps Pip Documentation
===========================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Introduction
------------
This is where it's managed the Pip's contribution to the *Cli Apps* database. The idea come about because I was getting tired of not having a clear idea of the command line tools and services in my own computer. Some I installed and forgot, some were installed for something that is not relevant anymore. Others maybe extremely interesting and I wouldn't know that they're there ... I wanted more visibility. So I started monitoring `Pip <https://pip.pypa.io/en/stable/>`_ and `Pacman <https://wiki.archlinux.org/title/pacman>`_, my two main sources of software, to understand what I had installed, what it did amd, most importantly, what I could do with it. I created a database to keep record on this things. It has the following columns:
1. Name. The name of the package.
2. Description. A brief description of the package. Usually taken from information given by these two sources.
3. URL. A link to *Github* or documentation. One of the things that interests me the most.
4. Four tag columns. I believe firmly that this thing should be easily searchable.
As you can see by analyzing these modules, the idea is to automate the databases' upkeep as much as possible. Updating is autommatic, tagging is autommatic, deleting is autommatic, etc, etc. My interventions with this service should only be to make the occasional query. But, as anyone who tried something like this know, when we try to automate, we garanty that will pass a lot of man hours building this kind of solution!
Although we're seeing *Pip's* part, there's another, virtually identical, dedicated to input coming from *Pacman* and *Yay*. But, seen one, seen'em all.

Modules
-------

.. toctree::
   tagging
   pip
   yay

External Dependencies
---------------------

* `KeyBERT <https://pypi.org/project/keybert/>`_
* `Thefuzz <https://github.com/seatgeek/thefuzz>`_
