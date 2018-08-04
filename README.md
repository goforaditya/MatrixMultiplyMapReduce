## Matrix Multiplication Using MapReduce over HDFS

In the following example we will learn to multiply two matrices which are stored over HDFS in the given structure. If you are new to Hadoop please try the [wordcount example](https://github.com/AdityaSinghRathore/WordCountHadoop) first.

```
A,0,0,63
A,0,1,45
A,0,2,93
A,0,3,32
A,0,4,49
A,1,0,33
A,1,3,26
A,1,4,95
A,2,0,25
A,2,1,11
A,2,3,60
A,2,4,89
A,3,0,24
A,3,1,79
A,3,2,24
A,3,3,47
A,3,4,18
A,4,0,7
A,4,1,98
A,4,2,96
A,4,3,27
B,0,0,63
B,0,1,18
B,0,2,89
B,0,3,28
B,0,4,39
B,1,0,59
B,1,1,76
B,1,2,34
B,1,3,12
B,1,4,6
B,2,0,30
B,2,1,52
B,2,2,49
B,2,3,3
B,2,4,95
B,3,0,77
B,3,1,75
B,3,2,85
B,4,1,46
B,4,2,33
B,4,3,69
B,4,4,88
```
Where each row in trhe dataset represents
<Matrix_Name>, &lt;Row&gt;, &lt;Column&gt;, &lt;Value&gt;

1. Data is stored in the file input.txt (given above for download) or simply do.
```
$ touch input.txt
$ vi input.txt
```
![](https://github.com/AdityaSinghRathore/MatrixMultiplyMapReduce/blob/master/img/0inputcre.png)
![](https://github.com/AdityaSinghRathore/MatrixMultiplyMapReduce/blob/master/img/01inputin.png)

2. Now Create our Mapper in Python.
[Code for Mapper](https://github.com/AdityaSinghRathore/MatrixMultiplyMapReduce/blob/master/mapper.py)
```
$ touch mapper.py
$ vi mapper.py
```
![](https://github.com/AdityaSinghRathore/MatrixMultiplyMapReduce/blob/master/img/2mapper.png)

3. Now Create our reducer (Code is avaliable in repo. for ***Download*** if it is not visible)
```
$ touch reducer.py
$ vi reducer.py
```
[Code for Reducer](https://github.com/AdityaSinghRathore/MatrixMultiplyMapReduce/blob/master/reducer.py)
![](https://github.com/AdityaSinghRathore/MatrixMultiplyMapReduce/blob/master/img/3reducerpy.png)

4. We try our code by running it locally
```
$ cat input.txt | python mapper.py | sort | python reducer.py
```
![](https://github.com/AdityaSinghRathore/MatrixMultiplyMapReduce/blob/master/img/4localrun.png)

5. Now we start Hadoop Cluster and transfer ***input.txt*** from local to ***HDFS*** storage for that we will create an input directory for matrix multiply example.
```
$ ssh localhost
$ start-dfs.sh
$ start-yarn.sh
$ hadoop fs -mkdir /user/aditya/matrix/
$ hadoop fs -mkdir /user/aditya/matrix/input
$ hadoop fs -put input.txt /user/aditya/matrix/input
```
![](https://github.com/AdityaSinghRathore/MatrixMultiplyMapReduce/blob/master/img/5hdcreatedir.png)

6. Now all that is left to do is to use ***mapreduce streaming*** and run our exaple over the input folder.
```
$ mapred streaming -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input /user/aditya/matrixm/input -output /user/aditya/matrixm/output

```
![](https://github.com/AdityaSinghRathore/MatrixMultiplyMapReduce/blob/master/img/6mapredrun.png)

Your job is now running

7. To see your final output. (ignore matrixm and use matrix directory)
```
$ hadoop fs -cat /user/aditya/matrix/output/*
```
![](https://github.com/AdityaSinghRathore/MatrixMultiplyMapReduce/blob/master/img/7finaloutput.png)

