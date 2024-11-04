# Glisco Plone Backend Framework

This documents our attempt at building the above, after many many years without
building a Plone package. With Plone 6, things might have changed a bit. 

## Python environment

As I started going through steps described below I hit some errors on buildout.
I turned to the [Plone 6 documentation][plone6docs] and installed a 
number of apparently important packages

### PyEnv

I installed the following and implemented the ~/.profile recommendations for it

```sh
curl https://pyenv.run | bash
```

### Python 

I then installed Python 3.12, as the default one (system) was 3.9. That said
I did not actually run 3.12 to install pix.

```sh
pyenv install 3.12
pip install pipx
```

### Plone Server Setup

I then went on my runtime folder, and typed 

```sh
pipx run cookiecutter gh:collective/cookiecutter-plone-starter
```

This resulted in the following output 

```pre
Cookiecutter Plone Starter 
================================================================================

Sanity checks
--------------------------------------------------------------------------------
  [1/5] Python: ✓
  [2/5] Node: ✓
  [3/5] yo: Yeoman not found.
  [4/5] Docker: ✓
  [5/5] git: ✓

Project details
--------------------------------------------------------------------------------

  [1/19] Project Title (Project Title): Plone6Runtime
  [2/19] Project Description (A new project using Plone 6.): 
  [3/19] Project Slug (Used for repository id) (plone6runtime): 
  [4/19] Project URL (without protocol) (plone6runtime.example.com): 
  [5/19] Author (Plone Foundation): Glisco Digital
  [6/19] Author E-mail (collective@plone.org): joe@glisco.io
  [7/19] Python Package Name (plone6runtime): 
  [8/19] Volto Addon Name (volto-plone6runtime): 
  [9/19] Choose a Python Test Framework
    1 - pytest
    2 - unittest
    Choose from [1/2] (1): 1
  [10/19] Plone Version (6.0.13): 
  [11/19] Should we use Volto Alpha Versions? (No): No
  [12/19] Volto Version (18.0.0): 
  [13/19] Volto Generator Version (9.0.0): 
  [14/19] Language
    1 - English
    2 - Deutsch
    3 - Español
    4 - Português (Brasil)
    5 - Nederlands
    6 - Suomi
    Choose from [1/2/3/4/5/6] (1): 1
  [15/19] GitHub or GitLab Username or Organization (collective): joemedicis
  [16/19] Container Registry
    1 - GitHub Container Registry
    2 - Docker Hub
    3 - GitLab
    Choose from [1/2/3] (1): 2
  [17/19] Should we setup a caching server?
    1 - Yes
    2 - No
    Choose from [1/2] (1): 2
  [18/19] Add Ansible playbooks?
    1 - Yes
    2 - No
    Choose from [1/2] (1): 
  [19/19] Add GitHub Action to Deploy this project?
    1 - Yes
    2 - No
    Choose from [1/2] (1): 

Plone6Runtime generation
--------------------------------------------------------------------------------

Summary:
  - Plone version: 6.0.13
  - Volto version: 18.0.0
  - Volto Generator version: 9.0.0
  - Output folder: /Users/joemedicis/Development/glisco/platform/plone6/server-side-components/runtime/plone6runtime

Frontend codebase:
 - Installing required npm packages
 - Generate frontend application with @plone/volto 18.0.0

Backend codebase
 - Remove folder src/plone6runtime/src/plone6runtime/tests not used by pytest
 - Format generated code in the backend

================================================================================

Project "Plone6Runtime" was generated
--------------------------------------------------------------------------------
Now, code it, create a git repository, push to your organization.

Sorry for the convenience,
The Plone Community.

================================================================================
```

After which I ran the following to install both the Front and Back End for 
Plone 6

```sh
make install
```

## Adding pagackages from elsewhere:



## First things first - creating the package 

It's been years since I last did something like this. The tech I used is deprecated! 
So, I'm basing my attempts on [Plone Cli][plonecli], which we first need to install:

```sh
python3 -m pip --version
python3 -m ensurepip --default-pip
```

Both commands above showed PIP3 available, which means we can install the Plone Client:

```sh
python3 -m pip install --upgrade pip
pip3 install plonecli --user
```

All these were intalled in the Pyhton3/bin folder, which I added to tha PATH var 
both on shell and on the .profile file 

```sh
export PATH=$PATH:/Users/joemedicis/Library/Python/3.9/bin
```

At this point I was able to see what kind of package I could create, by calling 

```sh
plonecli -h
plonecli -l
```

So, let's start with an add-on:

```sh
plonecli create addon src/glisco.platform.cms
```

## Building and Running the package

To build and run the package, one needs to be inside the package folder, in this 
case src/glisco.platform.cms. Once there I typed:

```sh
plonecli build
```

And that failed miserably

[plonecli]: https://pypi.org/project/plonecli/
[plone6docs]: https://6.docs.plone.org/install/create-project.html