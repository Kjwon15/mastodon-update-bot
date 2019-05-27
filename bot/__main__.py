import os

from .manager import MastodonManager

if __name__ == '__main__':
    db_url = os.getenv('DATABASE_URL')
    domain = os.getenv('MASTODON_HOST')
    token = os.getenv('MASTODON_ACCESS_TOKEN')
    debug = bool(os.getenv('DEBUG', False))

    mastodon_manager = MastodonManager(db_url, domain, token, debug=debug)
    mastodon_manager.run()

