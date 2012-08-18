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

Implementation Ideas
========================================

File table
----------------------------------------
The file table is responsible for mapping files to the locations of the
blocks in which the file is stored. This file is synced across all services
along with a hash of the file. It is also synced to the users computer; this
is important as losing the file table means losing access to all of your files.

Storing files
----------------------------------------
Each file is split into blocks and written to each service. How exactly this
is done depends on the configuration of WebRAID. (For more information about
the different levels of RAID, see `RAID - Standard levels
<http://en.wikipedia.org/wiki/RAID#Standard_levels>`_.

========== ================================================================================
RAID level Write mode
---------- --------------------------------------------------------------------------------
RAID-0     Split into N blocks, write a block to each service.
RAID-1     Write full file to each service.
RAID-2     Unsupported
RAID-3     Unsupported
RAID-4     Split into N-1 blocks, block_N is reduce(xor, blocks).
RAID-5     Split into N-1 blocks, block_rand is reduce(xor, blocks).
RAID-6     Split into N-2 blocks, block_rand1 and block_rand2 are both reduce(xor, blocks).

RAID-2 is unsupported as it is designed to optimize accesses on spinning
platters, which doesn't buy a performance gain on webservices. RAID-3 is
unsupported as the cost of writing a series of individual bytes to each
service comes with too much overhead to be worthwhile.
