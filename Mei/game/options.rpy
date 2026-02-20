## options.rpy — Mei Visual Novel Configuration

define config.name = _("Mei — Alien Giữa Loài Người")
define config.version = "0.1"

define gui.about = _p("""
Dựa trên vở kịch sân khấu trường THPT — "Bộ phim bình thường."
Phiên bản Visual Novel, kể lại từ góc nhìn của Mai (Mei).

Một câu chuyện về mặt nạ, sự hoàn hảo giả tạo,
và hành trình tìm lại bản thân thật giữa đám đông.
""")

define build.name = "MeiVN"

## Window config
define config.screen_width = 1920
define config.screen_height = 1080

define config.save_directory = "MeiVN-save"

define config.window_title = "Mei — Alien Giữa Loài Người"

## Build configuration
init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.documentation('*.html')
    build.documentation('*.txt')
