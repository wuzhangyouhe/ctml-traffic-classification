#!/usr/bin/env bash

tshark -c 500 -i en1 -w predict.pcap -f "tcp port https"
sleep 1
sudo chmod 755 *

./1_data_collector.sh predict.pcap predict_apply.csv