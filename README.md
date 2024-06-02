
# Scraper Service

`scraper_service` is a web service that grabs the HTTP GET status code of a given URL and exposes a Prometheus metric.

## Building and Running the Service

### Prerequisites

- Docker

### Build the Docker Image

```bash
docker build -t scraper_service .

# USAGE

curl --header "Content-Type: application/json" \
--request POST \
--data '{"url": "https://xxxxxxxxx"}' \
localhost:8787



```
