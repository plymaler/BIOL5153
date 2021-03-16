#! /usr/bin/env python3

# This script generates a slurm script for the AHPCC Pinnacle cluster

# define variables
jobname = 'plymaler_BUSCO'
queue = 'comp01'
prefix = jobname
num_nodes = 1
num_processors = 32
walltime = 1 # this is in hours

# This section prints the header/required info for the slurm script
# use a print statement for each line
print('#SBATCH --job-name=' + jobname)  # Job name
print('#SBATCH --partition', queue) # The partition to use for the job, use qstat -q to get list and choose one with E and workable walltime
print('#SBATCH --output=' + prefix + '_%j.txt') # standard output directed here, %j - job id
print('#SBATCH --error=' + prefix + '_%j.err') # standard error directed here
print('#SBATCH --mail-type=ALL') # send emails for all events - begin, end, etc
print('#SBATCH --mail-user=plymaler@obu.edu') # who to email
print('#SBATCH --nodes=' + str(num_nodes)) # Minimum number [-max] of nodes on which to distribute the Tasks
print('#SBATCH --ntasks-per-node=' + str(num_processors)) # allows you to control the distribution of Tasks on different nodes, can also use --ntasks=<n>
print('#SBATCH --time=' + str(walltime) + ':00:00') # time allocated to process, should not exceed partition walltime
print()
print()

print('export OMP_NUM_THREADS=num_processors') # OpenMP number of threads, Sets the maximum number of threads in the parallel region, should be equal to or less than ntasks-per-node value
print()

print(
'''
# load required modules
module purge
module load python/anaconda-3.7.3
source /share/apps/bin/conda-3.7.3.sh
conda activate bioconda3-el7
'''
)
# do not need module load busco.  The above lines start the bioconda3-el7 environment and busco is loaded there.
# To see all programs available in the bioconda3-el7 environment, type the three lines above (begin with module load...) into the terminal indiviually, then type conda list.
# Do still load modules for programs not available in conda environment, or run using absolute path to the program executable.
print()

print('# cd into the directory where you are submitting this script from')
print('cd $SLURM_SUBMIT_DIR')
print()

print('# copy files from storage to scratch (specify filepath if files not in directory submitting from)')
print('rsync -av MOG19_198_OBU_Sort26.fasta /scratch/$SLURM_JOB_ID')
print()

print('# cd onto the scratch disk to run the job')
print('cd /scratch/$SLURM_JOB_ID/')
print()

print('# run BUSCO (or other program).  Note output directory or filename')
print('busco -i MOG19_198_OBU_Sort26.fasta -l bacteria_odb10 -o SORT26_BUSCO -m genome -c 32')
print()

print('# copy files in output directory (use output directory from above) back to storage')
print('rsync -av SORT26_BUSCO $SLURM_SUBMIT_DIR')
