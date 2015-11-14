# Change Log

--------------------

## 1.3.1: [Sean Chester](https://github.com/sean-chester)
 + Added conceptual generalisation whereby every merge is logged so that 
 historical states can be recalled with ../cluster_generator/cluster.py.
 + Added more parallelism (courtesy of 
 [Kenneth S Bøgh](https://dk.linkedin.com/in/kenneth-sejdenfaden-bøgh-58915524)).
 + Aliased the input parametre _c_ as _a_ to fit the conceptual generalisation 
 (while maintaining backwards compatibility).

## 1.3: [Percy Liang](https://github.com/percyliang)
 + compatibility updates for newer versions of g++ (courtesy of Chris Dyer).

## 1.2: [Percy Liang](https://github.com/percyliang)
 + make compatible with MacOS (replaced timespec with timeval and changed order of linking).
 
## 1.1: [Percy Liang](https://github.com/percyliang) 
 + Removed deprecated operators so it works with GCC 4.3.

--------------------