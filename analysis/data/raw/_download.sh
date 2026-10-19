#!/bin/bash
cd "D:/2026.10/机械应力/analysis/data/raw"
declare -A urls=(
  ["GSE342782_series_matrix.txt.gz"]="https://ftp.ncbi.nlm.nih.gov/geo/series/GSE342nnn/GSE342782/matrix/GSE342782_series_matrix.txt.gz"
  ["GSE342782_Processed_DirectInf_neuronHD10s_BulkSeq_Counts.csv.gz"]="https://ftp.ncbi.nlm.nih.gov/geo/series/GSE342nnn/GSE342782/suppl/GSE342782_Processed_DirectInf_neuronHD10s_BulkSeq_Counts.csv.gz"
  ["GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz"]="https://ftp.ncbi.nlm.nih.gov/geo/series/GSE342nnn/GSE342782/suppl/GSE342782_SeraExoTreatedHD10sBulkSeq_counts.csv.gz"
)
for name in "${!urls[@]}"; do
  url="${urls[$name]}"
  ok=0
  for try in 1 2 3 4 5; do
    curl -s --max-time 280 -o "$name" "$url"
    if gzip -t "$name" 2>/dev/null; then
      sz=$(stat -c%s "$name")
      echo "OK $name try $try size $sz"
      ok=1
      break
    else
      echo "CORRUPT $name try $try, retrying"
      sleep 2
    fi
  done
  if [ "$ok" -ne 1 ]; then echo "FAILED $name after retries"; fi
done
echo "=== final ==="
ls -la
