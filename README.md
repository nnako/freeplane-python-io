# freeplane-python-io

This package provides the user a convenient way to create, read, update and
delete information stored inside Freeplan mindmap files. As an alternative or
an enhancement to working with mindmaps through the original graphical user
interface (GUI) which is provided by the brilliant Freeplane Mindmap Editor,
this package was designed to implement an application programming interface
(API) for Python as well as a command line interface (CLI) both to interact
with Freeplane mindmap files, directly.

## installation

```bash
pip install freeplane-io
```

## usage

```python
import freeplane




#
# load existing mindmap
#

# in order to access a mindmap, you first have to open it using
# the following function. please provide a valid path to your
# already existing Freeplane mindmap within the argument of the
# following function.

# load
mindmap = freeplane.Mindmap('./example_IN.mm')

# show available node styles
mindmap.styles




#
# check for GTD tasks
#

# there is a Freeplane addon "GTD+" which uses exclamation mark
# icons as identifiers for a GTD element within a Freeplane
# mindmap. In order to get a list of all these GTD elements,
# you can use the following method.

tasks = mindmap.find_nodes(icon=freeplane.ICON_EXCLAMATION)




#
# search for any core text
#

# in order to search the whole mindmap for a specific text string
# expected within the core section of a node, the following
# method can be used.

# search whole mindmap for "test"
nodes = mindmap.find_nodes(core="test", exact=True)

# search whole mindmap for "test", "tEST", ...
if not nodes:
    nodes = mindmap.find_nodes(core="test")

# get first node from list
node = nodes[0]

# printout its plain text
print(node.plaintext)




#
# write into existing mindmap
#

# modify test node's core text and color
node.plaintext = 'found and changed'

# create a test style
mindmap.add_style("test", {"bgcolor": "#999999"})

# set test style in node
node.style = "test"




#
# save mindmap
#

mindmap.save('./example_OUT.mm')
```

## the code base

### naming conventions for classes, functions, ... and variables

Using Python, developers are always encouraged to respect e.g. naming
conventions as defined in [PEP8](https://peps.python.org/pep-0008/). On the
practical side, the `freeplane-io` package is strongly related to the
functionalities implemented within the [Freeplane](https://freeplane.org/)
project (JAVA language) and accessible by its built-in Groovy scripting
environment. In effect, the `freeplane-io` package tries to provide a good
external API representation for the features, the Groovy-API provides within
the Freeplane editor. Thus, another objective is to keep this package as close
as possible to the Groovy-API. The syntax and naming will be some kind of mix.

### deliberate deviations from conventions

When browsing the code base of `freeplane-io`, you will see some deviations from
the PEP8 recommendations and from Freeplane's Groovy-API syntax. Some deviations result from the fact that the
developer was too inexperienced when he started this project, other deviations
are intentional as they help extending the machine-based readability of the
code in the way the developer likes it. One eye-catching deviation will be the representation of comments within the code. For the `freeplane-io` package, there are two distinct kinds of comments:

- **block comments** -> these comments are used as a kind of heading for the following block of code. It describes in veri few words (one line of text) what is being implemented within the next block of code.

- **concept comments** -> these multi-line comments are used to describe the implementation concept. Somtimes, it is not too obvious, how a programmer implements something. So the concept comments might help understanding.


### developing freeplane-python-io

The following steps should be performed in order to build a working local
development environment. for this, the standard dos / bash / ... console should be used.

1. clone this project into a new local project folder
   ```bash
   git clone https://...
   ```

2. create a Python virtual environment locally (make sure Python v3.x is being used, here)
   ```bash
   python -m venv env
   ```

3. install all necessary packages using pip
    ```bash
   pip install html2text

   ```

...

