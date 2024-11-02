# kafka websocket fastapi ddd

This is a basic template for Django projects configured to use Docker Compose, Makefile, and PostgreSQL.

## Requirements

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [GNU Make](https://www.gnu.org/software/make/)

## How to Use

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mizuhomizuho/kafka_websocket_fastapi.git
   cd kafka_websocket_fastapi

2. Install all required packages in `Requirements` section.


### Implemented Commands

* `make app` - up application and database/infrastructure
* `make app-logs` - follow the logs in app container
* `make app-down` - down application and all infrastructure
* `make app-shell`
* `make test`
