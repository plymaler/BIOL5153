#! /usr/bin/env python3

# This script generates a PBS file for the AHPCC Razor cluster

# define variables
jobname = 'plymaler_BLAST'
queue = 'med16core'
prefix = jobname
num_nodes = 1
num_processors = 1
walltime = 3 # this is in hours

# This section prints the header/required info for the PBS script
# use a print statement for each line
print('#PBS -N', jobname) # job name; use comma between -N and jobname because do want space
print('#PBS -q', queue) # which queue to use; use qstat -q to get list and choose one with E and workable walltime
print('#PBS -j oe') # join the STDOUT and STDERR into a single job output file
print('#PBS -o', prefix + '.' + '$PBS_JOBID') # set the name of the job output file
print('#PBS -l nodes=' + str(num_nodes) + ':ppn=' + str(num_processors)) # how many resources to ask for
print('#PBS -l walltime=' + str(walltime) + ':00:00') # set the walltime - must not exceed queue max; use plus because don't want space; use str(wall) becuase wall is an integer
print() #add new line by putting empty print statement because print statement ends in newline
print()

# cd into working directory (where executing script from)
print('cd $PBS_O_WORKDIR')
print()

# load the necessary modules
# print code chunk bracketed with '''
print(
'''
# load modules
module purge
module load gcc/7.2.1 python/3.6.0-anaconda java/sunjdk_1.8.0
module load [program I'm running]
'''
)
print()

# commands for this job
print('# insert commands here')
