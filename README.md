# Another Bug Miner (ABM)



## Getting Started

ABM requires that Python >= 3.5 is installed. The easiest way to install and
use ABM is by using a
[virtual environment](https://docs.python.org/3/library/venv.html).
Virtual environments are used to provide an independent set of Python
libraries and binaries that are isolated from those used by the system;
they can be especially useful when the default Python version on your system
doesn't meet the requirements for a particular package.
To get started, you should create a virtual environment for this project by
cloning the repository and executing the following command at its root:

```
$ python3 -m venv .
```

Now that a virtual environment has been created, we can instruct the shell to
use the environment by executing the following at the root of the repository:

```
$ . bin/activate
```

Note that you will need to execute the above command everytime that you begin
a new shell session. Once you're inside the virtual environment, you can
install (or upgrade) ABM using the command below:

```
$ pip install . --upgrade
```


## Approach

It would be easiest to implement using Python 3 and [requests](http://docs.python-requests.org/en/master/).

1.  Use the GitHub API to find the N-most popular projects on GitHub.
2.  For each project, use the GitHub API to obtain a list of pull requests.
    Write the list to a JSON file (e.g., `data/pull-requests/php.json`),
    where each pull request is described as a JSON object (pulled from
    GitHub).
3.  For each pull request (PR), determine whether that PR represents a bug fix.
    There are several ways to go about this:
      * look for an issue number in the PR description (e.g., "fixes #238").
      * use regex to look for indicative keywords (e.g., "bug" and "fix").
      * use Travis to find regressions (does the build change from failing
        to passing?)
