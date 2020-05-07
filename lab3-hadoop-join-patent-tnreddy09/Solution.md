# Running the Lab:
1. Create the Data Proc cluster.
2. Clone the git repo into the master node.
3. Download the input folder with the google drive link provided.
4. hdfs dfs -mkdir /user
5. hdfs dfs -mkdir /user/csci2400.anonymous
6. Copy the input folder containing patent and citation files to the hdfs.
   hdfs -dfs -put input
4. Copy the patent file to the hdfs.
5. Run the make file.

# Code Changes Explanation:

1. I have three mappers and reducers. In the first mapper I'll be merging both the input files and sorting the lines according to the Column1. In the Reducer1, I'll be extracting the state information of the 
Column1.

   cat apat63_99.txt cite75_99.txt | ./CheckCitationCountMapper.py  | sort  >  Mapper1.txt

   cat Mapper1.txt | ./CheckCitationCountReducer.py > Reducer1.txt

2. In the Mapper2, I'll be merging the input received from the Reducer1 and patent data file and in the Reducer2, I'll be extracting the state information of the other column.

   cat Reducer1.txt apat63_99.txt | ./CheckCitationCountMapper2.py | sort > Mapper2.txt

   cat Mapper2.txt | ./CheckCitationCountReducer2.py > Reducer2.txt
   
3.In the Mapper3, I'll be merging the input received from the Reducer2 and patent file, and in the Reducer3, will count the same state citations.  
   cat Reducer2.txt apat63_99.txt | ./CheckCitationCountMapper3.py | sort > Mapper3.txt

   cat Mapper3.txt | ./CheckCitationCountReducer3.py > Reducer3.txt

# Sample Output file
6004553,1999,14599,1998,"US","CA",218000,2,,424,3,31,1,0,1,,0,,10,0,0,,,0
6004554,1999,14599,1994,"US","TX",600015,2,,424,3,31,8,0,1,,0.5938,,8.75,0,0,,,0
6004555,1999,14599,1995,"US","TX",600015,2,,424,3,31,26,0,1,,0.7278,,6.3462,0,0,,,0
6004556,1999,14599,1997,"GB","",519205,2,,424,3,31,0,0,,,,,,,,,,0
6004557,1999,14599,1997,"AU","",727259,3,,424,3,31,1,0,1,,0,,1,0,0,,,1
6004558,1999,14599,1998,"AU","",762811,2,,424,3,31,4,0,1,,0.75,,6.5,0,0,,,3
6004559,1999,14599,1998,"US","AZ",748144,2,,424,3,31,5,0,0.8,,0.625,,18.2,0,0,,,0
6004560,1999,14599,1998,"TW","",,1,,424,3,31,0,0,,,,,,,,,,0
6004561,1999,14599,1997,"AT","",760012,3,,424,3,31,2,0,1,,0.5,,9,0,0,,,1
6004562,1999,14599,1996,"US","NY",471910,2,,424,3,31,0,0,,,,,,,,,,0
6004563,1999,14599,1995,"US","IA",25135,2,,424,3,31,24,0,0.8333,,0.41,,23.8333,0.1176,0.0833,,,1
6004564,1999,14599,1995,"DE","",742483,3,,424,3,31,0,0,,,,,,,,,,0
6004565,1999,14599,1997,"JP","",637670,3,,424,3,31,5,0,1,,0.32,,3.8,0.6,0.6,,,4
6004566,1999,14599,1993,"IL","",716540,2,,424,3,31,4,0,1,,0.5,,12,0,0,,,2
6004567,1999,14599,1997,"FR","",346250,3,,424,3,31,2,0,1,,0,,2,1,1,,,2
6004568,1999,14599,1997,"FR","",687499,3,,424,3,31,0,0,,,,,,,,,,0
6004569,1999,14599,1997,"US","GA",762812,2,,424,3,31,0,0,,,,,,,,,,0
6004570,1999,14599,1998,"US","PA",480850,2,,424,3,31,10,0,1,,0.58,,13.2,0,0,,,1
6004571,1999,14599,1997,"US","MO",,1,,424,3,31,5,0,1,,0.32,,12.4,,,,,0
6004572,1999,14599,1996,"US","NC",742241,2,,424,3,31,10,0,1,,0.46,,8.2,0,0,,,0
6004573,1999,14599,1997,"US","UT",717614,2,,424,3,31,9,0,1,,0.716,,9.2222,0,0,,,0
6004574,1999,14599,1996,"SE","",14910,3,,424,3,31,16,0,0.9375,,0.5244,,11.5625,0.1333,0.125,,,11
