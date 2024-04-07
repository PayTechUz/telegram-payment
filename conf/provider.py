"""
payment provider configurations
"""
import os


def get_provider_token(provider: list["str"]) -> str:
    """
    get provider token for specified provider
    """
    if provider == "click":
        return os.getenv("CLICK_PROVIDER_TOKEN")

    elif provider == "payme":
        return os.getenv("PAYME_PROVIDER_TOKEN")

    raise ValueError(f"invalid provider: {provider}")
