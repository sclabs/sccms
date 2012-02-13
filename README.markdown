Simple-Comic-CMS
================

<img src="http://sccms.gilgi.org/sccms.png" alt="Simple-Comic-CMS" title="Simple-Comic-CMS" height="250px" width="250px"/>

Introduction
------------

Simple-Comic-CMS (SCCMS) is a bare-bones and easy-to-customize content management system designed primarily for webcomics.

Prerequisites
-------------

- [Python 2.x](http://python.org/)
- [Django 1.x](https://www.djangoproject.com/)

Installation
------------

Make sure you have the prerequisites listed above installed. Next, [download the latest version of SCCMS](https://github.com/thomasgilgenast/Simple-Comic-CMS/zipball/master). Unzip the archive to the directory you want to run the server from.

Alternatively, you can clone the git repository by executing

    git clone git://github.com/thomasgilgenast/Simple-Comic-CMS.git

Feel free to fork the repository and develop your own tweaks and features under the conditions of the license (see below).

Quick-Start (in Five Easy Steps)
--------------------------------

1. In `settings.py`, change `SITE_TITLE` from 'My Awesome Webcomic' to whatever you actually want to call your site.
2. Run `python manage.py syncdb` and create a superuser for yourself when prompted.
3. Run `python manage.py runserver`.
4. Point your browser to <http://127.0.0.1:8000/admin/>.
5. Click on "Comics" and then "Add comic". Fill out all the fields, upload your image, and click "Save".

It's that simple! Point your browser to <http://127.0.0.1:8000> to see your comic!

Notes
-----

### Comic Upload Directory 

You can always add more comics through the admin interface as demonstrated above. The comic image files are uploaded to /media/comics on your site and the url example.com/media/comics should point to them.

### Comic Numbering

Make sure your comic numbering is consistent. Presently, SCCMS does not check to make sure that your numbering is correct. Numbering your comics incorrectly will result in broken navigation links.

Next Steps
----------

### Database Configuration

By default, SCCMS uses a sqlite database file located at the root of your site called "database.sqlite" for its database. To change this, change the DATABASES variable in settings.py, following the instructions in the comments.

### Site Themes

The templates directory contains a bare-bones example template (comic.html) that you should feel free to modify and style however you like.

### Need Help?

For more information visit <http://sccms.gilgi.org>. Direct all questions, comments, and bug reports to <sccms@gilgi.org>.

License Information
-------------------

SCCMS is released under the terms of the GNU General Public License. For details, please visit <http://www.gnu.org/licenses/gpl.html>.