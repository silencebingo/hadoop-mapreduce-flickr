#!/bin/bash

if [ $# -ne 5 ]; then
    echo "Invalid number of parameters!"
    echo "Usage: . driver.sh [place_file_location] [photo_file_location] [output_location_1] [output_location_2] [output_location_3]"
    exit 1
fi


# task1.1 select id name typeid
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
-D stream.num.map.output.key.fields=1 \
-D mapreduce.job.maps=1 \
-D mapreduce.job.reduces=0 \
-D mapreduce.job.name='city_filter' \
-file task1_mapper1.py \
-mapper task1_mapper1.py \
-input $1 \
-output ""$3"tmpFile"

hdfs dfs -copyToLocal ""$3"tmpFile/part-00000"
hdfs dfs -rm -r -f ""$3"tmpFile"

# task1 select city number
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
-D stream.num.map.output.key.fields=1 \
-D mapreduce.job.reduces=1 \
-D mapreduce.job.name='city_to_photo' \
-files part-00000 \
-file task1_mapper2.py \
-mapper task1_mapper2.py \
-file task1_reducer1.py \
-reducer task1_reducer1.py \
-input $2 \
-output $3


# task2
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
-D stream.num.map.output.key.fields=1 \
-D stream.non.zero.exit.is.failure=false \
-D mapreduce.job.reduces=1 \
-D mapreduce.job.name='top50' \
-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D mapred.text.key.comparator.options=-nr \
-file task2_mapper1.py \
-mapper task2_mapper1.py \
-file task2_reducer1.py \
-reducer task2_reducer1.py \
-input $3 \
-output $4



# task3.1
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
-D stream.num.map.output.key.fields=1 \
-D mapreduce.job.reduces=0 \
-D mapreduce.job.name='city_to_photo_to_tag' \
-files part-00000 \
-file task3_mapper1.py \
-mapper task3_mapper1.py \
-input $2 \
-output ""$5"tmpFile1"

rm -f part-00000
hdfs dfs -copyToLocal ""$4"/part-00000"

# task 3.2
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
-D stream.num.map.output.key.fields=1 \
-D stream.non.zero.exit.is.failure=false \
-D mapreduce.job.reduces=3 \
-D mapreduce.job.name='top50_tag' \
-files part-00000 \
-file task3_mapper2.py \
-mapper task3_mapper2.py \
-file task3_reducer1.py \
-reducer task3_reducer1.py \
-input ""$5"tmpFile1" \
-output ""$5"tmpFile2"

hdfs dfs -rm -r -f ""$5"tmpFile1"
rm -f part-00000

# task 3.3
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
-D stream.num.map.output.key.fields=1 \
-D stream.non.zero.exit.is.failure=false \
-D mapreduce.job.reduces=1 \
-D mapreduce.job.name='top50_tag_sorted' \
-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D mapred.text.key.comparator.options=-nr \
-file task3_mapper3.py \
-mapper task3_mapper3.py \
-file task3_reducer2.py \
-reducer task3_reducer2.py \
-input ""$5"tmpFile2" \
-output $5

hdfs dfs -rm -r -f ""$5"tmpFile2"