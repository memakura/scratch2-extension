# s2ext.py
# -*- coding: utf-8 -*-
from aiohttp import web


class S2EXT:
    """ Scratch 2 Offline Extension Example """
    def __init__(self):
        self.volume = 0

    async def handle_poll(self, request):
        """ Handle polling from Scratch """
        text = "volume " + str(self.volume) + "\n"
        return web.Response(text=text)

    async def handle_beep(self, request):
        """ Handle beep request from Scratch """
        print("play beep!")
        print("\007")
        return web.Response(text="OK")

    async def handle_setvolume(self, request):
        """ Handle set volume request from Scratch """
        tmp_volume = int(request.match_info['vol'])
        if tmp_volume >= 0 and tmp_volume <= 10:
            self.volume = tmp_volume
            print("set volume= " + str(self.volume))
        else:
            print("out of range: " + str(self.volume))
        return web.Response(text="OK")

    def main(self):
        """ Main routine """
        app = web.Application()
        app.router.add_get('/poll', self.handle_poll)
        app.router.add_get('/playBeep', self.handle_beep)
        app.router.add_get('/setVolume/{vol}', self.handle_setvolume)

        web.run_app(app, host='127.0.0.1', port=12345)

if __name__ == '__main__':
    s2ext = S2EXT()
    s2ext.main()
