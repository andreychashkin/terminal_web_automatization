from pages.mainpage import MainPage
from random import randint as rand
import pytest, default_settings


@pytest.mark.parametrize('protocol', ["SIP", "H323"])
def test_call_protocol(browser, protocol):
    obj = MainPage(browser)
    obj.call(protocol, resolution=rand(0, 14), speed=rand(0, 19), fps=rand(0, 6))
    obj.call_rezult(protocol)
    return


@pytest.mark.parametrize('resolution', default_settings.resolution)
def test_call_resolution_sip(browser, resolution, protocol='SIP'):
    obj = MainPage(browser)
    obj.call(protocol, resolution=resolution, speed="1536", fps=rand(0, 6))
    obj.call_rezult(protocol, resolution=resolution)
    return


@pytest.mark.parametrize('resolution', default_settings.resolution)
def test_call_resolution_h323(browser, resolution, protocol='H323'):
    obj = MainPage(browser)
    obj.call(protocol, resolution=resolution, speed="1536", fps=rand(0, 6))
    obj.call_rezult(protocol, resolution=resolution)
    return


@pytest.mark.parametrize('speed', default_settings.speed)
def test_call_speed_h323(browser, speed, protocol='H323'):
    obj = MainPage(browser)
    obj.call(protocol, resolution=rand(0, 14),speed=speed, fps=rand(0, 6))
    obj.call_rezult(protocol, speed=speed)
    return


@pytest.mark.parametrize('speed', default_settings.speed)
def test_call_speed_sip(browser, speed, protocol='SIP'):
    obj = MainPage(browser)
    obj.call(protocol, resolution=rand(0, 14), speed=speed, fps=rand(0, 6))
    obj.call_rezult(protocol, speed=speed)
    return


@pytest.mark.parametrize('fps', default_settings.fps)
def test_call_fps_h323(browser, fps, protocol='H323'):
    obj = MainPage(browser)
    obj.call(protocol, resolution=rand(0,14), speed=rand(0, 19), fps=fps)
    obj.call_rezult(protocol, fps=fps)
    return


@pytest.mark.parametrize('fps', default_settings.fps)
def test_call_fps_sip(browser, fps, protocol='SIP'):
    obj = MainPage(browser)
    obj.call(protocol, resolution=rand(0, 14), speed=rand(0, 19), fps=fps)
    obj.call_rezult(protocol, fps=fps)
    return


@pytest.mark.parametrize('number', default_settings.number)
def test_call_number_h323(browser, number, protocol='H323'):
    obj = MainPage(browser)
    obj.call(protocol, number=number)
    obj.call_rezult(protocol, number=number)
    return


@pytest.mark.parametrize('number', default_settings.number)
def test_call_number_sip(browser, number, protocol='SIP'):
    obj = MainPage(browser)
    obj.call(protocol, number=number)
    obj.call_rezult(protocol, number=number)
    return


@pytest.mark.parametrize('number', default_settings.number)
def test_call_number_sip_tcp(browser, number, protocol='SIP_TCP'):
    obj = MainPage(browser)
    obj.call(protocol, number=number)
    obj.call_rezult('SIP', number=number)
    return


@pytest.mark.xfail()
@pytest.mark.parametrize('number', default_settings.number)
def test_call_number_sip_tls(browser, number, protocol='SIP_TLS'):
    obj = MainPage(browser)
    obj.call(protocol, number=number)
    obj.call_rezult('SIP', number=number)
    return
