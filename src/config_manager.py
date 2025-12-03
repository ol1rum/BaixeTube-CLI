import json
from pathlib import Path

class ConfigManager:
    """
    Manages application configurations, including loading, saving, and updating settings.

    Configuration keys:
    - "download_path": The directory where downloaded files will be saved.
    - "video_quality": The preferred video quality for downloads (e.g., "best", "1080p").
    - "audio_format": The preferred audio format for downloads (e.g., "mp3", "m4a").
    - "embed_thumbnail": A boolean indicating whether to embed the video thumbnail in the audio file.
    """
    def __init__(self):
        # Define onde salvar o arquivo (Pasta do Usuário/.baixetube)
        self.config_dir = Path.home() / ".baixetube"
        self.config_file = self.config_dir / "config.json"
        
        # Configurações Padrão (Default)
        self.defaults = {
            "download_path": str(Path.home() / "Downloads"),
            "video_quality": "best",
            "audio_format": "mp3",
            "embed_thumbnail": True
        }
        
        self.settings = self.load_config()

    def load_config(self):
        """Carrega do arquivo ou cria se não existir."""
        if not self.config_file.exists():
            self.create_default_config()
            return self.defaults.copy()
        
        try:
            with open(self.config_file, 'r') as f:
                return json.load(f)
        except:
            return self.defaults.copy()

    def create_default_config(self):
        """Cria a pasta e o arquivo inicial."""
        self.config_dir.mkdir(parents=True, exist_ok=True)
        self.save_config(self.defaults)

    def save_config(self, new_settings):
        """Salva as alterações no arquivo JSON."""
        self.settings = new_settings
        with open(self.config_file, 'w') as f:
            json.dump(new_settings, f, indent=4)

    def get(self, key):
        return self.settings.get(key, self.defaults.get(key))

    def get_all_settings(self):
        return self.settings.copy()

    def update(self, key, value):
        self.settings[key] = value
        self.save_config(self.settings) 