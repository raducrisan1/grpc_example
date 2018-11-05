using System;
using System.Threading.Tasks;
using Grpc.Core;

namespace grpc_example
{
    class Program
    {
        static async Task Main(string[] args)
        {
            Channel channel = new Channel("[::]:32100", ChannelCredentials.Insecure);
            var client = new ScoreReader.ScoreReaderClient(channel);
            var rsp = await client.ReadAsync(new ScoreRequest {Sourceid = "srcid"});
            System.Console.WriteLine(rsp.Data);

            await channel.ShutdownAsync();
            System.Console.WriteLine("Done");
        }
    }
}
