FROM aidandj/pyboost_build_container

WORKDIR /code2

COPY ./shmem_cpp .
COPY ./shmem_py ./shmem_py

RUN cmake .
RUN make -j