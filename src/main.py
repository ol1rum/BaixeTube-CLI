from pathlib import Path
from config_manager import ConfigManager
import yt_dlp, questionary, os


__version__ = "2.0.0"

class BaixeTubeApp:

    def __init__(self):
        self.config_manager = ConfigManager()
        self.downloader = Downloader(self.config_manager.get_all_settings())
        self.BASE_STYLE = questionary.Style([
            ('answer', 'fg:green bold'),
            ('pointer', 'fg:red bold'),
        ])

        self.mainMenu()

    def cleanScreen(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    def showLogo(self) -> None:
        print("""                                            
\033[37m▄▄▄▄▄▄▄                        \033[31m▄▄▄▄▄▄▄▄▄    ▄▄         \033[m
\033[37m███▀▀███▄       ▀▀             \033[31m▀▀▀███▀▀▀    ██         \033[m
\033[37m███▄▄███▀  ▀▀█▄ ██  ██ ██ ▄█▀█▄\033[31m   ███ ██ ██ ████▄ ▄█▀█▄\033[m
\033[37m███  ███▄ ▄█▀██ ██   ███  ██▄█▀\033[31m   ███ ██ ██ ██ ██ ██▄█▀\033[m
\033[37m████████▀ ▀█▄██ ██▄ ██ ██ ▀█▄▄▄\033[31m   ███ ▀██▀█ ████▀ ▀█▄▄▄\033[m
""")
        
    def mainMenu(self) -> None:
        while True:
            self.cleanScreen()
            self.showLogo()
            choice = questionary.select(
                message="",
                choices=[
                    "⬇️  Download content",
                    "⚙️  Configurations",
                    "❌ Exit"
                ],
                style=self.BASE_STYLE
            ).ask()

            match choice:
                case "⬇️  Download content":
                    self.downloadMenu()
                case "⚙️  Configurations":
                    self.configMenu()
                case "❌ Exit":
                    exit()

    def configMenu(self) -> None:
        while True:
            self.cleanScreen()
            self.showLogo()
            choice = questionary.select(
                message="",
                choices=[
                    "⚙️  Download Path",
                    "⚙️  Video Quality",
                    "⚙️  Audio Format",
                    "⚙️  Embed Thumbnail",
                    "⬅️  Back"
                ],
                style=self.BASE_STYLE
            ).ask()


            match choice:
                case "⚙️  Download Path":
                    new_path = questionary.path(
                        message="Select the download path:",
                        default=self.config_manager.get("download_path"),
                        only_directories=True,
                        style=self.BASE_STYLE
                    ).ask()
                    
                    if new_path:
                        self.config_manager.update("download_path", new_path)
                        self.downloader.update_settings(self.config_manager.get_all_settings())

                case "⚙️  Video Quality":
                    new_quality = questionary.select(
                        message="Select the video quality:",
                        choices=[
                            "Best",
                            "1080p",
                            "720p",
                            "480p",
                            "Worst",
                        ],
                        default=self.config_manager.get("video_quality"),
                        style=self.BASE_STYLE
                    ).ask()
                    
                    if new_quality:
                        self.config_manager.update("video_quality", new_quality)
                        self.downloader.update_settings(self.config_manager.get_all_settings())

                case "⚙️  Audio Format":
                    new_format = questionary.select(
                        message="Select the audio format:",
                        choices=[
                            "mp3",
                            "m4a",
                            "wav"
                        ],
                        default=self.config_manager.get("audio_format"),
                        style=self.BASE_STYLE
                    ).ask()
                    
                    if new_format:
                        self.config_manager.update("audio_format", new_format)
                        self.downloader.update_settings(self.config_manager.get_all_settings())

                case "⚙️  Embed Thumbnail":
                    new_embed = questionary.confirm(
                        message="Embed thumbnail?",
                        default=self.config_manager.get("embed_thumbnail"),
                        style=self.BASE_STYLE
                    ).ask()
                    
                    if new_embed is not None:
                        self.config_manager.update("embed_thumbnail", new_embed)
                        self.downloader.update_settings(self.config_manager.get_all_settings())

                case "⬅️  Back":
                    break

    def downloadMenu(self) -> None:
        # self.cleanScreen()
        self.showLogo()

        link = questionary.text(
            message="Enter the link:",
            style=self.BASE_STYLE
        ).ask()

        if not link:
            return

        download_type = questionary.select(
            message="Select the download type:",
            choices=[
                "Video",
                "Audio",
            ],
            style=self.BASE_STYLE
        ).ask()
        download_type_func = self.downloader.downloadVideo if download_type == "Video" else self.downloader.downloadAudio
        
        download_playlist = False
        if "list" in link or "playlist" in link:
            download_playlist = questionary.confirm(
                message="Download the entire playlist?",
                default=False,
                style=self.BASE_STYLE
            ).ask()
        
        if download_playlist:
            print("Creating playlist folder...")
            playlist_name = self.downloader.getPlaylistName(link)
            print(f"Playlist name: {playlist_name}")
            Path(
                Path(self.config_manager.get("download_path")) / playlist_name
            ).mkdir(parents=True, exist_ok=True)

            download_type_func(link, noplaylist=False, playlist_folder=playlist_name)

        else:
            download_type_func(link)

        input("Press Enter to continue...")


class Downloader:
    
    def __init__(self, settings: dict):
        self.settings = settings
        self.base_options = {
            'ignoreerrors': True,
        }

    def update_settings(self, new_settings: dict):
        """Atualiza as configurações do downloader."""
        self.settings = new_settings

    def downloadVideo(self, link: str, noplaylist: bool = True, playlist_folder: str = None) -> None:
        video_quality_map = {
            "Best": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
            "1080p": "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]/best",
            "720p": "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720][ext=mp4]/best",
            "480p": "bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[height<=480][ext=mp4]/best",
            "Worst": "worstvideo[ext=mp4]+worstaudio[ext=m4a]/worst[ext=mp4]/worst",
        }
        
        video_format = video_quality_map.get(self.settings.get("video_quality"), video_quality_map["Best"])
        print(video_format)

        use_thumbnail = self.settings.get("embed_thumbnail", True)

        opts = {
            'format': video_format,
            'noplaylist': noplaylist,
            'writethumbnail': use_thumbnail,
            'postprocessors': [{'key': 'EmbedThumbnail'}] if use_thumbnail else []
        }
        self.__download(link, opts, playlist_folder)
        
    def downloadAudio(self, link: str, noplaylist: bool = True, playlist_folder: str = None) -> None:
        use_thumbnail = self.settings.get("embed_thumbnail", True)

        postprocessors = [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': self.settings.get("audio_format", "mp3"),
                'preferredquality': '192',
            }
        ]

        if use_thumbnail:
            postprocessors.append({'key': 'EmbedThumbnail'})

        opts = {
            'format': 'bestaudio/best',
            'writethumbnail': use_thumbnail,
            'postprocessors': postprocessors,
            'noplaylist': noplaylist
        }
        self.__download(link, opts, playlist_folder)

    def __download(self, link: str, extra_opts: dict, playlist_folder: str = None) -> None:
        download_path = Path(self.settings.get("download_path"))
        use_thumbnail = self.settings.get("embed_thumbnail", True)
        
        final_path_template = download_path / '%(title)s.%(ext)s'
        if playlist_folder:
            final_path_template = download_path / playlist_folder / '%(title)s.%(ext)s'

        final_opts = self.base_options.copy()
        final_opts.update(extra_opts)
        final_opts['outtmpl'] = str(final_path_template)
        
        try:
            with yt_dlp.YoutubeDL(final_opts) as ydl:
                print('Starting download...')
                ydl.download([link])
                print('Download complete!')
        except Exception as e:
            print(f'Error: {e}')

    def getPlaylistName(self, link) -> str:
        opts_read = {
            'quiet': True,
            'extract_flat': True,
            'force_generic_extractor': False
        }

        with yt_dlp.YoutubeDL(opts_read) as ydl:
            try:
                info = ydl.extract_info(link, download=False)
                
                title = info.get('title', 'Playlist Without Name')
                return title
                
            except Exception as e:
                print(f"Error: {e}")
                return "Unknown Playlist"



if __name__ == '__main__':
    BaixeTubeApp()