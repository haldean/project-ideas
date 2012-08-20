WebRAID
#######

Overview
========================================
Most people have access to a number of web services online that give
them a certain amount of free storage, but there's no way to manage all
of them at once, and no way to take advantage of the opportunities for
redundant backups that they provide. To get around this, a system could
be created to treat each of these services as a disk in a RAID array.
Doing so would provide users with all of the advantages of a RAID array:

* Fast parallel reads.
* Redundant backups (from R=2 up to R=N, where N is number of services)
* Ability to treat multiple storage providers as a single virtual disk.

Implementation
========================================

File table
----------------------------------------
The file table is responsible for mapping files to the locations of the blocks
in which the file is stored. This file is synced across all services along with
a hash of the file. It is also synced to the users computer; this is important
as losing the file table means losing access to all of your files.  The file
table also stores which RAID level is used for WebRAID (detailed below). The
RAID level can be changed after setting up WebRAID, but it requires a complete
reindexing of documents, and thus requires enough local space to store all of
the files in WebRAID, along with the necessary bandwidth to download and upload
all data.

Storing files
----------------------------------------
The file is written into multiple blocks, each of which is indexed. Then,
depending on which RAID level is in use, these blocks are written to
various services. The location and index of each block are stored in the
file table, i.e.:

::

        doc1    0       dropbox         [dropbox url]
        doc1    1       gdrive          [gdrive id]
        doc1    P       github          [repo/file]

Where P is used to mean "parity", which is an xor of all other chunks when
applicable (parity blocks are used in RAID levels 4, 5 and 6).

Optionally, the user can set up transparent compression on their files
that are saved, with the downside of increasing read and write times.

How exactly the files are chunked and stored depends on the RAID level WebRAID
is configured for.  (For more information about the different levels of RAID,
see `RAID - Standard levels <http://en.wikipedia.org/wiki/RAID#Standard_levels>`_.

========== ================================================================================
RAID level Write mode
---------- --------------------------------------------------------------------------------
RAID-0     Split into N blocks, write a block to each backend.
RAID-1     Write full file to each backend.
RAID-2     Unsupported
RAID-3     Unsupported
RAID-4     Split into N-1 blocks, block_N is reduce(xor, blocks).
RAID-5     Split into N-1 blocks, block_rand is reduce(xor, blocks).
RAID-6     Split into N-2 blocks, block_rand1 and block_rand2 are both reduce(xor, blocks).
========== ================================================================================

RAID-2 is unsupported as it is designed to optimize accesses on spinning
platters, which doesn't buy a performance gain on web services. RAID-3 is
unsupported as the cost of writing individual bytes to each backend comes with
too much overhead to be worthwhile.

Possible Storage Backends
========================================
I'm definitely looking for feedback here. The only requirements for a service
is that I be able to get an account for cheap or free (free preferable), and
they provide some sort of API for manipulating private data in non-negligable
sizes. If you have any suggestions for storage backends, please send me a pull
request.

Storage backends I'm currently considering:

* Dropbox
* Google Drive
* Microsoft SkyDrive
* Gmail (IMAP)
* Amazon S3
* Google Cloud Storage
* FTP server
* SCP server
* Write-to-directory
