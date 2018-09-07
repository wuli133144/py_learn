


import os


class ringbuffer(object):

    """
      ringbuffer for stream data

    """
    authoer=""
    version=""
    def __init__(self,size):
        self.size=size
        self.buffer=[]
        self.freespace=size
        self.rpos=0
        self.wpos=0
        pass


    def __str__(self):
        return "ringbuffer for av stream"







if __name__ == '__main__':

    rbuf=ringbuffer(2)
    print(rbuf)