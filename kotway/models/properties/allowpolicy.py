from enum import Enum


class AllowPolicy(str, Enum):
    """Enumeration of HTML 'allow' attribute Feature Policy directives.

    These directives delegate access to specific browser APIs and device hardware
    features to the embedded iframe context.
    """

    ACCELEROMETER = "accelerometer"
    """Controls access to motion sensors measuring device acceleration."""

    AMBIENT_LIGHT_SENSOR = "ambient-light-sensor"
    """Controls access to light sensors detecting ambient lighting levels."""

    AUTOPLAY = "autoplay"
    """Controls playing audio or video media automatically without user interaction."""

    BATTERY = "battery"
    """Controls access to the Battery Status API (navigator.getBattery())."""

    CAMERA = "camera"
    """Controls access to video capture devices such as webcams."""

    DISPLAY_CAPTURE = "display-capture"
    """Controls screen capture capabilities via getDisplayMedia()."""

    DOCUMENT_DOMAIN = "document-domain"
    """Controls the ability to set document.domain to relax same-origin policies."""

    ENCRYPTED_MEDIA = "encrypted-media"
    """Controls Encrypted Media Extensions (EME) required for DRM-protected video playback."""

    EXECUTION_WHILE_NOT_RENDERED = "execution-while-not-rendered"
    """Controls executing background tasks while the iframe is hidden or unrendered."""

    EXECUTION_WHILE_OUT_OF_VIEWPORT = "execution-while-out-of-viewport"
    """Controls executing tasks when the frame is positioned outside the active viewport."""

    FULLSCREEN = "fullscreen"
    """Controls requesting full-screen display modes via requestFullscreen()."""

    GAMEPAD = "gamepad"
    """Controls reading gamepad and external game controller inputs."""

    GEOLOCATION = "geolocation"
    """Controls access to geographic position data via navigator.geolocation."""

    GYROSCOPE = "gyroscope"
    """Controls access to orientation sensors measuring device rotational speed."""

    HID = "hid"
    """Controls interaction with Human Interface Devices via the WebHID API."""

    IDENTITY_CREDENTIALS_GET = "identity-credentials-get"
    """Controls authentication via the Federated Credential Management (FedCM) API."""

    IDLE_DETECTION = "idle-detection"
    """Controls detecting user idle states via the Idle Detection API."""

    MAGNETOMETER = "magnetometer"
    """Controls access to geomagnetic sensors measuring magnetic field strength."""

    MICROPHONE = "microphone"
    """Controls access to audio input devices such as microphones."""

    MIDI = "midi"
    """Controls interaction with Musical Instrument Digital Interface devices via Web MIDI."""

    PAYMENT = "payment"
    """Controls initiating payment workflows via the Payment Request API."""

    PICTURE_IN_PICTURE = "picture-in-picture"
    """Controls playing videos in floating windows via the Picture-in-Picture API."""

    PUBLICKEY_CREDENTIALS_CREATE = "publickey-credentials-create"
    """Controls creating WebAuthn security credentials (navigator.credentials.create())."""

    PUBLICKEY_CREDENTIALS_GET = "publickey-credentials-get"
    """Controls authenticating via WebAuthn credentials (navigator.credentials.get())."""

    SCREEN_WAKE_LOCK = "screen-wake-lock"
    """Controls preventing device displays from dimming or turning off."""

    SERIAL = "serial"
    """Controls communicating with serial hardware devices via the Web Serial API."""

    SPEAKER_SELECTION = "speaker-selection"
    """Controls selecting specific audio output hardware via selectAudioOutput()."""

    STORAGE_ACCESS = "storage-access"
    """Controls requesting unpartitioned third-party storage/cookie access."""

    USB = "usb"
    """Controls communicating with connected USB devices via the WebUSB API."""

    WEB_SHARE = "web-share"
    """Controls invoking native operating system sharing dialogs via navigator.share()."""

    WINDOW_MANAGEMENT = "window-management"
    """Controls multi-display placement and window inspection via Screen Detailed API."""

    XR_SPATIAL_TRACKING = "xr-spatial-tracking"
    """Controls spatial tracking features required for AR/VR via the WebXR API."""