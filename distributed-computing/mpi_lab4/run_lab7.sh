#!/bin/bash

EXE=lab7

# Кількість MPI процесів
mpi_procs=(1 4 9)

# Кількості OpenMP ниток
omp_threads=(1 2 3 4)

output_file="results.csv"
echo "MPI Procs,OpenMP Threads,Total Threads,Time (sec)" > $output_file

for np in "${mpi_procs[@]}"; do
  for nt in "${omp_threads[@]}"; do
    total_threads=$(( np * nt ))
    
    if [ $total_threads -le 12 ]; then
      echo "Запуск: MPI процеси = $np, OMP потоки= $nt (загалом $total_threads потоків)"
      export OMP_NUM_THREADS=$nt
      
      result=$(mpirun --oversubscribe -np $np ./$EXE 2>&1 | grep "Загальний час виконання" | awk '{print $4}')
        if [ $? -eq 0 ]; then
            echo "$np,$nt,$total_threads,$result" >> $output_file
            echo "- Результат: $result секунд"
        fi
    fi
  done
done

echo "Дані записано в $output_file"
