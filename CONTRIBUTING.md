# Contribution Guidelines

Please note that this project is released with a
[Contributor Code of Conduct](CODE-OF-CONDUCT.md). By participating in this
project you agree to abide by its terms.  You will also need to sign our
[Contributor License Agreement](ChaoSlingr%20CLA%20September%202017.pdf) prior to
submitting any changes to the project. Once completed, the agreement should be
emailed to [opensource@optum.com][email].

---

# How to Contribute

Now that we have the disclaimer out of the way, let's get into how you can be a
part of our project. There are many different ways to contribute.

## Issues

We track our work using Issues in GitHub. Feel free to open up your own issue
to point out areas for improvement or to suggest your own new experiment. If you
are comfortable with signing the waiver linked above and contributing code or
documentation, grab your own issue and start working.

## Coding Standards

We have some general coding guidelines to help ensure consistency in our project.

### Languages

*Python*

The source code for this project is written in Python. While it is possible to
write Lambda functions in many different languages, you will be asked to rewrite
them in Python if you submit an experiment written in another language.

*Terraform*

Terraform is the preferred language to use when spinning up temporary assets in
AWS to be used in unit testing.

*Scripting*

Our test scripts are written in a combination of Python and Bash.

### Experiment Naming

* Every component for a particular experiment should have the same prefix.
* Names should have the first letter of the words capitalized with an underscore
separating the name of the experiment from the name of the component.
* Naming for Trackr additionally contains information on which type of logging
is being performed.
* Lambda functions should contain the .py extension to dentote that they contain
Python code.

### Components

Each experiment consists of three main components and an associated documentation
file.  Please ensure that you have all four when submitting a new experiment.

*Generatr*

Generatr selects the misconfiguration to attempt and calls Slingr. Example:
[PortChange_Generatr.py](src/lambda/PortChange_Generatr.py)

*Slingr*

Slingr attempts the misconfiguration. Example:
[PortChange_Slingr.py](src/lambda/PortChange_Slingr.py)

*Trackr*

Trackr logs details about the misconfiguration being made. Example:
[PortChange_Slack_Trackr.py](src/lambda/PortChange_Slack_Trackr.py)

*Experiment Description*

This document provides information about the experiment along with applicable
input and output parameters for the various Lambda functions.  Example:
[PortChange.md](src/lambda/PortChange.md)

### Documentation

* High-level project documentation can be found in the [docs](docs) folder at the
root of the repository.
* Documentation specific to experiments should be included under [src/lambda](src/lambda)
at the same level as the Lambda functions being described.

## Pull Requests

If you've gotten as far as reading this section, then thank you for your
suggestions.

### General Guidelines

Ensure your pull request (PR) adheres to the following guidelines:

* Try to make the name concise and descriptive.
* Give a good description of the change being made.  Since this is very
subjective, see the [Updating Your Pull Request (PR)](#updating-your-pull-request-pr)
section below for further details.
* Every pull request should be associated with one or more issues.  If no issue
exists yet, please create your own.
* Make sure that all applicable issues are mentioned somewhere in the PR description.  This
can be done by typing # to bring up a list of issues.

### Updating Your Pull Request (PR)

A lot of times, making a PR adhere to the standards above can be difficult.
If the maintainers notice anything that we'd like changed, we'll ask you to
edit your PR before we merge it. This applies to both the content documented
in the PR and the changed contained within the branch being merged.  There's no
need to open a new PR. Just edit the existing one.

[email]: mailto:opensource@optum.com
