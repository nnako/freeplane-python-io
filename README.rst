freeplane-python-io
===================

This package provides the user a convenient way to create, read, update and
delete information stored inside Freeplan mindmap files. As an alternative or
an enhancement to working with mindmaps through the original graphical user
interface (GUI) which is provided by the brilliant Freeplane Mindmap Editor,
this package was designed to implement an application programming interface
(API) for Python as well as a command line interface (CLI) both to interact
with Freeplane mindmap files, directly.


These are the main features of the package:

+------------+------------+
| feature    | description   |
+============+============+
| Eintrag A  | Eintrag B  |
+------------+------------+
| Eintrag C  | Eintrag D  |
+------------+------------+
| **create, read and modify Freeplane mindmaps** | at least in theory, this package will not touch anything it does not know within an opened mindmap. so, you can read big maps, change them where you like and save them without any information loss. |
+-----------+--------+

**transparent handling of different mindmap file versions**
  different freeplane file
  versions are handled seamlessly. even old Freemind mindmaps should work.

**management of each node's creation and modification dates**
  dates will be
  translated into human-readable date strings. when creating or modifying nodes,
  the correct dates will be set.

**search and find nodes within a mindmap**
  based on the node's id, core text,
  attributes, details, notes, link or icons any node can be found within a mindmap
  using the mindmap's or node's `find_nodes` or `find_children` methods.

**navigate through the mindmap trees**
  based on the node object's `parent`,
  `children`, `next` and `get_child_by_index` attributes / methods it is possible
  to reach every node from every starting point within the mindmap.

**modify information within arbitrary nodes**
  the original attributes of each
  node (core text / html as `plaintext`, `notes`, `details`, `link`, `icons`, ...) can
  be read and modified. by using the node's `set_attribute`, `get_attribute` and
  `attribute` methods, the Freeplane' node attributes can be accessed.

**manage node links**
  hyperlinks between nodes within the same mindmap as well
  as accross different mindmaps are dealt with by using the `hyperlink` attribute
  of a node object.

**set and manage node styles**
  in Freeplane, "styles" are used to set and manage
  the design of nodes. using the `styles` attribute and the `add_style` attribute of
  a map object or the `style` attribute of a node object, the management is done.

**create and manage arrow links**
  besides hyperlinks, "arrow links" can be used
  to connect nodes on (this time on a visual level). the node object's
  `add_arrowlink` method helps connecting nodes visually.

**work with encrypted nodes**
  if you own appropriate passwords, you can encrypt and decrypt nodes / trees
  according to the PBEWithMD5AndAES algorithm which is used also inside the Freeplane
  editor.


installation
------------

.. code:: bash

    pip install freeplane-io


usage
-----

.. code:: python

    import freeplane




    #
    # load existing mindmap
    #

    # in order to access a mindmap, you first have to open it using
    # the following function. please provide a valid path to your
    # already existing Freeplane mindmap within the argument of the
    # following function.

    # load
    mindmap = freeplane.Mindmap('./examples/example_IN.mm')

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

    # search whole mindmap with regular expression
    if not nodes:
        nodes = mindmap.find_nodes(core=r"t[a-z]+t", regex=True)

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
    # handle encrypted nodes
    #

    # read a mindmap containing encrypted nodes
    mm = freeplane.Mindmap("./tests/mm_encryption.mm")

    # get one of those nodes. in the example, the nodes are identified by a
    # core text starting with "this is...". the first node is encrypted using the
    # password "test1", the 2nd one using "test".

    nodes = mm.find_nodes(core="this is")
    if len(nodes):

      # show the number of hits
      print(f"number of nodes found: {len(nodes)}")

      # get the 1st node
      node = nodes[0]

      # remove the node's encryption
      success = node.decrypt("test1")

      # now, search for "this is" again on a map level and see that there are
      # more than 2 hits, as the decrypted node / tree contains another node
      # fitting to this search.

      if success:

        # search for nodes
        nodes = mm.find_nodes(core="this is")

        # again, show the number of hits
        print(f"number of nodes found: {len(nodes)}")

        # now, remove the password. when a valid password is chosen, it would
        # be set accordingly. and the respective node would be decryptable via
        # the Freeplane editor.

        node.set_encryption_password("")

        # save the mindmap and check
        mm.save("./tests/mm_encryption.mm")



    #
    # save mindmap
    #

    mindmap.save('./example_OUT.mm')




development
-------------

As a user of this package or a developer, you are welcome to contribute to this
project. Contribution may happen in different ways. Here are a couple of
examples:

- **use the features** within your own application and **create an issue** if you want something fixed.

- create a new issue to announce and discuss **an idea**, or ask **a question**.

- **create an issue** if you want something changed. Your request will be openly discussed and might lead into a code change.

- **create a unittest** if you see some feature has not been tested, yet. See unittesting_ for details.

- **create a new feature** if you want to add more features. Please, discuss it, first. I might support you.


_`unittesting`
-----------

If you want to test your locally changed code, please add a **unittest** for
the changed aspect of the respective feature and test that aspect, before you
create a **pull request** for integrating both, the tests and the changes into
the code base. Here is the structure to be respected when working with tests:

::

    +-------+
    + Box   +
    +-------+

    ... here comes an ASCII diagram

.. graphviz::

   digraph G {
    A -> B;
    B -> C;


documentation
-------------

For more information, please visit our documentation_ at ReadTheDocs.

.. _documentation: https://freeplane-python-io.readthedocs.io/en/latest/

