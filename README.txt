Introduction
============

This product allows the display of content with *lead images* within
a Collage environment, in a Plone site.  

The typical *Summary* view for a Folder or a Collection only displays 
images for News Items, the only default type that images can be assigned 
to.  This package uses the existing 'Folder lead-image view' provided by
collective.contentleadimage and displays the content within a Collage.  Both
Folders and Collections (Topics) can have this new Collage view applied to
them.

Usage
=====

Install this product using Buildout, or a similar method, and then start up
your Plone instance.  The ZCML configuration will automatically get picked up
and register these additional views for your Collage content.  

You should install ``collective.contentleadimage`` on your site in order for
these Collage views to be useful.  Assigning some lead images to content will
also be necessary use these views to their potential.

Setting the layout
------------------

#. Create a Collage.
#. Add rows and/or columns accordingly to said Collage.
#. Add a Folder or Collection to your Collage.  This can be either actual
   content or an alias. 
#. In the *Compose* page for the Collage, locate the *Layout* link for the
   content you just added.  Click this.
#. Select *Summary (lead images)* and your new layout will appear.
#. Assign lead images to content to have them appear in this layout.

Todo
====

#. Some unit testing

