# disktools
Extensions to basic disk tools like du, df, etc, but written in python.

## Installation

> pip install disktools


## Disk Usage (Cached)

*duc* is a python-based rewrite of *du*. It is relatively fast compared to its naive LLVM (numba optimized version). The main performance gain comes from using cache. Here is an example:

The output of 

```bash
duc /foo/bar
```

is equivalent to the output of


```bash
du -sb /foo/bar
```

The difference would be, that *duc* creates cache stock called **.duc** in each folder as it traverses over the file system tree, hosting all previous results for all the subfolders if there are any.

The minor caveat of such approach is that creating the **.duc** entry screws the *last modification* timestamp of the containing folder. But over time this is not important, since it happens only once. Newly cache updates do not affect the containing folder anymore. 

The idea of such caching design vs. global filesystem entry is to enable long term monitoring of any chosen sub path of your data. It has been tested to perform on XFS filesystems with volumes over 100TB and over 10 millions of files.

Any improvements and issue reports are welcomed.

---

You might also want to check out [findtools](https://github.com/ewiger/findtools)
