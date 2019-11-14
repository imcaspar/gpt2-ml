gdown.pl
========

Google Drive direct download of big files

Requirements
============

*wget* and *Perl* must be in the PATH.   
**Windows** and **linux** compatible.

Usage
=====

Use Google Drive shareable links, viewable by anyone:   

    $ ./gdown.pl 'gdrive file url' ['desired file name']   

Example
=======

For example, to download [this video](https://drive.google.com/file/d/0B1L_hFrWJfRhLUJZdXdSdTdfSWs/edit) from my [axolotl project](https://circulosmeos.wordpress.com/2015/03/04/axolotl-a-simple-plain-text-documentation-system/), just copy the url, and give a file name if desired:

    $ ./gdown.pl https://drive.google.com/file/d/0B1L_hFrWJfRhLUJZdXdSdTdfSWs/edit axolotl.mp4   

Resuming a download
===================

If you need to resume a download, please, use [**gdown.pl v2.0** here](https://github.com/circulosmeos/gdown.pl/tree/with-resume).   
As long as a file name is indicated as second parameter, *gdown.pl v2.0* **will try to resume the partially downloaded file** if a local incomplete file with that name already exists.

Version
=======

This version is **v1.4**.

### Warning

Please, note that v1.2 (available between days 12 to 31 of Jan/2019) **should not be used**, as it contains a bug that could result in unusable downloaded files. Proceed to overwrite with v1.3 in case you have it.

Docker
======

A simple Docker file is provided, to build a simple Docker image with gdown.pl.
This has been used for pre-pulling data from a Google Drive to Kubernetes persistent volumes. Thanks @anton-khodak

License
=======

Distributed [under GPL 3](http://www.gnu.org/licenses/gpl-3.0.html)

Disclaimer
==========

This software is provided "as is", without warranty of any kind, express or implied.

More info
=========

[https://circulosmeos.wordpress.com/2014/04/12/google-drive-direct-download-of-big-files](https://circulosmeos.wordpress.com/2014/04/12/google-drive-direct-download-of-big-files)

Contact
=======

by [circulosmeos](loopidle@gmail.com)   
