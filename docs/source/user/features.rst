.. _feat:

Features
========

These are the main features of the package:

**create, read and modify Freeplane mindmaps**
  at least in theory, this package
  will not touch anything it does not know within an opened mindmap. so, you
  can read big maps, change them where you like and save them without any
  information loss.

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
