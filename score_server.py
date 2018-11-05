from concurrent import futures
import time
import grpc
import scorereader_pb2
import scorereader_pb2_grpc


_ONE_DAY_ = 60 * 60 * 24

class ScoreService(scorereader_pb2_grpc.ScoreReaderServicer):
        
        def Read(self, request, context):
            # here, calculate the score            
            return scorereader_pb2.ScoreResponse(data='mytest')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    scorereader_pb2_grpc.add_ScoreReaderServicer_to_server(ScoreService(), server)
    server.add_insecure_port('[::]:32100')
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()

