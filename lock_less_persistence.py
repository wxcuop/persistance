import os
import threading
from collections import deque

SEGMENT_SIZE = 4 * 1024 * 1024  # 4MB
MAX_SEGMENTS = 32767

class LockLessPersistence:
    def __init__(self, persistence_name):
        self.persistence_name = persistence_name
        self.streams = {}
        self.lock = threading.Lock()
        self.init_persistence()

    def init_persistence(self):
        if not os.path.exists(self.persistence_name):
            os.makedirs(self.persistence_name)
        self.streams[0] = LockFreeStream(0, os.path.join(self.persistence_name, "stream_0"))

    def create_stream(self, stream_id):
        with self.lock:
            if stream_id not in self.streams:
                self.streams[stream_id] = LockFreeStream(stream_id, os.path.join(self.persistence_name, f"stream_{stream_id}"))

    def write_to_stream(self, stream_id, data):
        if stream_id in self.streams:
            self.streams[stream_id].write(data)
        else:
            raise ValueError(f"Stream {stream_id} does not exist.")

    def read_from_stream(self, stream_id):
        if stream_id in self.streams:
            return self.streams[stream_id].read()
        else:
            raise ValueError(f"Stream {stream_id} does not exist.")

class LockLessStream:
    def __init__(self, stream_id, file_path):
        self.stream_id = stream_id
        self.file_path = file_path
        self.data_queue = deque()
        self.lock = threading.Lock()
        self.segment_count = 0

    def write(self, data):
        with self.lock:
            if len(data) > SEGMENT_SIZE:
                raise ValueError("Data exceeds segment size")
            self.data_queue.append(data)
            self._persist_data(data)

    def read(self):
        with self.lock:
            if self.data_queue:
                return self.data_queue.popleft()
            else:
                return self._read_from_file()

    def _persist_data(self, data):
        if self.segment_count >= MAX_SEGMENTS:
            raise OverflowError("Maximum number of segments reached")
        with open(self.file_path, 'a') as f:
            f.write(data + '\n')
        self.segment_count += 1

    def _read_from_file(self):
        with open(self.file_path, 'r') as f:
            return f.read()

# Example usage
persistence = LockLessPersistence("my_persistence")
persistence.create_stream(1)

# Writing to streams
persistence.write_to_stream(0, "Hello, Stream 0!")
persistence.write_to_stream(1, "Hello, Stream 1!")

# Reading from streams
print(persistence.read_from_stream(0))
print(persistence.read_from_stream(1))
