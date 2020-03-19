import speedtest


def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]

def main():
    for i in range(3):
        d, u, p = test()
        print('Test #{}'.format(i+1))
        print('Download: {:.2f}'.format(d / 1024))
        print('Upload: {:.2f}'.format(u / 1024))
        print('Ping: {}'.format(p))

if __name__ == '__main__':
    main()
