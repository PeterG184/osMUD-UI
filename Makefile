
BUILD_DIR = bin

all: dhcp_mock.build api.build

dhcp_mock.build:
	go build -o ${BUILD_DIR}/dhcp_mock ./tools/dhcp_mock

api.build:
	CGO_ENABLED=0 CC=arm-linux-gnueabi-gcc GOOS=linux GOARCH=arm GOARM=7 go build -o ${BUILD_DIR}/api ./api

clean:
	mkdir -p ${BUILD_DIR}
	rm -r ${BUILD_DIR}
