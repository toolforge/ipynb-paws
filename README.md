# ipynb-paws
This bit of code allows you to import a notebook from another notebook using the rendered public version we call PAWS public in [PAWS](https://wikitech.wikimedia.org/wiki/PAWS).

This is incorporated into the singleuser image at build-time.

To make this work, you can run `import paws.<user>.<notebook>` and in most cases,
you will "import" the notebook into the shell or notebook you are using in PAWS.

There are character restrictions in what python will allow you to import, so things
under the user BStorm_(WMF) cannot be imported because you cannot use parentheses
in an import in python.
