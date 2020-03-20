import TransferData
import sys
import mmap
import ctypes


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # create
        shmem = mmap.mmap(-1, ctypes.sizeof(TransferData.TransferData))
        data = TransferData.TransferData.from_buffer(shmem)
        print('Python Program - Filling Data')
        TransferData.fill(data)
        input("Press Enter to continue...")
    else:
        # get
        with open( "/dev/shm/CppTransferDataSHMEM", "r+b" ) as fd:
            shmem = mmap.mmap(fd.fileno(), ctypes.sizeof(TransferData.TransferData))
            data = TransferData.TransferData.from_buffer(shmem)
            print('Python Program - Getting Data')
            TransferData.print_data(data)
