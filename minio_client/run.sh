# sleep while docker-compose inits
sleep 5

# config main host
mc config host add minio http://minio:9000 OMQAGGOL63D7UNVQFY8X GcY5RHNmnEWvD/1QxD3spEIGj+Vt9L7eHaAaBTkJ
mc mb minio/nasa

# config remote host
mc config host add minio_offsite http://minio_offsite:9000 OMQAGGOL63D7UNVQFY8X GcY5RHNmnEWvD/1QxD3spEIGj+Vt9L7eHaAaBTkJ
mc mb minio_offsite/nasa

# constantly mirror both buckets
while true; do
    sleep 1
    mc mirror minio/nasa minio_offsite/nasa > /dev/null
done
