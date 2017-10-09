from aiohttp import web

volume = 0

async def handle_poll(request):
    text = "volume " + str(volume) + "\n"
    return web.Response(text=text)

async def handle_beep(request):
    print("play beep!")
    print("\007")
    return web.Response(text="OK")

async def handle_setvolume(request):
    global volume  # 忘れずに
    tmp_volume = int(request.match_info['vol']) # いったん別の変数へ
    if tmp_volume >= 0 and tmp_volume <= 10:
        volume = tmp_volume
        print("set volume= " + str(volume))
    else:
        print("out of range: " + str(tmp_volume))
    return web.Response(text="OK")

app = web.Application()
app.router.add_get('/poll', handle_poll)
app.router.add_get('/playBeep', handle_beep)
app.router.add_get('/setVolume/{vol}', handle_setvolume)

web.run_app(app, host='127.0.0.1', port=12345)