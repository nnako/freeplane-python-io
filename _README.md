# freeplane-python-io

This package provides the user a convenient way to create, read, update and
delete information stored inside Freeplan mindmap files. As an alternative or
an enhancement to working with mindmaps through the original graphical user
interface (GUI) which is provided by the brilliant Freeplane Mindmap Editor,
this package was designed to implement an application programming interface
(API) for Python as well as a command line interface (CLI) both to interact
with Freeplane mindmap files, directly.

## features

These are the main features of the package:

- **create, read and modify Freeplane mindmaps**<br>at least in theory, this package
  will not touch anything it does not know within an opened mindmap. so, you
  can read big maps, change them where you like and save them without any
  information loss.

- **transparent handling of different mindmap file versions**<br>different freeplane file
  versions are handled seamlessly. even old Freemind mindmaps should work.

- **management of each node's creation and modification dates**<br>dates will be
  translated into human-readable date strings. when creating or modifying nodes,
  the correct dates will be set.

- **search and find nodes within a mindmap**<br>based on the node's id, core text,
  attributes, details, notes, link or icons any node can be found within a mindmap
  using the mindmap's or node's `find_nodes` or `find_children` methods.

- **navigate through the mindmap trees**<br>based on the node object's `parent`,
  `children`, `next` and `get_child_by_index` attributes / methods it is possible
  to reach every node from every starting point within the mindmap.

- **modify information within arbitrary nodes**<br>the original attributes of each
  node (core text / html as `plaintext`, `notes`, `details`, `link`, `icons`, ...) can
  be read and modified. by using the node's `set_attribute`, `get_attribute` and
  `attribute` methods, the Freeplane' node attributes can be accessed.

- **manage node links**<br>hyperlinks between nodes within the same mindmap as well
  as accross different mindmaps are dealt with by using the `hyperlink` attribute
  of a node object.

- **set and manage node styles**<br>in Freeplane, "styles" are used to set and manage
  the design of nodes. using the `styles` attribute and the `add_style` attribute of
  a map object or the `style` attribute of a node object, the management is done.

- **create and manage arrow links**<br>besides hyperlinks, "arrow links" can be used
  to connect nodes on (this time on a visual level). the node object's
  `add_arrowlink` method helps connecting nodes visually.

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

