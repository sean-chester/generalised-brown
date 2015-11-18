## generalised-brown
version 1.0
© 2015 Sean Chester and Leon Derczynski

-------------------------------------------
### Table of Contents 

  * [Introduction](#introduction)
  * [Requirements](#requirements)
  * [Installation](#installation)
  * [Usage](#usage)
  * [License](#license)
  * [Contact](#contact)
  

------------------------------------
### Introduction
<a name="introduction" ></a>

The *generalised-brown* software suite clusters word types by 
distributional similarity in two phases. It first generates a list 
of merges based on the well-known Brown clustering algorithm and 
then recalls historical states to vary the granularity of the
clusters. For example, given the following corpus:

> Alice likes dogs and Bob likes cats while Alice hates snakes and Bob hates spiders

Greedily clustering word types based on *average mutual information* 
(i.e., running the *C++ merge generator*) produces the following 
merge list (assuming _a_ = _|V|_ = 10):

> snakes spiders 8

> dogs cats 7

> Alice Bob 6

> and while 5

> likes hates 4

> dogs snakes 3

> dogs and 2

> dogs Alice 1

> dogs likes 0

One can then recall any historical state of the computation in order to 
produce a set of clusters (i.e., run the *python cluster generator*).
For example, with _c_ = 5, we recall the state _c_ - 1 = 4 to produce 
the following clusters:

> {snakes, spiders}
> {dogs, cats}
> {Alice, Bob}
> {likes, hates}
> {and, while}

This approach (setting separate values of _a_ and _c_) we refer to as 
*Roll-up feature generation*. By contrast, traditional Brown clustering 
would produce the following five clusters (equivalent to running the 
*C++ merge generator* with _a_ = 5 **and** the *python cluster generator* 
with _c_ = 5):

> {likes, hates}
> {snakes, spiders, cats, dogs}
> {and, while}
> {Alice}
> {Bob}

For details about the concepts implemented in this software, please 
read our recent AAAI paper:

> L. Derczynski and S. Chester. 2016. "Generalised Brown Clustering 
>   and Roll-up Feature Generation." In: Proceedings of the 
>   Thirtieth AAAI Conference on Artificial Intelligence (AAAI-16). 
>		7 pages. To appear.

For details about traditional Brown clustering, consult the article 
in which it was introduced:

> PF Brown et al. 1992. "Class-based n-gram models of natural language."
>   Computational Linguistics 18(4): 467--479.

or the implementation that our *C++ merge generator* forked:  

> [wcluster](https://github.com/percyliang/brown-cluster).


------------------------------------
### Requirements
<a name="requirements" ></a>

*generalised-brown* relies on the following applications:

 + For compiling the *C++ merge generator*: A C++ compiler that 
 is compatible with C++ 11 and OpenMP (e.g., the newest 
 [GNU compiler](https://gcc.gnu.org/)) and the *make* program

 + For running the *python cluster generator*: A *python* 
 interpreter

------------------------------------
### Installation
<a name="installation" ></a>

The *python cluster generator* does not need to be compiled.
To compile the *C++ merge generator*, navigate to the 
*merge_generator/* subdirectory of the project and type:

>make

------------------------------------
### Usage
<a name="usage" ></a>

To produce a set of features for a corpus, you will first want to use 
Generalised Brown (i.e., the *C++ merge generator*) to create a merge list. 
Then, you can create c clusters by running the *python cluster generator* 
on the merge list. This second step can be done for as many values of _c_ 
as you like, but we recommend that each value of _c_ is not larger than the 
value of _a_ used to generate the merge list.

To run the *C++ merge generator*, type:

>./merge_generator/wcluster --text [input_file] --a [active_set_size]

The resultant merges will be recorded in:

>./[input_file]-c[active_set_size]-p1.out/merges

To run the *python cluster generator*, type:

>python ./cluster_generator/cluster.py -in ./[input_file]-c[active_set_size]-p1.out/merges -c 3

Each word type will be printed to *stdout* with its cluster id.

The *C++ merge generator* runs in _O(|V| a^2)_ time, where _|V|_ is the number 
of distinct word types in the corpus (i.e., the size of the vocabulary) and 
_a_ is a bound on the algorithm's search space. The *python cluster generator* 
runs in _O(|V|)_ time.
  

------------------------------------
### License
<a name="license"></a>

This software consists of two sub-modules, each released under a 
different license: 

 + The *python cluster generator* is subject to the terms of 
[The MIT License](http://opensource.org/licenses/MIT) 

 + The *C++ merge generator* follows the original licensing terms  
of [wcluster](https://github.com/percyliang/brown-cluster). 

See the relevant sub-directories of this repository for the 
specific details of each license.



------------------------------------
### Contact
<a name="contact"></a>

This software suite will undergo a major revision; so, you are encouraged 
to ensure that this is still the latest version. Please do not hesitate to 
contact the authors if you have comments, questions, or bugs to report.
>[generalised-brown on GitHub](https://github.com/sean-chester/generalised-brown) 

------------------------------------