from enum import Enum


class SandboxToken(str, Enum):
    """Enumeration of HTML sandbox attribute token values.

    Each token selectively relaxes the strict security restrictions applied by an
    empty sandbox attribute (`sandbox=""`).
    """

    ALLOW_FORMS = "allow-forms"
    """Allows the embedded document to submit HTML forms."""

    ALLOW_MODALS = "allow-modals"
    """Allows opening modal windows via window.alert(), confirm(), prompt(), and print()."""

    ALLOW_ORIENTATION_LOCK = "allow-orientation-lock"
    """Allows locking the screen orientation via screen.orientation.lock()."""

    ALLOW_POINTER_LOCK = "allow-pointer-lock"
    """Allows capturing raw mouse pointer movement via the Pointer Lock API."""

    ALLOW_POPUPS = "allow-popups"
    """Allows opening new browsing contexts via window.open(), target="_blank", or showModalDialog()."""

    ALLOW_POPUPS_TO_ESCAPE_SANDBOX = "allow-popups-to-escape-sandbox"
    """Allows popups opened by the iframe to render without inheriting sandbox restrictions."""

    ALLOW_PRESENTATION = "allow-presentation"
    """Allows initiating a Web Presentation session (e.g., Chromecast, AirPlay)."""

    ALLOW_SAME_ORIGIN = "allow-same-origin"
    """Allows content to retain its original origin instead of forcing a unique, null origin."""

    ALLOW_SCRIPTS = "allow-scripts"
    """Allows running JavaScript and automatic features like auto-focusing inputs."""

    ALLOW_STORAGE_ACCESS_BY_USER_ACTIVATION = (
        "allow-storage-access-by-user-activation"
    )
    """Allows access to parent/unpartitioned storage via the Storage Access API upon user interaction."""

    ALLOW_TOP_NAVIGATION = "allow-top-navigation"
    """Allows navigating the top-level browsing context (the main window)."""

    ALLOW_TOP_NAVIGATION_BY_USER_ACTIVATION = (
        "allow-top-navigation-by-user-activation"
    )
    """Allows top-level navigation only if triggered by direct user gesture (clicks or taps)."""

    ALLOW_TOP_NAVIGATION_TO_CUSTOM_PROTOCOLS = (
        "allow-top-navigation-to-custom-protocols"
    )
    """Allows launching external non-web protocol handlers (e.g., mailto:, tel:, app schemes)."""

    ALLOW_DOWNLOADS = "allow-downloads"
    """Allows triggering file downloads with or without user interaction."""