from locators.VideosLocator import Videoslocators
from pages import BasePage
import default_settings, time

class VideoPage(BasePage):

    def add_video(self):
        self._click(Videoslocators.OPEN_ADD_VIDEO_FORM)
        self._input(Videoslocators.TITLE_VIDEO, "test")
        self._input(Videoslocators.DESCRIPTION_VIDEO, "test video")
        self._input(Videoslocators.INPUT_VIDEO, default_settings.video)
        self._click(Videoslocators.ADD_VIDEO_BUTTON)
        time.sleep(15)

    def dell_all_video(self):
        try:
            while True:
                self._click(Videoslocators.OPEN_DELL_MODAL)
                self._click(Videoslocators.DELL_BUTTON)
                time.sleep(1)
        except:
            return