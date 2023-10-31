FROM docker.io/openvino/ubuntu20_dev: 2023.1.0

ENV DEVICE=GPU

ENTRYPOINT [“/bin/bash/”, “-c”, “python3 gpu_app.py -d $DEVICE”]
