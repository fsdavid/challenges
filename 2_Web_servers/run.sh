docker build -t challenge-2 .

# Run Docker container
docker run --name=challenge-2 \
    --rm \
    -d \
    -e PORT=3000 \
    -e BASE_URL=conabio \
    -p 3000:3000 \
    challenge-2